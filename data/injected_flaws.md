# Injected flaws (Flaw Detection task)

Three flaws per game, one of each type. They are the ground truth used to score Flaw Detection.

## abstract_deterministic

### tic-tac-toe
- **Missing**: It is not stated who goes first.
  - Removed sentence: "The player who is playing "X" always goes first."
- **Ambiguous**: The draw condition is vague (when is the grid 'crowded'? who decides?).
  - "If all squares are filled and neither player has made a complete row of Xs or Os, then the game is a draw." becomes "If the board gets crowded and nobody seems able to win, the game may be considered over."
- **Inconsistent**: Contradiction: first three marks in a row win, then four are needed (impossible on a 3x3 grid).
  - Added sentence: "A player needs four marks in a row to win." (contradicts: "then that player wins.")

### connect-four
- **Missing**: The 'gravity' rule is missing: it is not said where the disc stops in the column.
  - Removed sentence: "Each disc will fall to the lowest unoccupied space within the selected column."
- **Ambiguous**: It is unclear what happens if the grid fills up with no winner (it should be a draw).
  - "If all slots are filled before either player achieves this, the game ends in a draw." becomes "If the board fills up, the outcome is decided in some other way."
- **Inconsistent**: Contradiction: one disc is played at a time, but then two discs per turn.
  - Added sentence: "On each turn a player drops two discs." (contradicts: "into their chosen column from the top of the grid.")

### checkers
- **Missing**: The condition for becoming a king is missing, even though kings are mentioned later.
  - Removed sentence: "When a man reaches the farthest row forward, known as the kings row or crown head, it becomes a king."
- **Ambiguous**: It is not specified which squares are used (only the dark ones).
  - "Only the dark squares of the checkerboard are used." becomes "Some of the squares of the checkerboard are used."
- **Inconsistent**: Contradiction about who moves first (dark vs light).
  - Added sentence: "The player with the light pieces always makes the first move." (contradicts: "The player with the darker color moves first, then players alternate turns.")
- *Issues already in the original rulebook:* It mixes rules from different variants (American, international, Russian).

### nine-mens-morris
- **Missing**: The protection of pieces that are part of a mill is missing.
  - Removed sentence: "A piece in an opponent's mill, however, can be removed only if no other pieces are available."
- **Ambiguous**: The number of pieces per player is not specified.
  - "Each player has nine pieces, or men, usually coloured black and white." becomes "Each player has several pieces, or men, usually coloured black and white."
- **Inconsistent**: Contradiction: in phase two pieces cannot jump, but then they can.
  - Added sentence: "During phase two, a man may jump over an adjacent piece to reach a vacant point." (contradicts: "A piece may not "jump" another piece.")

### reversi-othello
- **Missing**: The rule that flanked opponent pieces are flipped is missing (core mechanic).
  - Removed sentence: "All of the opponent's pieces between these two pieces are 'captured' and turned over to match the player's colour."
- **Ambiguous**: It is unclear for how many moves and on which squares players must play at the start.
  - "For the first four moves, the players must play to one of the four squares in the middle of the board" becomes "For the first few moves, the players must play near the middle of the board"
- **Inconsistent**: Contradiction about the winning condition (more pieces vs fewer pieces).
  - Added sentence: "The player with the fewest pieces of their colour on the board at the end wins." (contradicts: "A player's objective is to have more of their allocated colour face upwards at the end of the game.")
- *Issues already in the original rulebook:* It says 'There are two differences' but lists three. Typo: 'cannot not play'.

## low-interaction-procedural-games

### ticket-to-ride
- **Missing**: The rule that taking a face-up Locomotive counts as two cards is missing.
  - Removed sentence: "If a Locomotive card is one of the five face-up cards, the player who draws it may only draw one card, instead of two."
- **Ambiguous**: The end-of-game condition has no precise threshold (0, 1 or 2 trains).
  - "When one player’s stock of colored plastic trains gets down to only 0,1 or 2 trains left" becomes "When one player’s stock of colored plastic trains gets low"
- **Inconsistent**: Contradiction: at most one route per turn, but also up to two.
  - Added sentence: "On his turn a player may claim up to two routes." (contradicts: "A player may claim any open route on the board.")

### carcassonne
- **Missing**: The majority rule when several meeples share a feature is missing.
  - Removed sentence: "If there are multiple meeples in a single scored feature, the player with the most meeples is awarded full points and all other players receive nothing."
