# Wrapper classes for the chat models tested in the project.
# Every model is loaded from the Hugging Face Hub and used through the same interface
# (ChatModel), so that the test functions do not depend on the specific model.



import time
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig

# Sampling parameters shared by all models and all tasks.
generation_settings = dict(
    do_sample=True,
    temperature=0.7,
    top_p=0.9,
    repetition_penalty=1.1,
)


# Base class: loads a model and its tokenizer and generates answers to a prompt.
# Subclasses only set the model name on the Hugging Face Hub and, if needed,
# options for the chat template or the 4-bit quantization.
class ChatModel:
    model_name = None
    use_system_message = True
    template_options = {}
    
    # Load tokenizer and model on the given device; quantize=True loads the model in 4 bit.
    def __init__(self, device, quantize=False):
        self.device = device
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)

        if quantize:
            # 4-bit NF4 quantization with double quantization, used for the 7B models
            bnbConfig = BitsAndBytesConfig(
                load_in_4bit=True,
                bnb_4bit_compute_dtype=torch.float16,
                bnb_4bit_use_double_quant=True,
                bnb_4bit_quant_type="nf4",
            )
            self.model = AutoModelForCausalLM.from_pretrained(
                self.model_name, quantization_config=bnbConfig, device_map="auto"
            )
        else:
            # newer versions of transformers use dtype, older ones torch_dtype
            try:
                self.model = AutoModelForCausalLM.from_pretrained(self.model_name, dtype=torch.float32).to(device)
            except TypeError:
                self.model = AutoModelForCausalLM.from_pretrained(self.model_name, torch_dtype=torch.float32).to(device)
        self.model.eval()
        
        # some tokenizers have no padding token so the end-of-sequence token is used instead
        if self.tokenizer.pad_token_id is None:
            self.tokenizer.pad_token = self.tokenizer.eos_token

        # maximum number of tokens (prompt + answer) the model can handle
        self.max_context = getattr(self.model.config, "max_position_embeddings", 4096)

    # Build the list of chat messages, models without a system role (Mistral) receive the system text at the beginning of the user message.
    def buildMessages(self, system, user):
        if system and self.use_system_message:
            return [{"role": "system", "content": system},
                    {"role": "user", "content": user}]
        if system:
            user = system + "\n\n" + user
        return [{"role": "user", "content": user}]

    # Format the messages with the chat template of the model and return the token ids.
    def tokenize(self, system, user):
        messages = self.buildMessages(system, user)
        encoded = self.tokenizer.apply_chat_template(
            messages,
            add_generation_prompt=True,
            return_tensors="pt",
            return_dict=True,
            **self.template_options,
        )
        return encoded["input_ids"]

    # Number of tokens of the formatted prompt.
    def countTokens(self, system, user):
        return int(self.tokenize(system, user).shape[-1])

    # Generate the answer to a prompt.
    # prompt is a (system, user) tuple or a plain string. Returns a dictionary with the answer, the number of input and output tokens,
    # whether the answer reached the max_new_tokens limit and the generation time in seconds.
    def generateOut(self, prompt, max_new_tokens=600, seed=None):
        system, user = prompt if isinstance(prompt, tuple) else ("", prompt)

        input_ids = self.tokenize(system, user).to(self.model.device)
        prompt_length = int(input_ids.shape[-1])
        
        # fixed seed for the sampling, one per iteration
        if seed is not None:
            torch.manual_seed(seed)
            if torch.cuda.is_available():
                torch.cuda.manual_seed_all(seed)

        start = time.time()
        with torch.no_grad():
            outputs = self.model.generate(
                input_ids=input_ids,
                attention_mask=torch.ones_like(input_ids),
                max_new_tokens=max_new_tokens,
                pad_token_id=self.tokenizer.pad_token_id,
                **generation_settings,
            )
            
        # the output contains the prompt followed by the answer. Only the answer is kept.  
        answer_tokens = outputs[0][prompt_length:]
        answer = self.tokenizer.decode(answer_tokens, skip_special_tokens=True).strip()

        return {
            "output": answer,
            "input_tokens": prompt_length,
            "output_tokens": int(answer_tokens.shape[-1]),
            "hit_max_new_tokens": int(answer_tokens.shape[-1]) >= max_new_tokens,
            "seconds": round(time.time() - start, 2),
        }


class Qwen(ChatModel):
    model_name = "Qwen/Qwen2.5-0.5B-Instruct"
    template_options = {"enable_thinking": False}


class Llama1B(ChatModel):
    model_name = "meta-llama/Llama-3.2-1B-Instruct"

    
class Qwen7B(ChatModel):
    model_name = "Qwen/Qwen2.5-7B-Instruct"
    template_options = {"enable_thinking": False}
 
    def __init__(self, device):
        super().__init__(device, quantize=True)

# quantized in 4 bit; its chat template has no system role.
class Mistral7B(ChatModel):
    model_name = "mistralai/Mistral-7B-Instruct-v0.3"
    use_system_message = False

    def __init__(self, device):
        super().__init__(device, quantize=True)