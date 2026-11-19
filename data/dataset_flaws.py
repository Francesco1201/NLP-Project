# Flaws injected into the rulebooks for the Flaw Detection task.
# FLAWS lists three flaws per game, one per type:
# - missing: the sentence in "find" is removed;
# - ambiguous: the sentence in "find" is replaced by the vaguer "new";
# - inconsistent: the sentence "add", which contradicts "find", is added after it.
# The flawed rulebooks are built from the original ones by buildFlawedGames.

import re

FLAWS = {
    "tic-tac-toe": [
        {"type": "missing",
         "find": 'The player who is playing "X" always goes first.',
         "problem": "It is not stated who goes first."},
        {"type": "ambiguous",
         "find": "If all squares are filled and neither player has made a complete row of Xs or Os, then the game is a draw.",
         "new": "If the board gets crowded and nobody seems able to win, the game may be considered over.",
         "problem": "The draw condition is vague (when is the grid 'crowded'? who decides?)."},
        {"type": "inconsistent",
         "find": "then that player wins.",
         "add": "A player needs four marks in a row to win.",
         "problem": "Contradiction: first three marks in a row win, then four are needed (impossible on a 3x3 grid)."},
    ],
    "connect-four": [
        {"type": "missing",
         "find": "Each disc will fall to the lowest unoccupied space within the selected column.",
         "problem": "The 'gravity' rule is missing: it is not said where the disc stops in the column."},
        {"type": "ambiguous",
         "find": "If all slots are filled before either player achieves this, the game ends in a draw.",
         "new": "If the board fills up, the outcome is decided in some other way.",
         "problem": "It is unclear what happens if the grid fills up with no winner (it should be a draw)."},
        {"type": "inconsistent",
         "find": "into their chosen column from the top of the grid.",
         "add": "On each turn a player drops two discs.",
         "problem": "Contradiction: one disc is played at a time, but then two discs per turn."},
    ],
    "checkers": [
        {"type": "missing",
         "find": "When a man reaches the farthest row forward, known as the kings row or crown head, it becomes a king.",
         "problem": "The condition for becoming a king is missing, even though kings are mentioned later."},
        {"type": "ambiguous",
         "find": "Only the dark squares of the checkerboard are used.",
         "new": "Some of the squares of the checkerboard are used.",
         "problem": "It is not specified which squares are used (only the dark ones)."},
        {"type": "inconsistent",
         "find": "The player with the darker color moves first, then players alternate turns.",
         "add": "The player with the light pieces always makes the first move.",
         "problem": "Contradiction about who moves first (dark vs light)."},
    ],
    "nine-mens-morris": [
        {"type": "missing",
         "find": "A piece in an opponent's mill, however, can be removed only if no other pieces are available.",
         "problem": "The protection of pieces that are part of a mill is missing."},
        {"type": "ambiguous",
         "find": "Each player has nine pieces, or men, usually coloured black and white.",
         "new": "Each player has several pieces, or men, usually coloured black and white.",
         "problem": "The number of pieces per player is not specified."},
        {"type": "inconsistent",
         "find": 'A piece may not "jump" another piece.',
         "add": "During phase two, a man may jump over an adjacent piece to reach a vacant point.",
         "problem": "Contradiction: in phase two pieces cannot jump, but then they can."},
    ],
    "reversi-othello": [
        {"type": "missing",
         "find": "All of the opponent's pieces between these two pieces are 'captured' and turned over to match the player's colour.",
         "problem": "The rule that flanked opponent pieces are flipped is missing (core mechanic)."},
        {"type": "ambiguous",
         "find": "For the first four moves, the players must play to one of the four squares in the middle of the board",
         "new": "For the first few moves, the players must play near the middle of the board",
         "problem": "It is unclear for how many moves and on which squares players must play at the start."},
        {"type": "inconsistent",
         "find": "A player's objective is to have more of their allocated colour face upwards at the end of the game.",
         "add": "The player with the fewest pieces of their colour on the board at the end wins.",
         "problem": "Contradiction about the winning condition (more pieces vs fewer pieces)."},
    ],
    "ticket-to-ride": [
        {"type": "missing",
         "find": "If a Locomotive card is one of the five face-up cards, the player who draws it may only draw one card, instead of two.",
         "problem": "The rule that taking a face-up Locomotive counts as two cards is missing."},
        {"type": "ambiguous",
         "find": "When one player’s stock of colored plastic trains gets down to only 0,1 or 2 trains left",
         "new": "When one player’s stock of colored plastic trains gets low",
         "problem": "The end-of-game condition has no precise threshold (0, 1 or 2 trains)."},
        {"type": "inconsistent",
         "find": "A player may claim any open route on the board.",
         "add": "On his turn a player may claim up to two routes.",
         "problem": "Contradiction: at most one route per turn, but also up to two."},
    ],
    "carcassonne": [
        {"type": "missing",
         "find": "If there are multiple meeples in a single scored feature, the player with the most meeples is awarded full points and all other players receive nothing.",
         "problem": "The majority rule when several meeples share a feature is missing."},
        {"type": "ambiguous",
         "find": "Start by distributing 7 meeples of the color of their choice to each player",
         "new": "Start by distributing a handful of meeples of the color of their choice to each player",
         "problem": "The number of starting meeples per player is not specified (7)."},
        {"type": "inconsistent",
         "find": "You may not place a meeple in a feature where there already is at least one other meeple.",
         "add": "You may always place your meeple on a road or city even if another player's meeple already occupies it.",
         "problem": "Contradiction: a meeple cannot be placed in an occupied feature, but then it always can."},
    ],
    "splendor": [
        {"type": "missing",
         "find": "Players may not have more than three reserved cards in hand, and the only way to get rid of a card is to buy it (see below).",
         "problem": "The limit of three reserved cards in hand is missing."},
        {"type": "ambiguous",
         "find": "A player can never have more than 10 tokens at the end of their turn (including jokers). If this happens, they must return tokens until they only have 10 left.",
         "new": "A player should not hold too many tokens at the end of their turn; if they do, they must return some.",
         "problem": "The token limit has no precise number (10)."},
        {"type": "inconsistent",
         "find": "In case of a tie, the player who has purchased the fewest development cards wins.",
         "add": "In case of a tie, the player with the most development cards wins.",
         "problem": "Contradiction in the tie-break (fewest cards vs most cards)."},
    ],
    "kingdomino": [
        {"type": "missing",
         "find": "- Or connect it to another domino matching at least 1 of its landscape (horizontally or vertically only).",
         "problem": "The rule for connecting dominoes is missing (at least one side with the same landscape)."},
        {"type": "ambiguous",
         "find": "Each property will give you as much prestige points as the NUMBER OF SQUARES multiplied with the NUMBER OF SPECIFIC CROWNS (see back of rules) appearing on the property.",
         "new": "Each property will give you prestige points based on its size and the crowns appearing on it.",
         "problem": "The scoring calculation is not specified (squares x crowns)."},
        {"type": "inconsistent",
         "find": "All your dominoes must fit in 5x5 grid.",
         "add": "There is no limit to the size of your kingdom.",
         "problem": "Contradiction: the kingdom must fit in a 5x5 grid, but then it has no size limit."},
    ],
    "azul": [
        {"type": "missing",
         "find": "If the pattern line already holds tiles, you may only add tiles of the same color to it.",
         "problem": "The rule that a pattern line holds a single colour is missing."},
        {"type": "ambiguous",
         "find": "In a 2-player game, place 5 Factory displays. • In a 3-player game, place 7 Factory displays. • In a 4-player game, place 9 Factory displays.",
         "new": "Place a number of Factory displays that depends on the number of players.",
         "problem": "The number of Factory displays by player count is not specified (5/7/9)."},
        {"type": "inconsistent",
         "find": "Gain 7 points for each complete vertical line of 5 consecutive tiles on your wall.",
         "add": "Vertical lines give no bonus at the end of the game.",
         "problem": "Contradiction about the bonus for complete columns (7 points vs no bonus)."},
    ],
    "crazy-eights": [
        {"type": "missing",
         "find": "Players may do so if the card they want to get rid of is the same number or suit of the card flipped up.",
         "problem": "The rule about which cards can be played (same number or suit) is missing."},
        {"type": "ambiguous",
         "find": "they must draw cards from the pile until they can do so or until they’ve drawn a maximum of five cards.",
         "new": "they must draw some cards from the pile.",
         "problem": "It is unclear how many cards are drawn when a player cannot play (until able, max 5)."},
        {"type": "inconsistent",
         "find": "- Aces are worth 1 point",
         "add": "- Aces are worth 11 points",
         "problem": "Contradiction about the value of aces (1 vs 11 points)."},
    ],
    "uno": [
        {"type": "missing",
         "find": 'If a player forgets to say "Uno!" when they have one card left and is caught, that player must draw two cards.',
         "problem": "The penalty for not saying 'Uno!' is missing."},
        {"type": "ambiguous",
         "find": "The dealer shuffles and deals 7 cards to each player.",
         "new": "The dealer shuffles and deals several cards to each player.",
         "problem": "The number of starting cards is not specified (7)."},
        {"type": "inconsistent",
         "find": "Skip - The next player is skipped.",
         "add": "When a Skip is played, the next player takes two turns in a row.",
         "problem": "Contradiction about the effect of the Skip card (skip a turn vs play twice)."},
    ],
    "fluxx": [
        {"type": "missing",
         "find": "If it contradicts a New Rule already in play, discard the old rule.",
         "problem": "It is missing what to do when a New Rule contradicts a rule already in play."},
        {"type": "ambiguous",
         "find": "Shuffle the deck and deal three cards to each player.",
         "new": "Shuffle the deck and deal a few cards to each player.",
         "problem": "The number of starting cards is not specified (3)."},
        {"type": "inconsistent",
         "find": "That player wins instantly, no matter whose turn it is!",
         "add": "A player can only win at the end of their own turn.",
         "problem": "Contradiction: a player wins at once even on another player's turn, but then only at the end of their own turn."},
    ],
    "exploding-kittens": [
        {"type": "missing",
         "find": "Force any other player to give you 1 card from their hand. They choose which card to give you.",
         "problem": "The Favor card is listed but its effect is not described."},
        {"type": "ambiguous",
         "find": "Peek at the top 3 cards from the Draw Pile",
         "new": "Peek at some of the top cards from the Draw Pile",
         "problem": "See the Future does not specify how many cards are seen (3)."},
        {"type": "inconsistent",
         "find": "2- Shuffle the remaining deck and deal 4 cards face down to each player.",
         "add": "Each player receives 7 cards.",
         "problem": "Contradiction about the number of starting cards (4 + Defuse = 5 vs 7)."},
    ],
    "mao": [
        {"type": "missing",
         "find": "If the player is unable to do so, they must draw one card and knock on the table.",
         "problem": "It is missing what a player does when they cannot play a card."},
        {"type": "ambiguous",
         "find": "Whenever a rule is broken, the player is penalized by being given one card from the draw pile.",
         "new": "Whenever a rule is broken, the player may be penalized somehow.",
         "problem": "The penalty for breaking a rule is not specified (one card from the deck)."},
        {"type": "inconsistent",
         "find": "game play will begin with the player to the left of the dealer and continue clockwise from there.",
         "add": "The dealer always plays the first card.",
         "problem": "Contradiction about who plays first (player left of the dealer vs dealer)."},
    ],
    "monopoly": [
        {"type": "missing",
         "find": "Each player is given $1,500 divided as follows: 2 each of $500s, $100s and $50s; 6 $40s; 5 each of $10s, $ 5s and $1s.",
         "problem": "The starting money of each player is missing ($1,500)."},
        {"type": "ambiguous",
         "find": 'estimate your tax at $900 and pay the Bank, or you may pay 10"%" of your total worth to the Bank.',
         "new": "pay either a fixed amount or a percentage of your total worth to the Bank.",
         "problem": "The Income Tax does not specify the fixed amount or the percentage."},
        {"type": "inconsistent",
         "find": "Two or more tokens may rest on the same space at the same time.",
         "add": "Only one token may occupy a space at any time.",
         "problem": "Contradiction: several tokens can share a space, but then only one."},
    ],
    "risk": [
        {"type": "missing",
         "find": "In case of a tie, the defender always wins.",
         "problem": "The rule that ties in the dice go to the defender is missing."},
        {"type": "ambiguous",
         "find": "move as many armies as you’ d like from one (and only one) of your territories into one (and only one) of your adjacent territories.",
         "new": "move some armies between your territories.",
         "problem": "The final move does not specify how many territories and to where (one, adjacent)."},
        {"type": "inconsistent",
         "find": "The attacker can never lose more than 2 armies on a single roll.",
         "add": "The attacker may lose up to 3 armies on a single roll.",
         "problem": "Contradiction about the maximum number of armies lost per roll (2 vs 3)."},
    ],
    "clue": [
        {"type": "missing",
         "find": "Remember: You may make only one Accusation during a game.",
         "problem": "The limit of one accusation per game is missing."},
        {"type": "ambiguous",
         "find": "Roll the die and move your token the number of squares you rolled.",
         "new": "Roll the die and move your token.",
         "problem": "It is not specified how many squares a player moves."},
        {"type": "inconsistent",
         "find": "the player with the red token— always plays first.",
         "add": "Colonel Mustard always plays first.",
         "problem": "Contradiction about who starts (Miss Scarlet vs Colonel Mustard)."},
    ],
    "forbidden-island": [
        {"type": "missing",
         "find": "If the matching Island tile is already flooded, it sinks into the abyss! Remove it and the matching Flood card from the game and place them out of play.",
         "problem": "It is missing what happens when the card of an already flooded tile is drawn (it sinks)."},
        {"type": "ambiguous",
         "find": "You may only have 5 cards in your hand, including Treasure and Special Action cards. If you ever find that you have 6 or more cards",
         "new": "You may only have a limited number of cards in your hand, including Treasure and Special Action cards. If you ever find that you have too many cards",
         "problem": "The hand limit has no precise number (5)."},
        {"type": "inconsistent",
         "find": "• You may capture a treasure on a flooded tile.",
         "add": "• You may never capture a treasure while standing on a flooded tile.",
         "problem": "Contradiction: a treasure can be captured on a flooded tile, but then never."},
    ],
    "the-game-of-life": [
        {"type": "missing",
         "find": "Spin the spinner and move your car the number of spaces shown.",
         "problem": "It is missing how players move during their turn."},
        {"type": "ambiguous",
         "find": "Collect retirement bonuses: 1st: $400K 2nd: $300K 3rd: $200K 4th: $100K",
         "new": "Collect a retirement bonus that depends on your arrival order.",
         "problem": "The retirement bonuses have no amounts."},
        {"type": "inconsistent",
         "find": "Collect $100K per Pet card.",
         "add": "Pet cards are worth nothing at the end of the game.",
         "problem": "Contradiction about the final value of Pet cards ($100K vs nothing)."},
    ],
    "mafia": [
        {"type": "missing",
         "find": "If the majority of the players (not counting the accused) votes for “Guilty as member of the Mafia,” the suspected player is “sentenced to death” and s/he is out of the game until the end of the round.",
         "problem": "It is missing how a suspect is eliminated in the Day phase (majority vote)."},
        {"type": "ambiguous",
         "find": "6-7 players: 2 black cards + others red / 8-10 players: 3 black cards + others red / 11-13 players: 4 black cards + others red / 14-16 players: 5 black cards + others red",
         "new": "a few black cards (more with larger groups) + others red",
         "problem": "The number of black cards (Mafia) by player count is not specified."},
        {"type": "inconsistent",
         "find": "Honest players have to suspect everybody, but they have an advantage of being the majority.",
         "add": "The Mafia always outnumber the Honest players.",
         "problem": "Contradiction: the Honest are the majority, but then the Mafia always outnumber them."},
    ],
    "werewolf": [
        {"type": "missing",
         "find": "The person chosen, which could be themself, will survive if the Werewolves chose the same player to kill.",
         "problem": "The effect of the Doctor's healing is missing."},
        {"type": "ambiguous",
         "find": "You need at least 7 people to play.",
         "new": "You need a good number of people to play.",
         "problem": "The minimum number of players is not specified (7)."},
        {"type": "inconsistent",
         "find": "The Werewolves win if the number of Werewolves equal the number of Villagers left.",
         "add": "The Werewolves only win when every Villager has been killed.",
         "problem": "Contradiction about the Werewolves' winning condition (equal numbers vs everyone dead)."},
    ],
    "dixit": [
        {"type": "missing",
         "find": "Note: You’re not allowed to vote for your own image.",
         "problem": "The rule against voting for your own card is missing."},
        {"type": "ambiguous",
         "find": "In any other case, the storyteller scores 3 points and so do the players who found his image.",
         "new": "In any other case, the storyteller and the players who found his image score some points.",
         "problem": "The score in the normal case is not specified (3 points)."},
        {"type": "inconsistent",
         "find": "The game ends when the last card from the pack has been drawn.",
         "add": "The game ends as soon as a player reaches 30 points on the scoring track.",
         "problem": "Two conflicting end-of-game conditions (deck exhausted vs 30 points)."},
    ],
    "codenames": [
        {"type": "missing",
         "find": "The starting team has 9 words to guess. The other team has 8.",
         "problem": "It is missing how many words each team must guess (9 and 8)."},
        {"type": "ambiguous",
         "find": "You also say one number, which tells your teammates how many codenames are related to your clue.",
         "new": "You may also give some indication of how far your clue reaches.",
         "problem": "It is unclear that the clue must come with a number of related words."},
        {"type": "inconsistent",
         "find": "The field operatives must always make at least one guess.",
         "add": "Touching an innocent bystander does not end your turn.",
         "problem": "Contradiction: touching an innocent bystander ends the turn, but then it does not."},
    ],
    "the_resistance": [
        {"type": "missing",
         "find": "; a tied vote is also a rejection",
         "problem": "It is missing what happens with a tied vote (the team is rejected)."},
        {"type": "ambiguous",
         "find": "Note: The 4th Mission in games of 7 or more players requires at least two Mission Fail cards to be a failed mission.",
         "new": "Note: Some Missions in larger games may require more Mission Fail cards to be a failed mission.",
         "problem": "It is not specified which mission and with how many players two Fail cards are needed."},
        {"type": "inconsistent",
         "find": "Note: The Resistance Operatives must select the Mission Success card; Spies may select either the Mission Success or Mission Fail card.",
         "add": "Resistance Operatives may also play Mission Fail cards if they wish.",
         "problem": "Contradiction: the Resistance must play Success, but then may also play Fail."},
    ],
}

