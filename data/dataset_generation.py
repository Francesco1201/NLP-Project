# Data for the Generation part. generationSpecs: one specification per game category (mechanics, theme and
# number of players) for the Generation of a New Game task. variantGames: the base games of the Variant task, one per category.

generationSpecs = {
    "abstract_deterministic": {
        "mechanics": "two players take turns moving or placing pieces on a checkered board, with perfect information and no dice or cards",
        "theme": "dinosaur",
        "nplayers": "2",
    },
    "low-interaction-procedural-games": {
        "mechanics": "players take tiles from a shared supply and place them on their own personal board to form patterns that score points",
        "theme": "medieval knights",
        "nplayers": "2-4",
    },
    "exception-heavy rule systems": {
        "mechanics": "players get rid of their cards by matching a property of the top card of the discard pile, and special cards change the rules",
        "theme": "pizza",
        "nplayers": "3-6",
    },
    "thematic games with randomness": {
        "mechanics": "cooperative play, movement on a modular board, dice and event cards",
        "theme": "treasure-hunting archaeologist adventure",
        "nplayers": "2-4",
    },
    "social/party games": {
        "mechanics": "hidden roles, group discussion and voting",
        "theme": "pirate",
        "nplayers": "5-8",
    },
}

variantGames = [
    "checkers",
    "ticket-to-ride",
    "exploding-kittens",
    "clue",
    "werewolf",
]
