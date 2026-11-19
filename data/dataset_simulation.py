# Game situations for the Simulation task, one per tested game. For each game: "stage" is the situation given to the model; best_move,
# acceptable_move and wrong_moves are the reference moves used to score Move correctness; rule_basis lists the rules the moves depend on.

simulations = {
    "connect-four": {
        "stage": """Red played first and you are Yellow. It is your turn.
Columns are numbered 1 to 7 from left to right, rows 1 to 6 from the bottom.
Row 1 (bottom): column 1 empty, column 2 Yellow, column 3 Red, column 4 Red, column 5 Red, column 6 empty, column 7 empty.
Row 2: column 4 Yellow, every other column empty.
Rows 3 to 6 are empty.""",
        "best_move": "Drop a disc into column 6: it falls to row 1 and blocks Red's horizontal line 3-4-5.",
        "acceptable_move": "None: any other column lets Red win immediately by playing column 6.",
        "wrong_moves": "Any column other than 6; placing a disc directly on a chosen row (ignoring gravity); dropping more than one disc.",
        "rule_basis": "One disc per turn; the disc falls to the lowest empty space; four in a row wins.",
    },
    "checkers": {
        "stage": """You are playing American checkers with the dark pieces. Dark men move toward row 8; only dark squares are used.
Squares are named with a column (a to h) and a row (1 to 8); a1 is a dark square.
Dark men (yours): a1, e1, c3, g3.
Light men (opponent): d4, b6, h6, f8.
No kings on the board. It is your turn.""",
        "best_move": "Capture with c3: jump over the light man on d4 and land on e5; the man on d4 is removed. No further jump is possible.",
        "acceptable_move": "None: the capture is mandatory.",
        "wrong_moves": "Any non-capturing move (e.g. g3-f4, g3-h4, c3-b4): capturing is mandatory and the opponent may remove the piece as a penalty; moving backwards; jumping over own pieces.",
        "rule_basis": "Capturing is mandatory in most official rules; men move and capture forward diagonally.",
    },
    "nine-mens-morris": {
        "stage": """The board uses the standard notation: columns a to g and rows 1 to 7.
Lines that matter: a7-d7-g7 (top side of the outer square), c5-d5-e5 (top side of the inner square), d7-d6-d5 (vertical line).
d7 is connected to a7, g7 and d6.
All men have been placed (phase two). You are White and it is your turn.
White (yours, 6 men): a7, g7, d6, a1, g1, b2.
Black (5 men): c5, d5, e5, b4, f2.
d7 is empty.""",
        "best_move": "Move the man from d6 to d7, forming the mill a7-d7-g7, then remove a Black man that is not in a mill: b4 or f2.",
        "acceptable_move": "Move d6 to d7 and form the mill, but without removing a man or with a vague removal.",
        "wrong_moves": "Removing c5, d5 or e5 (they form a mill and other Black men are available); flying (White has more than three men); jumping over a piece; moving to a non-adjacent point.",
        "rule_basis": "A mill allows removing one opponent man; a man in a mill can be removed only if no other men are available; in phase two men move to adjacent points.",
    },
    "ticket-to-ride": {
        "stage": """Four-player game. At the end of his last turn another player was left with only 2 trains, so this is your final turn.
Your hand: 1 Blue card, 1 Locomotive, 3 Red cards, 2 Yellow cards. You have 12 trains left.
Your only incomplete Destination Ticket connects Kansas City and Chicago (7 points). You have already claimed Saint Louis - Chicago.
Kansas City and Saint Louis are connected by a double route of length 2: the Purple one has been claimed by an opponent, the Blue one is open.
Face-up cards: 2 Blue, 1 Locomotive, 1 Green, 1 White.""",
        "best_move": "Claim the Blue route Kansas City - Saint Louis by playing the Blue card and the Locomotive: +2 points for the route and the ticket is completed (+7 instead of -7).",
        "acceptable_move": "None that completes the ticket; drawing cards or Destination Tickets is legal but leaves the ticket incomplete (-7).",
        "wrong_moves": "Using Red or Yellow cards for the Blue route; drawing cards and then claiming the route in the same turn; claiming more than one route; claiming the Purple route.",
        "rule_basis": "One action per turn; a set of cards of the route's colour, Locomotives are wild; after a player has 0-2 trains, each player gets one final turn; incomplete tickets subtract points.",
    },
    "kingdomino": {
        "stage": """Your kingdom must fit in the 5x5 grid with columns A to E and rows 1 to 5. Your castle is on C3.
Dominoes already placed: Wheat field on D3 and Wheat field on E3 (no crowns); Forest on C2 and Forest on D2 (no crowns).
You must now place the domino you chose (action D1): one half is a Wheat field with 1 crown, the other half is a Lake.
No other square of your kingdom is occupied. Ignore the choice of your next domino.""",
        "best_move": "Place the Wheat-with-crown half next to the existing Wheat field (D4, E4 or E2) and the Lake half on a free adjacent square inside A-E/1-5: the Wheat property becomes 3 squares x 1 crown = 3 points.",
        "acceptable_move": "A legal placement where the crowned Wheat square does not touch the Wheat field (e.g. next to the castle on C4 or B3): 1 point.",
        "wrong_moves": "A placement touching only non-matching landscapes and not the castle; a placement outside the 5x5 grid (e.g. column F); overlapping an occupied square; diagonal connection.",
        "rule_basis": "Connect to the starting tile or to a matching landscape (horizontally or vertically); the kingdom must fit in 5x5; points = squares x crowns per property.",
    },
    "azul": {
        "stage": """Another player already has 4 tiles in one horizontal row of their wall and will very likely complete it this round, so this is probably the last round.
Your pattern lines: line 1 empty, line 2 empty, line 3 holds 2 Blue tiles, line 4 holds 1 Yellow tile, line 5 empty.
Your wall: row 1 already has a Red tile; row 3 has no Blue tile yet.
Factory display A: 1 Blue, 3 Red. Factory display B: 2 Black, 2 Yellow.
Center of the table: 2 Blue, 1 Yellow and the starting player marker (nobody has taken from the center yet).
It is your turn.""",
        "best_move": "Take the 1 Blue tile from Factory display A and complete pattern line 3; the 3 Red tiles go to the center. The Blue tile is moved to the wall and scores this round.",
        "acceptable_move": "Take the 2 Blue tiles from the center: line 3 is completed, but one Blue tile and the starting player marker fall on the floor line (minus points). Or take the Red or Yellow tiles into a legal line without completing it.",
        "wrong_moves": "Putting Red tiles in line 3 (it holds Blue) or in line 1 (wall row 1 already has Red); putting Blue in line 4 (it holds Yellow); taking tiles of two colours.",
        "rule_basis": "Take all tiles of one colour from one display or the center; a pattern line holds one colour; a colour cannot go in a line whose wall row already has it; floor tiles give minus points; the first player to take from the center takes the starting player marker.",
    },
    "uno": {
        "stage": """The top card of the DISCARD pile is a Red 7.
Your hand: Red Draw Two, Blue 7, Yellow 3.
The next player has one card left and has just said "Uno!".
It is your turn.""",
        "best_move": "Play the Red Draw Two: the next player draws 2 cards and loses the turn, so they cannot win now.",
        "acceptable_move": "Play the Blue 7 (legal, but the next player may win with their last card).",
        "wrong_moves": "Playing the Yellow 3 (no colour, number or symbol match); drawing a card while holding a playable card; playing two cards.",
        "rule_basis": "Match colour, number or symbol; Draw Two makes the next player draw 2 and lose the turn.",
    },
    "exploding-kittens": {
        "stage": """You have just drawn an Exploding Kitten at the end of your turn.
Your hand: Defuse, Nope, Skip, Taco Cat.
The next player, Bea, has 2 cards. Two turns ago you saw her use her only Defuse Card.
The Draw Pile has 9 cards.""",
        "best_move": "Play the Defuse and secretly put the Exploding Kitten back on top of the Draw Pile (or very near the top), so that Bea, who probably has no Defuse, is likely to draw it.",
        "acceptable_move": "Play the Defuse and put the Kitten anywhere else in the pile.",
        "wrong_moves": "Playing the Skip or the Nope to avoid exploding (only a Defuse saves you; a Nope cannot stop an Exploding Kitten); not reinserting the Kitten; showing where it is.",
        "rule_basis": "Drawing an Exploding Kitten eliminates you unless you play a Defuse; the Kitten is reinserted anywhere you like in secret; Nope stops any action except an Exploding Kitten or a Defuse.",
    },
    "mao": {
        "stage": """The previous player has just played the 7 of hearts and said "Have a nice day".
Your hand: 7 of spades, Jack of clubs, 3 of hearts, 9 of diamonds.
It is your turn.""",
        "best_move": "Play the 7 of spades, say \"Have a very nice day\" and name the card: \"Seven of spades\". Say nothing else.",
        "acceptable_move": "Play the 7 of spades but forget one of the two required phrases; or draw one card (the penalty for not playing a seven) and end the turn.",
        "wrong_moves": "Playing the 3 of hearts, the Jack or the 9 (after a seven you must play a seven or draw); talking beyond the required phrases.",
        "rule_basis": "After a seven the next player must play a seven (adding one \"very\") or draw one card per seven; a spade must be named; talking is not allowed.",
    },
    "monopoly": {
        "stage": """Classic rules, no Speed Die.
You have just landed on Park Place, which is unowned and costs $350.
You have $300 in cash. You own Boardwalk, Reading Railroad and Mediterranean Avenue, all unmortgaged and without buildings.
Mortgage values: Reading Railroad $100, Mediterranean Avenue $30.""",
        "best_move": "Mortgage Reading Railroad (+$100) and buy Park Place for $350: you complete the dark blue colour group (double rent on Boardwalk and Park Place, and you can build later).",
        "acceptable_move": "Decline and let the property go to auction, bidding in the auction (legal, but another player may complete or block the group).",
        "wrong_moves": "Buying Park Place without having $350; mortgaging only Mediterranean Avenue and buying anyway ($330 is not enough); building houses now; borrowing from the Bank or other players.",
        "rule_basis": "An unowned property can be bought at its price or is auctioned; unimproved properties can be mortgaged at any time; owning a full colour group doubles unimproved rent; players can borrow only by mortgaging.",
    },
    "clue": {
        "stage": """You are Miss Scarlet. Your detective notebook shows:
- Suspects: all crossed off except Mrs. Peacock.
- Weapons: all crossed off except the Rope.
- Rooms: all crossed off except the Lounge and the Library.
You have not made any Accusation yet. You have just entered the Lounge this turn.""",
        "best_move": "Suggest \"Mrs. Peacock, with the Rope, in the Lounge\" (moving her token and the Rope into the Lounge). Only the Lounge card can be shown: if someone shows it, the room is the Library; if nobody can, it is the Lounge. Then make the Accusation on the same turn with the room you have deduced.",
        "acceptable_move": "Accuse immediately choosing one of the two rooms (50% risk with your only Accusation), or make the Suggestion and wait for a later turn to accuse.",
        "wrong_moves": "Suggesting the Library while being in the Lounge; making more than one Accusation; looking at the envelope before accusing.",
        "rule_basis": "A Suggestion must name the room you are in; opponents show one named card if they have it; you may make a Suggestion and an Accusation on the same turn; only one Accusation per game.",
    },
    "forbidden-island": {
        "stage": """You are the Engineer. Your pawn is on the Temple of the Moon (un-flooded), one of the two tiles where the Earth Stone can be captured.
Your hand: 4 Earth Stone cards and 1 Sandbags card.
Adjacent tiles: Fools' Landing to your right (flooded) and the Temple of the Sun below you (flooded; it is the other Earth Stone tile).
Two treasures have already been captured. The water level is 3.
It is your turn and you have 3 actions.""",
        "best_move": "Capture the Earth Stone (1 action, discard the 4 cards), then shore up both Fools' Landing and the Temple of the Sun with one action (the Engineer shores up 2 tiles for 1 action). Use the last action freely (e.g. another shore up).",
        "acceptable_move": "Shore up the adjacent tiles but capture the Earth Stone later, or use the Sandbags without capturing now.",
        "wrong_moves": "Capturing with fewer than 4 cards or from a non-matching tile; giving cards to a player on another tile; taking more than 3 actions; moving diagonally (only the Explorer can).",
        "rule_basis": "Up to 3 actions; capture by discarding 4 matching cards on a corresponding tile; Engineer shores up 2 tiles per action; Special Action cards cost no action.",
    },
    "werewolf": {
        "stage": """The game started with 8 people: Moderator, Seer, Doctor, 2 Werewolves and 3 Villagers. You are the Seer.
Two players have died; their roles were not revealed.
Alive: you, Anna, Bob, Carla and Dan.
Last night you pointed at Anna and the Moderator gave you a thumbs-up.
It is now daytime. Bob has just accused Carla; nobody has supported the accusation yet.""",
        "best_move": "Do not support Bob's accusation; accuse Anna (sharing what you saw, if you wish) and look for a second player to support it, then vote to kill Anna.",
        "acceptable_move": "Stay silent or vote without using your information (legal, but wastes the only certain information about a Werewolf).",
        "wrong_moves": "Showing your character card; claiming the Seer can kill or protect; killing someone without a supported accusation and a majority vote; acting during the day as if it were night.",
        "rule_basis": "The Seer learns if a player is a Werewolf; an accusation must be supported by a second player; the accused defends, then a majority vote kills; Werewolves win when they equal the Villagers.",
    },
    "dixit": {
        "stage": """Five players. You are not the storyteller.
The storyteller said: "Shelter from the storm".
The displayed cards are:
1: a small hut with a lit window in a snowstorm
2: an umbrella sheltering a child in heavy rain (this is the card you gave)
3: a desert at noon
4: a birthday cake
5: a lion sleeping in the sun
You have voting tokens 1 to 5. It is time to vote.""",
        "best_move": "Vote for card 1: place voting token 1 face down in front of you. Card 2 is your own and cannot be voted for.",
        "acceptable_move": "Vote for card 3, 4 or 5 (legal but unlikely to be the storyteller's card).",
        "wrong_moves": "Voting for card 2 (your own card); voting for more than one card; revealing your vote before everyone has voted.",
        "rule_basis": "Each player secretly votes for the card they believe is the storyteller's; you are not allowed to vote for your own image.",
    },
    "the_resistance": {
        "stage": """Five players: you, Bob, Carla, Dan and Eve. You are a Resistance Operative.
Mission 1 (team: you and Bob) succeeded.
Mission 2 (team: Carla, Dan and Eve) failed with one Mission Fail card.
The score is Resistance 1 - Spies 1. You are now the Leader for Mission 3.""",
        "best_move": "Propose a team of 2 (the size of the 3rd mission with 5 players): yourself and Bob, giving a Team card to each, then call the vote.",
        "acceptable_move": "A team of 2 that includes one player from the failed mission.",
        "wrong_moves": "A team of 3 or more players; skipping the team vote; revealing your Character card.",
        "rule_basis": "The Leader assigns the number of Team cards given by the table (5 players, 3rd mission: 2); the Leader may include himself; all players vote on the team.",
    },
}