# Real problems of the original rulebooks: they are not injected flaws and were not
# counted as invented problems during the evaluation.
KNOWN_ISSUES_ORIGINAL = {
    "reversi-othello": ["It says 'There are two differences' but lists three.",
                        "Typo: 'cannot not play'."],
    "kingdomino": ["'see back of rules' and 'as indicated to the right' refer to parts of the rulebook that are missing."],
    "splendor": ["Sentences that refer to missing pictures ('this card', 'this noble')."],
    "carcassonne": ["Many examples refer to missing figures ('In our example')."],
    "uno": ["'The game continues until someone has one card and declares Uno' is misleading.",
            "'Shuffle Hand & Custom cards' appear in the scoring but are never described."],
    "monopoly": ["OCR errors: '$5005', 'NOCT', 'himther', 'I 2 hotels', '6 $40s' (should be $20)."],
    "the-game-of-life": ["The FAQ mentions 'Life tiles', which are neither among the components nor in the rules."],
    "werewolf": ["The Moderator is counted among the character cards."],
    "checkers": ["It mixes rules from different variants (American, international, Russian)."],
    "risk": ["References to page numbers of the rulebook."],
}

# Regular expression that matches the text even if spaces and line breaks differ.
def flexiblePattern(text):
    return r"\s+".join(re.escape(word) for word in text.split())