- **Ambiguous**: The number of starting meeples per player is not specified (7).
  - "Start by distributing 7 meeples of the color of their choice to each player" becomes "Start by distributing a handful of meeples of the color of their choice to each player"
- **Inconsistent**: Contradiction: a meeple cannot be placed in an occupied feature, but then it always can.
  - Added sentence: "You may always place your meeple on a road or city even if another player's meeple already occupies it." (contradicts: "You may not place a meeple in a feature where there already is at least one other meeple.")
- *Issues already in the original rulebook:* Many examples refer to missing figures ('In our example').

### splendor
- **Missing**: The limit of three reserved cards in hand is missing.
  - Removed sentence: "Players may not have more than three reserved cards in hand, and the only way to get rid of a card is to buy it (see below)."
- **Ambiguous**: The token limit has no precise number (10).
  - "A player can never have more than 10 tokens at the end of their turn (including jokers). If this happens, they must return tokens until they only have 10 left." becomes "A player should not hold too many tokens at the end of their turn; if they do, they must return some."
- **Inconsistent**: Contradiction in the tie-break (fewest cards vs most cards).
  - Added sentence: "In case of a tie, the player with the most development cards wins." (contradicts: "In case of a tie, the player who has purchased the fewest development cards wins.")
- *Issues already in the original rulebook:* Sentences that refer to missing pictures ('this card', 'this noble').

### kingdomino
- **Missing**: The rule for connecting dominoes is missing (at least one side with the same landscape).
  - Removed sentence: "- Or connect it to another domino matching at least 1 of its landscape (horizontally or vertically only)."
- **Ambiguous**: The scoring calculation is not specified (squares x crowns).
  - "Each property will give you as much prestige points as the NUMBER OF SQUARES multiplied with the NUMBER OF SPECIFIC CROWNS (see back of rules) appearing on the property." becomes "Each property will give you prestige points based on its size and the crowns appearing on it."
- **Inconsistent**: Contradiction: the kingdom must fit in a 5x5 grid, but then it has no size limit.
  - Added sentence: "There is no limit to the size of your kingdom." (contradicts: "All your dominoes must fit in 5x5 grid.")
- *Issues already in the original rulebook:* 'see back of rules' and 'as indicated to the right' refer to parts of the rulebook that are missing.

### azul
- **Missing**: The rule that a pattern line holds a single colour is missing.
  - Removed sentence: "If the pattern line already holds tiles, you may only add tiles of the same color to it."
- **Ambiguous**: The number of Factory displays by player count is not specified (5/7/9).
  - "In a 2-player game, place 5 Factory displays. • In a 3-player game, place 7 Factory displays. • In a 4-player game, place 9 Factory displays." becomes "Place a number of Factory displays that depends on the number of players."
- **Inconsistent**: Contradiction about the bonus for complete columns (7 points vs no bonus).
  - Added sentence: "Vertical lines give no bonus at the end of the game." (contradicts: "Gain 7 points for each complete vertical line of 5 consecutive tiles on your wall.")

## exception-heavy rule systems

### crazy-eights
- **Missing**: The rule about which cards can be played (same number or suit) is missing.
  - Removed sentence: "Players may do so if the card they want to get rid of is the same number or suit of the card flipped up."
- **Ambiguous**: It is unclear how many cards are drawn when a player cannot play (until able, max 5).
  - "they must draw cards from the pile until they can do so or until they’ve drawn a maximum of five cards." becomes "they must draw some cards from the pile."
- **Inconsistent**: Contradiction about the value of aces (1 vs 11 points).
  - Added sentence: "- Aces are worth 11 points" (contradicts: "- Aces are worth 1 point")

### uno
- **Missing**: The penalty for not saying 'Uno!' is missing.
  - Removed sentence: "If a player forgets to say "Uno!" when they have one card left and is caught, that player must draw two cards."
- **Ambiguous**: The number of starting cards is not specified (7).
  - "The dealer shuffles and deals 7 cards to each player." becomes "The dealer shuffles and deals several cards to each player."
- **Inconsistent**: Contradiction about the effect of the Skip card (skip a turn vs play twice).
  - Added sentence: "When a Skip is played, the next player takes two turns in a row." (contradicts: "Skip - The next player is skipped.")
- *Issues already in the original rulebook:* 'The game continues until someone has one card and declares Uno' is misleading. 'Shuffle Hand & Custom cards' appear in the scoring but are never described.

