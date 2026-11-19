# Functions that run one task on one game (or specification) with a model.
# Each function builds the prompt, checks that it fits in the context of the
# model, generates the answer and returns it together with its metadata.

from prompts import gameUnderstanding, gameFlawDetection, gameSimulation, gameGeneration, gameVariant

# Raise an error if prompt + answer would exceed the context length of the model.
def checkContextLength(model, prompt, max_new_tokens, gameName):
    promptTokens = model.countTokens(*prompt)
    if promptTokens + max_new_tokens > model.max_context:
        raise ValueError(
            f"{gameName}: the prompt has {promptTokens} tokens + {max_new_tokens} for the answer, "
            f"but the model can handle only {model.max_context}."
        )

# Common steps of the tasks that only need the rulebook (Explain, Flaw Detection, Variant).
def runPrompt(model, makePrompt, gameName, gameData, max_new_tokens, seed):
    prompt = makePrompt(gameName, gameData["rules_text"])
    checkContextLength(model, prompt, max_new_tokens, gameName)
    result = model.generateOut(prompt, max_new_tokens=max_new_tokens, seed=seed)
    return {
        "game": gameName,
        "category": gameData["category"],
        "seed": seed,
        **result,
    }


def testGameUnderstanding(model, gameName, gameData, max_new_tokens=1500, seed=None):
    return {"task": "explain",
            **runPrompt(model, gameUnderstanding, gameName, gameData, max_new_tokens, seed)}


def testGameFlawDetection(model, gameName, flawedGameData, max_new_tokens=1500, seed=None):
    return {"task": "flaw_detection",
            **runPrompt(model, gameFlawDetection, gameName, flawedGameData, max_new_tokens, seed)}


def testGameSimulation(model, gameName, gameData, gameStage, max_new_tokens=1500, seed=None):
    prompt = gameSimulation(gameName, gameData["rules_text"], gameStage)
    checkContextLength(model, prompt, max_new_tokens, gameName)
    result = model.generateOut(prompt, max_new_tokens=max_new_tokens, seed=seed)
    return {
        "task": "simulation",
        "game": gameName,
        "category": gameData["category"],
        "game_stage": gameStage,
        "seed": seed,
        **result,
    }


def testGameGeneration(model, category, spec, max_new_tokens=1500, seed=None):
    prompt = gameGeneration(spec["mechanics"], spec["theme"], spec["nplayers"])
    checkContextLength(model, prompt, max_new_tokens, category)
    result = model.generateOut(prompt, max_new_tokens=max_new_tokens, seed=seed)
    return {
        "task": "generation",
        "game": None,
        "category": category,
        "mechanics": spec["mechanics"],
        "theme": spec["theme"],
        "nplayers": spec["nplayers"],
        "seed": seed,
        **result,
    }


def testGameVariant(model, gameName, gameData, max_new_tokens=1500, seed=None):
    return {"task": "variant",
            **runPrompt(model, gameVariant, gameName, gameData, max_new_tokens, seed)}