# Apply the flaws of one game to its rulebook.
# Returns the flawed text and, for each flaw, its ground truth (type, problem, original and inserted text, expected fix) used for the evaluation.
def applyFlaws(rules, flaws):
    text = rules
    groundTruth = []
    for number, flaw in enumerate(flaws, 1):
        pattern = re.compile(flexiblePattern(flaw["find"]))
        matches = pattern.findall(text)
        
        # the sentence to change must be unique, otherwise the flaw would be ambiguous
        if len(matches) != 1:
            raise ValueError(f"The text to change must appear exactly once "
                             f"(found {len(matches)} times): {flaw['find'][:60]}...")
        original = " ".join(matches[0].split())

        if flaw["type"] == "missing":
            replacement = ""
            inserted = None
            expected_fix = original
        elif flaw["type"] == "ambiguous":
            replacement = flaw["new"]
            inserted = flaw["new"]
            expected_fix = original
        elif flaw["type"] == "inconsistent":
            replacement = matches[0] + " " + flaw["add"]
            inserted = flaw["add"]
            expected_fix = f"Remove the sentence: '{flaw['add']}'. It contradicts: '{original}'"
        else:
            raise ValueError(f"Unknown flaw type: {flaw['type']}")

        text = pattern.sub(lambda match: replacement, text, count=1)
        groundTruth.append({
            "flaw_id": number,
            "type": flaw["type"],
            "problem": flaw["problem"],
            "inserted_text": inserted,
            "original_text": original,
            "expected_fix": expected_fix,
        })
    
    # clean up the text: empty bullet points and double spaces left by the removals    
    text = re.sub(r"^[ \t]*[•\-][ \t]*\n", "", text, flags=re.M)
    text = re.sub(r"(?<=\S) {2,}(?=\S)", " ", text)
    return text, groundTruth

# Return the games that have flaws, with the flawed rulebook and the ground truth.
def buildFlawedGames(games):
    flawedGames = {}
    for name, data in games.items():
        if name in FLAWS:
            text, groundTruth = applyFlaws(data["rules_text"], FLAWS[name])
            flawedGames[name] = {**data, "rules_text": text, "flaws": groundTruth,
                                  "known_issues_original": KNOWN_ISSUES_ORIGINAL.get(name, [])}
    return flawedGames