### fluxx
- **Missing**: It is missing what to do when a New Rule contradicts a rule already in play.
  - Removed sentence: "If it contradicts a New Rule already in play, discard the old rule."
- **Ambiguous**: The number of starting cards is not specified (3).
  - "Shuffle the deck and deal three cards to each player." becomes "Shuffle the deck and deal a few cards to each player."
- **Inconsistent**: Contradiction: a player wins at once even on another player's turn, but then only at the end of their own turn.
  - Added sentence: "A player can only win at the end of their own turn." (contradicts: "That player wins instantly, no matter whose turn it is!")

### exploding-kittens
- **Missing**: The Favor card is listed but its effect is not described.
  - Removed sentence: "Force any other player to give you 1 card from their hand. They choose which card to give you."
- **Ambiguous**: See the Future does not specify how many cards are seen (3).
  - "Peek at the top 3 cards from the Draw Pile" becomes "Peek at some of the top cards from the Draw Pile"
- **Inconsistent**: Contradiction about the number of starting cards (4 + Defuse = 5 vs 7).
  - Added sentence: "Each player receives 7 cards." (contradicts: "2- Shuffle the remaining deck and deal 4 cards face down to each player.")

### mao
- **Missing**: It is missing what a player does when they cannot play a card.
  - Removed sentence: "If the player is unable to do so, they must draw one card and knock on the table."
- **Ambiguous**: The penalty for breaking a rule is not specified (one card from the deck).
  - "Whenever a rule is broken, the player is penalized by being given one card from the draw pile." becomes "Whenever a rule is broken, the player may be penalized somehow."
- **Inconsistent**: Contradiction about who plays first (player left of the dealer vs dealer).
  - Added sentence: "The dealer always plays the first card." (contradicts: "game play will begin with the player to the left of the dealer and continue clockwise from there.")

## thematic games with randomness

### monopoly
- **Missing**: The starting money of each player is missing ($1,500).
  - Removed sentence: "Each player is given $1,500 divided as follows: 2 each of $500s, $100s and $50s; 6 $40s; 5 each of $10s, $ 5s and $1s."
- **Ambiguous**: The Income Tax does not specify the fixed amount or the percentage.
  - "estimate your tax at $900 and pay the Bank, or you may pay 10"%" of your total worth to the Bank." becomes "pay either a fixed amount or a percentage of your total worth to the Bank."
- **Inconsistent**: Contradiction: several tokens can share a space, but then only one.
  - Added sentence: "Only one token may occupy a space at any time." (contradicts: "Two or more tokens may rest on the same space at the same time.")
- *Issues already in the original rulebook:* OCR errors: '$5005', 'NOCT', 'himther', 'I 2 hotels', '6 $40s' (should be $20).

### risk
- **Missing**: The rule that ties in the dice go to the defender is missing.
  - Removed sentence: "In case of a tie, the defender always wins."
- **Ambiguous**: The final move does not specify how many territories and to where (one, adjacent).
  - "move as many armies as you’ d like from one (and only one) of your territories into one (and only one) of your adjacent territories." becomes "move some armies between your territories."
- **Inconsistent**: Contradiction about the maximum number of armies lost per roll (2 vs 3).
  - Added sentence: "The attacker may lose up to 3 armies on a single roll." (contradicts: "The attacker can never lose more than 2 armies on a single roll.")
- *Issues already in the original rulebook:* References to page numbers of the rulebook.

### clue
- **Missing**: The limit of one accusation per game is missing.
  - Removed sentence: "Remember: You may make only one Accusation during a game."
- **Ambiguous**: It is not specified how many squares a player moves.
  - "Roll the die and move your token the number of squares you rolled." becomes "Roll the die and move your token."
- **Inconsistent**: Contradiction about who starts (Miss Scarlet vs Colonel Mustard).
  - Added sentence: "Colonel Mustard always plays first." (contradicts: "the player with the red token— always plays first.")

### forbidden-island
- **Missing**: It is missing what happens when the card of an already flooded tile is drawn (it sinks).
  - Removed sentence: "If the matching Island tile is already flooded, it sinks into the abyss! Remove it and the matching Flood card from the game and place them out of play."
- **Ambiguous**: The hand limit has no precise number (5).
  - "You may only have 5 cards in your hand, including Treasure and Special Action cards. If you ever find that you have 6 or more cards" becomes "You may only have a limited number of cards in your hand, including Treasure and Special Action cards. If you ever find that you have too many cards"
