# Game of Thoughts

This project studies how well large language models of different sizes understand, apply and generate rules for board games. Four instruction-tuned models are tested on rulebooks of 15 board games, divided into five categories, in five tasks grouped in three parts:

| Part | Task | What the model is asked to do |
|---|---|---|
| Understanding | Explain | Explain the rules of a game to someone who has never played it, given its rulebook |
| Understanding | Flaw Detection | Find the missing, ambiguous or inconsistent rules injected into a rulebook and suggest corrections |
| Simulation | Simulation | Suggest and justify the best next move in a given game situation |
| Generation | Generation of a New Game | Create a new game from mechanics, theme and number of players |
| Generation | Variant | Invent a variant of an existing game, given its rulebook |

Every prompt is run 3 times per model (660 answers in total). All answers were scored by hand with task-specific rubrics; the scores and the analysis are included in the repository.

## Models

| Short name | Hugging Face model | Precision |
|---|---|---|
| Qwen 0.5B | `Qwen/Qwen2.5-0.5B-Instruct` | full precision |
| Llama 1B | `meta-llama/Llama-3.2-1B-Instruct` | full precision |
| Mistral 7B | `mistralai/Mistral-7B-Instruct-v0.3` | 4-bit (NF4, bitsandbytes) |
| Qwen 7B | `Qwen/Qwen2.5-7B-Instruct` | 4-bit (NF4, bitsandbytes) |

## Repository structure

```
.
├── src/                      # code used to run the models
│   ├── models.py             # ChatModel base class and one subclass per model
│   ├── prompts.py            # the prompt of each task
│   └── runTest.py            # functions that run one task on one game
├── data/                     # datasets
│   ├── dataset.py            # the 25 original rulebooks (5 per category)
│   ├── dataset_flaws.py      # flaws injected into the rulebooks (Flaw Detection)
│   ├── injected_flaws.md     # readable list of the injected flaws
│   ├── dataset_simulation.py # game situations and reference moves (Simulation)
│   └── dataset_generation.py # specifications (New Game) and base games (Variant)
├── notebooks/                # notebooks that generate the answers (Google Colab)
│   ├── game_understanding.ipynb
│   ├── game_simulation.ipynb
│   └── game_generation.ipynb
├── results/                  # model answers and evaluation workbooks
│   ├── Results_game_understanding/
│   ├── Results_simulation/
│   └── Results_generation/
└── evaluation/               # analysis of the scores
    ├── analysis.ipynb        # builds the summary tables
    ├── metrics.py            # loads the scores and computes the tables
    ├── scores/               # scores exported from the workbooks (CSV)
    └── tables/               # summary tables (CSV and LaTeX)
```

### Results and evaluation workbooks

Each folder in `results/` contains:

- `results_<model>.json`: the answers of one model, one entry per prompt and iteration, with the model, the iteration, the task, the game (or category), the seed, the answer, the number of input and output tokens, whether the answer reached the token limit and the generation time.
- An Excel workbook (`Understanding_Evaluation.xlsx`, `Simulation_Evaluation.xlsx`, `Generation_Evaluation.xlsx`): **the workbooks used to score the answers**. Each row contains an answer of a model, the scores of every criterion and the notes that justify them; the reference material used for the scoring is next to the scores (ground truth of the injected flaws, reference moves, checklists of the core mechanics and of the constraints, core of each base game for the variants).

| Workbook | Sheets |
|---|---|
| `Understanding_Evaluation.xlsx` | `Explain`, `FlawDetection_output` (one row per answer), `FlawDetection_flaws` (one row per injected flaw) |
| `Simulation_Evaluation.xlsx` | `Simulation` |
| `Generation_Evaluation.xlsx` | `Generation`, `Variant` |

The CSV files in `evaluation/scores/` contain the same scores exported from the workbooks, and are the input of the analysis.

### Evaluation criteria

- **1-5 scale** (reported as means): Task understanding, Coverage, Consistency, Hallucination, Constraint adherence, Completeness, Playability. For Consistency, Hallucination and Playability the score depends on the number of critical and minor problems (no problems: 5; 1-2 minor: 4; 1 critical and/or 4 or more minor: 3; 2-3 critical: 2; more than 3 critical: 1).
- **0-2 scale** (reported as the percentage of answers with score 2 / 1 / 0): Move correctness (best / acceptable / wrong move), Meaningful variant, Fix quality, Balance (no evident imbalance / not assessable / evident imbalance), Fun.
- **Flaw Detection**: Detected (0/1) for each injected flaw, reported as recall; Type correct (0/1) and Fix quality computed on detected flaws; Invented problems as a count per answer.

## Environment

The answers were generated on **Google Colab**, mostly on an **NVIDIA A100** GPU; some runs were executed on an **NVIDIA L4** when the A100 was not available.

| Software | Version |
|---|---|
| Python | 3.13 |
| PyTorch | 2.14.1 (CUDA 13.0) |
| Transformers | 5.22.1 |
| bitsandbytes | 0.50.2 |

The notebooks install bitsandbytes and accelerate in their first cell; the other libraries (tqdm, pandas) are already available on Colab. The analysis only needs pandas.

Generation parameters, the same for all models and tasks: sampling with `temperature=0.7`, `top_p=0.9`, `repetition_penalty=1.1`, `max_new_tokens=1500`; one fixed seed per iteration (43, 44, 45). Every prompt is sent as a single user message, formatted with the chat template of the model.

## Reproducing the experiment

### 1. Generate the answers

1. Copy the repository to Google Drive, in a folder named `Progetto NLP 2026` in `My Drive` (or change `basePath` in the second cell of each notebook).
2. The Llama and Mistral models are gated on Hugging Face: accept their licence on the model pages and add a Hugging Face access token to Colab (Secrets, name `HF_TOKEN`).
3. Open a notebook in Colab with a GPU runtime (an A100 or L4 is recommended for the 7B models) and run all the cells:
   - `notebooks/game_understanding.ipynb`: Explain and Flaw Detection;
   - `notebooks/game_simulation.ipynb`: Simulation;
   - `notebooks/game_generation.ipynb`: Generation of a New Game and Variant.

The answers are saved in `results/` after every generation. If a session is interrupted, running the notebook again skips the answers already saved; to regenerate everything, delete the JSON files first.

**Note on reproducibility.** The fixed seeds make the runs repeatable on the same hardware and with the same library versions, but the exact answers can change on a different GPU or with different versions of PyTorch, Transformers or bitsandbytes. For this reason, all the answers used for the evaluation are included in `results/`.

### 2. Build the summary tables

Open `evaluation/analysis.ipynb` (locally or in Colab) and run all the cells. It reads the scores in `evaluation/scores/`, checks that the number of scores per model is complete and saves in `evaluation/tables/`:

- `full_results`: all criteria of all tasks, one column per model;
- `category_results`: the same criteria, one column per game category (all models together);
- `category_results_<model>`: the same table by game category for each model.

Each table is saved as CSV and as a LaTeX table.

## Use of AI tools

The code, the dataset preparation and the scoring were carried out with the assistance of Claude Opus 5.5 (Anthropic); every score was reviewed by the author. Details are given in the AI disclaimer of the report.
