# Prompts of the five tasks. Each function fills the prompt with the data of a game and returns a
# (system, user) tuple; the system message is always empty.


def gameUnderstanding(game, rules):
    prompt = f"""Below is the rulebook of the game "{game}".

<rulebook>
{rules.strip()}
</rulebook>

Explain the rules of {game} to someone who has never played it, based on the rulebook above. Organize the explanation in these sections:
1. Goal of the game
2. Setup
3. Turn structure
4. Core mechanics
5. End of the game and how to win"""
    return ("", prompt)


def gameFlawDetection(game, rules):
    prompt = f"""Below is a rulebook for the game "{game}". It may contain problems.

<rulebook>
{rules.strip()}
</rulebook>

Review this rulebook and point out any missing, ambiguous or inconsistent rules.
For each problem you find, explain what is wrong and suggest a correction."""
    return ("", prompt)


def gameSimulation(game, rules, gameStage):
    prompt = f"""You are playing {game}. These are the rules:

<rulebook>
{rules.strip()}
</rulebook>

The current situation is:
{gameStage}

Suggest the best next move and justify your answer."""
    return ("", prompt)


def gameGeneration(mechanics, theme, nplayers):
    prompt = f"""You have to come up with a new game which follows these mechanics: {mechanics}.
The game must be a {theme} game, and it is for {nplayers} players.
Explain the rules in a simplified form and create a name for it."""
    return ("", prompt)


def gameVariant(game, rules):
    prompt = f"""Below is the rulebook of the game "{game}".

<rulebook>
{rules.strip()}
</rulebook>

Invent a variant of {game} with alternative rules. You may add new cards, pieces or rules, as long as they are consistent with the original rules. If your variant removes or replaces an original rule, state it explicitly. Before explaining the variant, list the additional game components it requires, or write that none are needed. Then explain the new or modified rules of the variant; you do not need to repeat the rules that stay the same as in the original rulebook. For each change, explain how it works and how it affects the way the game is played. Give the variant a name."""
    return ("", prompt)