- **Inconsistent**: Contradiction: a treasure can be captured on a flooded tile, but then never.
  - Added sentence: "• You may never capture a treasure while standing on a flooded tile." (contradicts: "• You may capture a treasure on a flooded tile.")

### the-game-of-life
- **Missing**: It is missing how players move during their turn.
  - Removed sentence: "Spin the spinner and move your car the number of spaces shown."
- **Ambiguous**: The retirement bonuses have no amounts.
  - "Collect retirement bonuses: 1st: $400K 2nd: $300K 3rd: $200K 4th: $100K" becomes "Collect a retirement bonus that depends on your arrival order."
- **Inconsistent**: Contradiction about the final value of Pet cards ($100K vs nothing).
  - Added sentence: "Pet cards are worth nothing at the end of the game." (contradicts: "Collect $100K per Pet card.")
- *Issues already in the original rulebook:* The FAQ mentions 'Life tiles', which are neither among the components nor in the rules.

## social/party games

### mafia
- **Missing**: It is missing how a suspect is eliminated in the Day phase (majority vote).
  - Removed sentence: "If the majority of the players (not counting the accused) votes for “Guilty as member of the Mafia,” the suspected player is “sentenced to death” and s/he is out of the game until the end of the round."
- **Ambiguous**: The number of black cards (Mafia) by player count is not specified.
  - "6-7 players: 2 black cards + others red / 8-10 players: 3 black cards + others red / 11-13 players: 4 black cards + others red / 14-16 players: 5 black cards + others red" becomes "a few black cards (more with larger groups) + others red"
- **Inconsistent**: Contradiction: the Honest are the majority, but then the Mafia always outnumber them.
  - Added sentence: "The Mafia always outnumber the Honest players." (contradicts: "Honest players have to suspect everybody, but they have an advantage of being the majority.")

### werewolf
- **Missing**: The effect of the Doctor's healing is missing.
  - Removed sentence: "The person chosen, which could be themself, will survive if the Werewolves chose the same player to kill."
- **Ambiguous**: The minimum number of players is not specified (7).
  - "You need at least 7 people to play." becomes "You need a good number of people to play."
- **Inconsistent**: Contradiction about the Werewolves' winning condition (equal numbers vs everyone dead).
  - Added sentence: "The Werewolves only win when every Villager has been killed." (contradicts: "The Werewolves win if the number of Werewolves equal the number of Villagers left.")
- *Issues already in the original rulebook:* The Moderator is counted among the character cards.

### dixit
- **Missing**: The rule against voting for your own card is missing.
  - Removed sentence: "Note: You’re not allowed to vote for your own image."
- **Ambiguous**: The score in the normal case is not specified (3 points).
  - "In any other case, the storyteller scores 3 points and so do the players who found his image." becomes "In any other case, the storyteller and the players who found his image score some points."
- **Inconsistent**: Two conflicting end-of-game conditions (deck exhausted vs 30 points).
  - Added sentence: "The game ends as soon as a player reaches 30 points on the scoring track." (contradicts: "The game ends when the last card from the pack has been drawn.")

### codenames
- **Missing**: It is missing how many words each team must guess (9 and 8).
  - Removed sentence: "The starting team has 9 words to guess. The other team has 8."
- **Ambiguous**: It is unclear that the clue must come with a number of related words.
  - "You also say one number, which tells your teammates how many codenames are related to your clue." becomes "You may also give some indication of how far your clue reaches."
- **Inconsistent**: Contradiction: touching an innocent bystander ends the turn, but then it does not.
  - Added sentence: "Touching an innocent bystander does not end your turn." (contradicts: "The field operatives must always make at least one guess.")

### the_resistance
- **Missing**: It is missing what happens with a tied vote (the team is rejected).
  - Removed sentence: "; a tied vote is also a rejection"
- **Ambiguous**: It is not specified which mission and with how many players two Fail cards are needed.
  - "Note: The 4th Mission in games of 7 or more players requires at least two Mission Fail cards to be a failed mission." becomes "Note: Some Missions in larger games may require more Mission Fail cards to be a failed mission."
- **Inconsistent**: Contradiction: the Resistance must play Success, but then may also play Fail.
  - Added sentence: "Resistance Operatives may also play Mission Fail cards if they wish." (contradicts: "Note: The Resistance Operatives must select the Mission Success card; Spies may select either the Mission Success or Mission Fail card.")
