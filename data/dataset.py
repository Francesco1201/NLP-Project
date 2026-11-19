# Base dataset: the 25 rulebooks, 5 per game category. Each entry has the name of the game, its category and the text of the rulebook
# (copied from PDF rulebooks and web pages).

games = {
    "tic-tac-toe": {
        "name": "Tic tac toe",
        "category": "abstract_deterministic",
        "rules_text": """
         Tic tac toe is a two player game where the goal is to be the first player to get three in a row on a 3-by-3 grid. 
         To start, one player draws a board, creating a 3-by-3 grid of squares.
         The player who is playing "X" always goes first.
         Players alternate placing Xs and Os on the board until either player has three in a row, horizontally, vertically,
         or diagonally or until all squares on the grid are filled. If a player is able to draw three Xs or three Os in a row, then that player wins.
         If all squares are filled and neither player has made a complete row of Xs or Os, then the game is a draw. 
        """,
    },
    "connect-four": {
        "name": "Connect four",
        "category": "abstract_deterministic",
        "rules_text": """
          Connect 4 is a two player game played on a vertically oriented grid consisting of 7 columns and 6 rows.
          Each player selects a color and alternates turns, dropping colored discs from the top into any of the columns.
          The main aim of the game is to form a line of four discs of one’s own color, either horizontally, vertically, or diagonally.
          The first player to achieve this wins the game. This simple setup allows for easy understanding
          yet leads to a rich layer of strategic depth as players vie to outmaneuver each other and block potential winning moves.
          Players determine who will go first, typically through a coin toss or a similar method of choice.
          Players take turns, each dropping one disc at a time into their chosen column from the top of the grid.
          Each disc will fall to the lowest unoccupied space within the selected column.
          The game concludes when a player successfully forms a straight line of four of their discs, either horizontally, vertically, or diagonally.
          If all slots are filled before either player achieves this, the game ends in a draw.
        """,
    },
    "checkers": {
        "name": "Checkers",
        "category": "abstract_deterministic",
        "rules_text": """
        Checkers is a group of strategy board games for two players which involve forward movements of uniform game pieces and mandatory captures by jumping over opponent pieces.
        The term "checkers" derives from the checkered board which the game is played on, whereas "draughts" derives from the verb "to draw" or "to move".
        The most popular forms of checkers in Anglophone countries are American checkers (also called English draughts), which is played on an 8x8 checkerboard;
        Russian draughts, Turkish draughts and Armenian draughts, all of them on an 8x8 board; and international draughts, played on a 10x10 board - with the latter widely played in many countries worldwide.
        There are many other variants played on 8x8 boards. Canadian checkers and Malaysian/Singaporean checkers (also locally known as dam) are played on a 12x12 board. 
        Checkers is played by two opponents on opposite sides of the gameboard.
        One player has dark pieces (usually black); the other has light pieces (usually white or red).
        The player with the darker color moves first, then players alternate turns.
        A player cannot move the opponent's pieces. A move consists of moving a piece to an adjacent unoccupied square.
        All pieces move forward only at the beginning of the game. At the beginning of a player's turn, if the adjacent square of a player's piece
        (in the player's forward direction) contains an opponent's piece, and the square immediately beyond it is vacant,
        the piece may be captured (must be captured in most international rules) by jumping over it. 
        The captured piece is then removed from the board.
        Only the dark squares of the checkerboard are used. A piece can only move into an unoccupied square.
        When capturing an opponent's piece is possible, capturing is mandatory in most official rules. If the player does not capture,
        the other player can remove the opponent's piece as a penalty (or muffin), and where there are two or more such positions the player forfeits pieces
        that cannot be moved (although some rule variations make capturing optional). In almost all variants, a player with no valid move remaining loses.
        This occurs if the player has no pieces left, or if all the player's pieces are obstructed from moving by opponent pieces.
        An uncrowned piece (man) moves one step ahead and captures an adjacent opponent's piece by jumping over it and landing on the next square.
        Multiple enemy pieces can be captured in a single turn provided this is done by successive jumps made by a single piece; the jumps do not need to be on the same diagonal direction
        and may "zigzag" (change direction). In American checkers and Spanish draughts, men can jump only forwards;
        in international draughts and Russian draughts, men can jump both forwards and backwards.
        When a man reaches the farthest row forward, known as the kings row or crown head, it becomes a king.
        It is marked by placing an additional piece on top of, or crowning, the first man. The king has additional powers,
        namely the ability to move any amount of squares at a time (in international checkers), move backwards and, in variants where men cannot already do so, capture backwards.
        Like a man, a king can make successive jumps in a single turn, provided that each jump captures an enemy piece.
        In international draughts, kings can move any number of squares, forward or backward.
        Kings with such an ability are also informally called flying kings. They may capture an opposing man, regardless of distance, by jumping to any
        of the unoccupied squares immediately past the man. Because jumped pieces remain on the board until the turn is completed, it is possible to reach
        a position in a multi-jump move where the flying king is blocked from capturing further by a piece already jumped.
        Flying kings are not used in American checkers; a king's only advantage over a man is the additional ability to move and capture backwards. 
        """,
    },
    "nine-mens-morris": {
        "name": "Nine men's morris",
        "category": "abstract_deterministic",
        "rules_text": """
        Nine men's morris is a strategy board game for two players, dating back to at least the Roman Empire.
        The game is also known as nine-man morris, mill, mills, the mill game, merels, merrills, merelles, marelles, morelles,
        and ninepenny marl in English. In North America, the game has also been called cowboy checkers, and its board is sometimes printed on the back of checkerboards.
        Nine men's morris is a solved game, that is, a game whose optimal strategy has been calculated. It has been shown that with perfect play from both players, the game results in a draw.
        The classical Latin term mareculus is the diminutive of 'man', the eclisiastical Latin word merellus means 'gamepiece', which may have been corrupted in English to 'morris',
        while miles is Latin for soldier. Three main alternative variations of the game are three, six, and twelve men's morris.
        The board consists of a grid with twenty-four intersections, or points. Each player has nine pieces, or men, usually coloured black and white. Players try to form 'mills'—three of their own men lined horizontally
        or vertically—allowing a player to remove an opponent's man from the game. A player wins by reducing the opponent to two men (whereupon they can no longer form mills and thus are unable to win) or by leaving them without a legal move.
        The game proceeds in three phases:
         1- Placing men on vacant points
         2- Moving men to adjacent points
         3- (optional phase) Moving men to any vacant point when the player has been reduced to three men.
        The game begins with an empty board. The players determine who plays first and then take turns. During the first phase, a player's turn consists of placing a man from the player's hand onto an empty point.
        If a player is able to place three pieces on contiguous points in a straight line, vertically or horizontally, they have formed a mill, which allows them to remove one of the opponent's pieces from the board.
        A piece in an opponent's mill, however, can be removed only if no other pieces are available. After all men have been placed, phase two begins. 
        Players continue to alternate moves, this time moving a man to an adjacent point each turn. A piece may not "jump" another piece.
        Players continue to try to form mills and remove the opponent's pieces as in phase one. If all of a player's pieces get blocked in (where they are unable to move to an adjacent, empty space) that player loses.
        A player can "break" a mill by moving a piece out of an existing mill, then moving it back to form the same mill a second time (or any number of times), each time removing one of the opponent's men.
        The act of removing an opponent's man is sometimes called "pounding" the opponent.
        When one player has been reduced to three men, phase three begins. 
        When a player is reduced to three pieces, there is no longer a limitation on that player of moving to only adjacent points: The player's men may "fly" (or "hop", or "jump") from any point to any vacant point.
        Some rules sources say this is the way the game is played, some treat it as a variation, and some do not mention it at all. A 19th-century games manual calls this the "truly rustic mode of playing the game".
        Flying was introduced to compensate when the weaker side is one man away from losing the game.
        At the beginning of the game, it is more important to place pieces in versatile locations rather than to try to form mills immediately and make the mistake of concentrating one's pieces in one area of the board.
        An ideal position, which typically results in a win, allows a player to shuttle one piece back and forth between two mills, removing a piece every turn. 
        """,
    },
    "reversi-othello": {
        "name": "Reversi/Othello",
        "category": "abstract_deterministic",
        "rules_text": """
        Reversi is an abstract strategy board game invented during the Victorian era.
        It has remained popular for more than a century being given a boost in the 1970s when a version of it was re-marketed under the name 'Othello'
        and another in the 1990s when a computer version of it was included with the Microsoft Windows operating system.
        Reversi involves play by two parties on an eight-by-eight square grid with pieces that have two distinct sides.
        Pieces typically appear coin-like, with a light and a dark face, each side representing one player. 
        The goal for each player is to make pieces of their colour constitute a majority of the pieces on the board at the end of the game, by turning over as many of their opponent's pieces as possible.
        Reversi is played upon an 8 x 8 squared board without chequers.
        Accompanying the board, there should be 64 pieces - originally each was red on one side and green on the other but of course any 2 colours can be used and more recently they tend to be dark and light.
        The board starts empty. Each player is allocated one of the colours by mutual agreement and they take turns to play a piece until all the squares are occupied. 
        A player's objective is to have more of their allocated colour face upwards at the end of the game.
        Player's toss a coin to decide who will play first. Each turn, the player places one piece on the board with their colour facing up.
        For the first four moves, the players must play to one of the four squares in the middle of the board and no pieces are captured or reversed.
        Each piece played must be laid adjacent to an opponent's piece so that the opponent's piece or a row of opponent's pieces is flanked by the new piece and another piece of the player's colour.
        All of the opponent's pieces between these two pieces are 'captured' and turned over to match the player's colour.
        It can happen that a piece is played so that pieces or rows of pieces in more than one direction are trapped between the new piece played and other pieces of the same colour.
        In this case, all the pieces in all viable directions are turned over.
        The game is over when neither player has a legal move (i.e. a move that captures at least one opposing piece) or when the board is full.
        There are two differences between Othello and Reversi.
         1- In Othello, the two colours are Black and White and Black always plays first
         2- In Othello, the four squares in the middle of the board start with four counters already placed - white top left and bottom right; black top right and bottom left.
            The reason for this is that In Reversi, the extra freedom can result in an opening that produces a less interesting game.
         3- In Reversi if one player cannot not play a piece, the game finishes. In Othello, a player without a move simply passes, and the other player keeps playing pieces until the first player can make a move again.
        """,
    },
    "ticket-to-ride": {
        "name": "Ticket to ride",
        "category": "low-interaction-procedural-games",
        "rules_text": """
        Ticket to Ride is a cross-country train adventure. Players compete to connect different cities by laying claim to railway routes on a map of North America.
        Components: 
        - 1 Board map of North American train routes;
        - 240 Colored Train Cars (45 each in Blue, Red, Green, Yellow and Black, plus some extra replacement cars in each color);
        - 144 Illustrated cards: 110 Train Car cards (12 each of Box, Passenger, Tanker, Reefer, Freight, Hopper, Coal, and Caboose cars, plus 14 Locomotives), 30 Destination Ticket cards, 1 Summary card, 1 Longest Continuous Path Bonus card,
        1 Promotional card for additional maps, 1 Days of Wonder Promotional card;
        - 5 Wooden Scoring Markers (1 for each player in Blue, Red, Green, Yellow and Black);
        - 1 Rules booklet;
        - 1 Days of Wonder Online access number
        
        Setting up the Game:
        Place the board map in the center of the table. Each player takes a set of 45 Colored
        Train Cars along with its matching Scoring Marker. Each player places his Scoring
        Marker on Start on the Scoring Track running along the map’s border. Throughout
        the game, each time a player scores points, he will advance his marker accordingly.
        Shuffle the Train Car cards and deal a starting hand of 4 cards to each player.
        Place the remaining deck of Train Car cards near the board and turn the top five cards from the deck face-up.
        Place the Longest Path Bonus card face up next to the board.
        Shuffle the Destination Ticket cards and deal 3 cards to each player. Each player
        looks at their Destination Tickets and decides which ones they wish to keep. A player
        must keep at least two, but may keep all three if he chooses. Any returned cards are
        placed on the bottom of the Destination Ticket deck. This deck is then placed next to the
        board. Players keep their Destination Tickets secret until the end of the game. You are now ready to begin.
        
        Object of the Game:
        The object of the game is to score the highest number of total points. Points can be
        scored by:
        - Claiming a Route between two adjacent cities on the map;
        - Successfully completing a Continuous Path of routes between two cities listed on your Destination Ticket(s);
        - Completing the Longest Continuous Path of routes.
        Points are lost if you do not successfully complete the route given on the Destination Ticket(s) you kept.
        
        The Game Turn:
        The player who is the most experienced traveler goes first. Play then proceeds clockwise around the table, each player taking one turn at a time until
        the game ends. On his turn, a player must perform one (and only one) of the following three actions:
        - Draw Train Car Cards: The player may draw 2 Train Car cards. He may take any one of the face-up cards or he may draw the top card from the
        deck (this is a blind draw). If he draws a face up card, he immediately turns a replacement card face-up from the deck. He then draws his second
        card, either from the face up cards or from the top of the deck. (See Train Car Cards for special rules for Locomotive cards).
        - Claim a Route: The player may claim a route on the board by playing a set of Train Car cards that match the color and length of the route and
        then placing one of his colored trains on each space of this route. He then records his score by moving his Scoring Marker the appropriate numberù
        of spaces (see Route Scoring Table) along the Scoring Track on the board.
        - Draw Destination Tickets: The player draws 3 Destination Tickets from the top of the deck. He must keep at least one of them, but he may keep
        two or all three if he chooses. Any returned cards are placed on the bottom of the deck.
        
        Train Car Cards:
        There are 8 types of regular Train Car cards, plus Locomotive cars. The colors of each type of Train Car card match various routes
        between cities on the board: Purple, Blue, Orange, White, Green, Yellow, Black, and
        Red. Locomotives are Multi-colored and act as a wild card that can be part of any set of
        cards when claiming a route. If a Locomotive card is one of the five face-up cards, the
        player who draws it may only draw one card, instead of two. If, after having drawn one
        card the replacement card is a Locomotive, the player cannot take it. If at any time, three
        of the five face-up cards are Locomotives, all five cards are immediately discarded and
        five new ones are turned face-up to replace them.
        Note: If a player is lucky enough to get a Locomotive from the top of the deck in a blind
        draw, it stills counts as a single card and he may still draw a total of two cards that turn.
        A player may have any number of cards in his hand at any time.
        When the deck is exhausted, the discards are reshuffled into a new draw pile deck. The
        cards should be shuffled thoroughly, since all the cards have been discarded in sets.
        In the unlikely event that there are no cards left in the deck and there are no discards
        (because players are hoarding many cards in their hands), a player cannot draw Train
        Car cards. Instead he may only claim a route or draw Destination Ticket cards.
        
        Claiming Routes:
        To claim a route, a player must play a set of cards equal to the number of spaces in the
        route. A set of cards must be of the same type. Most routes require a specific type of set.
        For example a Blue route must be claimed using blue-colored Passenger Car cards. Some
        routes - those that are Gray colored - can be claimed using a set of cards of any one color.
        When a route is claimed, the player places one of his plastic trains in each of the spaces
        of the route. All the cards in the set used to claim the route are then discarded.
        
        A player may claim any open route on the board. He is never required to
        connect to any of his previously played routes. A player may only claim
        a maximum of one route, hence connect two adjacent cities, never more,
        on his turn.
        Some cities are connected by Double-Routes. One player cannot claim
        both routes to the same cities.
        Important Note: In 2 or 3 player games, only one of the Double-Routes
        can be used. A player can claim either of the two routes between cities, but
        the other route is then closed to other players.
        
        Route Scoring Table:
        When a player claims a route, he records the points he receives by
        moving his Scoring Marker on the Scoring Track: 
        - route length = 1, points scored = 1;
        - route length = 2, points scored = 2;
        - route length = 3, points scored = 4;
        - route length = 4, points scored = 7;
        - route length = 5, points scored = 10;
        - route length = 6, points scored = 15;
        
        Drawing Destination Ticket Cards:
        A player can use his turn to draw more Destination Ticket cards. To do so, he draws 3 new cards from the top of the Destination Ticket Deck. He must
        keep at least one of the cards, but may also keep two or all three if he chooses. If there are less than 3 Destination Tickets left in the deck, the player
        only draws the cards that are available. Any returned cards are placed on the bottom of the Destination Ticket Deck.
        Each Destination Ticket includes the name of two cities on the map and a Point Value. If a player successfully completes a series of routes that connect
        the two cities, they will add the amount of points indicated on the Destination Ticket to their point totals at the end of the game. If they do not
        successfully connect the two cities, they deduct the amount of points indicated.
        Destination Tickets are kept secret from other players until the game's final scoring. A player may have any number of Destination Ticket cards during
        the game.
        
        Game End:
        When one player’s stock of colored plastic trains gets down to only 0,1 or 2 trains left at the end of his turn, each player, including that player, gets
        one final turn. The game then ends and players calculate their final scores.
        
        Calculating Scores:
        Players should have already accounted for the points earned as they completed different routes. To make sure no mistakes were made, you may
        want to re-count the points for each player’s routes.
        Players should then reveal all their Destination Tickets and add (or subtract) the value of their Destination Tickets still in hand, based on whether
        they successfully (or not) connected those cities together.
        The player who has the Longest Continuous Path of routes receives this special bonus card and adds 10 points to his score. When evaluating and
        comparing path lengths, only take into account continuous lines of plastic trains of the same color. A continuous path may include loops, and pass
        through the same city several times, but a given plastic train may never be used twice in the same continuous path. In the case of a tie for the longest
        path, all tied players score the 10 point bonus.
        The player with the most points wins the game. If two or more players are tied for the most points, the player who has completed the most Destination
        Tickets wins. In the unlikely event that they are still tied, the player with the Longest Continuous Path card wins.
        """,
    },
    "carcassonne": {
        "name": "Carcassonne",
        "category": "low-interaction-procedural-games",
        "rules_text": """
        Carcassonne a clever tile-laying game by Klaus-Jürgen Wrede for 2 to 5 players aged 7 and up.
        Carcassonne, the world-famous French city, known for its imposing fortifications erected during the Antiquity
        and the Middle Ages. This fortress, surrounded by magnificent walls, still stands today as one of the most
        unique French cities. In this game, players must develop the area around Carcassonne. They will place their
        followers onto roads and into cities, monasteries, and fields. Only those who make the most judicious
        placements will gain the points required to win the game.
        
        COMPONENTS AND SETUP
        Welcome to the Carcassonne universe! This rule book was conceived to allow you to learn to play the game as fast
        as possible. After reading it, you will be able to explain and play the game. You are going to take your first step into
        the universe of the modern classic that is Carcassonne.
        To begin, we need to set up the game, something that only takes a few brief moments. We will also take this
        opportunity to present the components:
        The first and most important pieces of Carcassonne are the Land tiles: there are 84 tiles which depict roads, cities, and monasteries, all
        of which are generally surrounded by fields.
        Twelve (12) of these tiles show a river. These are explained in the supplementary rules. Other graphical elements such as
        houses, people, or animals have no impact on the game.
        Every tile shares the same back, with the exception of the start tile and the twelve River tiles. The back of those 
        tiles is darker, making them easy to set them aside.
        Place the start tile (the one with a dark back) in the middle of the table. Shuffle the remaining tiles and set them as
        different facedown stacks that are easily accessible to all players.
        
        Then comes the scoreboard, which you set to the side of your playing surface (table, floor, etc.).
        Finally, we have the meeples. You will find in the box 40 regular meeples, including 8 meeples in each of these colors: yellow, red,
        green, blue, and black. In addition, there are also 5 abbots, including 1 in each of the same colors.
        Start by distributing 7 meeples of the color of their choice to each player (don’t forget to give yourself some as well). These meeples
        constitute each player’s personal supply.
        Then, each of you takes the remaining meeple in their color and sets it on space 0 of the scoreboard. Return to the box any unused meeples
        and, for your first game, the abbots.
        Determine a first player (for example, the youngest).
        
        OVERVIEW AND GOAL OF THE GAME
        Before diving into the explanation of this game, you should know what the goal is in Carcassonne.
        One after the other, players will place tiles. This is how, one tile at a time, a landscape of roads, cities, monasteries,
        and fields will be created and expanded. You may place your meeples on these tiles, where they will become
        highwaymen, knights, monks, and farmers and hopefully allow you to score as many points as possible. Points are
        not only earned during the game, but also at the very end. After the final scoring the player with the highest score
        is proclaimed the winner. And now, we are ready to begin!
        
        GAMEPLAY
        A game of Carcassonne is played in clockwise order. Starting with the first player, the current player does the
        following actions in the order listed below, after which it is the next player’s turn, and so on and so forth.
        First, we’ll give you a brief description of the actions you have to do during one of your turns. These actions will be
        detailed as we present the roads, the cities, and finally the monasteries. So what are these actions?
        - Placing a tile: The player must draw exactly 1 Land tile from a stack and place it faceup to continue the landscape.
        - Placing a meeple: The player may place a meeple from her supply onto the tile she has just placed.
        - Scoring a feature: The player must score any feature completed by her tile placement.
        
        The roads:
        1. Placing a tile: You draw the depicted tile with three road segments starting from a village. You must place it in such a way that it continues the existing landscape (the tiles already in play).
        2. Placing a meeple as a highwayman: After placing the tile, you may place a meeple as a highwayman on one of that tile’s road segments, but only if the road is unoccupied by another highwayman.
         In our example, since the road is not yet completed, no scoring occurs (see action 3) and play moves on to the next player. 
         The other player draws a tile that he places to continue the landscape. He may not place a meeple on the road to the right since your highwayman is already present
         on that road. Instead, he chooses to place his meeple as a knight in the city segment of that tile.
        3. Scoring a road: When both ends of a road are closed, that road is completed and scored. The end of a road is closed when it meets a village, a city, a monastery, or it loops onto itself by meeting the other end.
        So let’s see if there is a scoring here... Huzzah! There is one because both ends of the road are closed. Even though it is your opponent that placed the tile, this still completes your road.
        How many points do you score? When scoring a road, each tile of that road grants you 1 point. Here, since you scored a road that is made out of 3 tiles, you score 3 points. Well done!
        
        It is now time to note your score. You keep track of your score with the meeple you placed on the scoreboard before starting the game. Continuing our example, you move it forward 3 spaces to 
        show that you’ve scored 3 points. Note: if your score passes 50 points, lay down your scoring meeple to show your 50+ points. After each scoring, return to your 
        supply the meeple that was just scored.
        
        That’s it! We’ve already seen the most important parts of the game. Now, we will further expand on those actions by showing you how they apply to the other features, namely the cities and the monasteries.
        The cities:
        1. Placing a tile: As usual, you draw a tile that you use to continue the landscape. Of course, the illustration must be continued as well. 
        For example, a city segment must be connected to an open city.
        2. Placing a meeple as a knight: Then, you see if there is already a meeple as a knight in the city. Here, there isn’t, so you can place one of your meeples as a knight in this city.
        3. Scoring a city: Let’s continue our example and assume that a few turns have passed. You now draw this tile that you place to continue your city. Since the tile you’ve placed 
        completes a feature (here, the city), it must now be scored. A city is completed when it is surrounded by walls and there are no gaps inside the city.
        Since you have a meeple in the completed city, you are the player to score it.
        Each tile in a completed city is worth 2 points. In addition, each coat of arms is worth 2 more points. For this city, you score 8 points! As usual, the meeple that was in the scored feature returns to your supply.
        
        The monasteries:
        1. Placing a tile: Once more, you draw a tile to continue the landscape. Monasteries are always depicted in the center of a tile. When placing such a tile, you must, as usual, make sure that it continues the illustration.
        2. Placing a meeple as a monk: You can place a meeple on a monastery as a monk. Of course, that meeple must come from your supply.
        3. Scoring a monastery: A monastery is completed when it is surrounded by tiles. During scoring, the monastery is worth 1 point per tile that completes it (including the monastery itself).
        Perfect! By placing this tile, you complete your monastery. It earns you 9 points and allows you to take your meeple back.
        
        And voilà! We have already seen most of the rules for Carcassonne. There are only a few points left to see, but first, here is a summary of what we’ve seen so far:
        Summary:
        1. Placing a tile: You must place your drawn tile in such a way that it continues the landscape and the illustration. In some very rare cases, it may be impossible to place the tile. In those cases, simply return the tile to the box and draw a new one.
        2. Placing a meeple: You may place a meeple on the tile you’ve just placed. You may not place a meeple in a feature where there already is at least one other meeple.
        3. Scoring a feature: A road is completed when both ends lead to a village, a city, a monastery, or the road forms a loop. Each tile in a completed road is worth 1 point. 
        A city is completed when it is surrounded by walls and there are no holes inside the city. Each tile in the
        completed city is worth 2 points. Each coat of arms in the completed city is worth an extra 2 points. 
        A monastery is completed when it is surrounded by 8 tiles. Each of the monastery’s tiles (the 8 surrounding tiles and the one with the monastery itself) is worth 1 point.
        Scoring always occurs at the end of a player’s turn. At that moment, each player with a meeple in a scored feature earns points. After each scoring, return to your supply the scored meeples.
        If there are multiple meeples in a single scored feature, the player with the most meeples is awarded full points and all other players receive nothing. When more than one player have the most meeples in a scored feature, the tied
        players all score full points.
        (Note: How can there be more than one meeple in the same feature? More on that right below...)
        
        Many meeples in the same feature:
        The tile you’ve just drawn could continue the road. However, there already is a highwayman on that road, which means that you may not place yours.
        You decide to place your tile, and a highwayman, so that it is not connected.
        During a following turn, you draw this tile and decide to continue the road with it. Both roads, each with a highwayman, are now connected. Since this 
        completes the road, it is now scored and both you and the other player score 4 points. Then, you both take your meeple back.
        You wish to take control of the city away from yellow and place your tile as pictured with a knight on it. You are allowed to place a 
        knight there because the city segment is not connected to another city segment with a knight on it. If you succeed in linking your two city segments, your two knights will allow you to take the city from yellow.
        Lucky you! That is exactly the tile you needed to connect the city segments. Since you now have the most knights in the city, only you get to score the 
        10 points awarded for completing that city. Then, both you and the other player take back your meeples.
        
        GAME END AND FINAL SCORING
        Sadly, all good things must come to an end, and the same goes for a game of Carcassonne. You may wish that it were 
        otherwise, but there must be a winner! Thus, the game ends immediately after the turn of the player who placed the
        last tile. Then, players proceed to a final scoring, after which the winner will be known to all!
        Once the game is over, all meeples still in play are scored:
            Each incomplete road is worth 1 point per tile, just like during the game.
            Each incomplete city is worth 1 point per tile and 1 point per coat of arms, which is only half the points.
            Each incomplete monastery is worth 1 point plus 1 point per adjacent tile, just like during the game.
            Each field is worth 3 points per adjacent completed city.
        This is how farmers are scored, which is only shown here to present all the aspect of the final scoring. Farmers are
        presented in the supplementary rules. We recommend playing a few games before introducing farmers and fields.
        Once the final score is known, the winner is the player with the most points. Congratulations on winning your first
        game of Carcassonne!
        After a few games, start playing with the fields and the farmers in order to increase your strategic possibilities.
        Farmers and fields are but the first step into this brave new world of Carcassonne.
        We’d also like to take this opportunity to thank you for playing Carcassonne and we hope that you will find
        many hours of enjoyment with this game. If you have any questions, do not hesitate to contact us at the address listed below.
        """,
    },
    "splendor": {
        "name": "Splendor",
        "category": "low-interaction-procedural-games",
        "rules_text": """
        In Splendor, you take on the role of a rich merchant during the Renaissance. You will use your resources to acquire mines, transportation methods, and artisans 
        who will allow you to turn raw gems into beautiful jewels.
        
        Contents:
        40 tokens: 7 Emerald tokens (green), 7 Diamond tokens (white), 7 Sapphire tokens (blue), 7 Onyx tokens (black), 7 Ruby tokens (red), 5 Gold Joker tokens (yellow).
        90 Development cards: 40 Level 1 cards, 30 Level 2 cards, 20 Level 3 cards, 10 Noble tiles.
        
        Game setup:
        Shuffle each development card deck separately, and then place them in a column in the middle of the table in increasing order from bottom to top (O; OO; OOO).
        Then reveal 4 cards from each level.
        Shuffle the noble tiles and reveal as many of them as there are players plus one (example: 5 tiles for a 4 player game).
        The remaining tiles are removed from the game; they will not be used during the game. Finally, place the tokens in 6 distinct piles (sort themby color) within reach of the players.
        
        Game with 2 or 3 players:
        With 2 players: Remove 3 tokens of each gem color (there should be only 4 of each remaining). Don’t touch the gold. Reveal 3 noble tiles.
        With 3 players: Remove 2 tokens of each gem color (there should be only 5 of each remaining). Don’t touch the gold. Reveal 4 noble tiles.
        
        There are no other changes.
        
        Game overview:
        During the game, the players take gem and gold tokens. With these tokens, they purchase development cards,
        which are worth prestige points and/or bonuses. These bonuses allow players to purchase subsequent
        development cards for a lesser cost. When a player has enough bonuses, they immediately receive a visit
        from a noble (which is also worth prestige points).
        As soon as a player reaches 15 prestige points, the current turn ends and the player
        with the most prestige points is declared the winner.
        
        The development cards:
        To win prestige points, the players must purchase development cards. These cards are visible in the middle of the table and
        may be purchased by all players during the game. The developments in hand are the cards which the players
        reserve throughout the game. Developments in hand may only be purchased by the players holding them. 
        The player who purchases this card wins 4 prestige points. Owning this card allows the player to benefit from a blue 
        bonus. To purchase this card, the player must spend 3 blue tokens, 3 black tokens, and 6 white tokens.
        
        The noble tiles:
        The noble tiles are visible in the middle of the table. At the end of their turn, a player automatically receives the visit from 
        a noble if that player has the amount of bonuses (and only bonuses) required, and they get the corresponding tile. A player cannot refuse a visit from a noble.
        Receiving a noble isn’t considered to be an action. Each noble tile is worth 3 prestige points, but players can only get a single
        one per turn.
        The player who acquires this noble’s tile gains 3 prestige points. If a player has enough development cards to amass 3
        blue bonuses, 3 green bonuses, and 3 white bonuses, then that player automatically receives a visit from that noble.
        
        GAME RULES
        The youngest player begins. Play then proceeds clockwise. On their turn, a player must choose to perform only one of the following four actions.
        - Take 3 gem tokens of different colors.
        - Take 2 gem tokens of the same color.
        This action is only possible if there are at least 4 tokens of the chosen color left when the player takes them.
        - Reserve 1 development card and take 1 gold token (joker).
        - Purchase 1 face-up development card from the middle of the table or a previously reserved one.
        Selecting tokens:
        A player can never have more than 10 tokens at the end of their turn (including jokers). If this happens, they must return tokens until they only have 10 left. A player can return all or
        some of those they’ve just drawn. The tokens owned by a player must be visible by all players at all times.
        Reminder: players may not take 2 tokens of the same color if there are less than 4 tokens available of that color.
        Reserve a development card:
        To reserve a card, a player simply needs to take a face-up development from the middle of the table or (if you’re feeling lucky) draw the first card from one of the three decks (level O; OO; OOO) without showing it to the other players.
        The reserved cards are kept in hand and cannot be discarded.
        Players may not have more than three reserved cards in hand, and the only way to get rid of a card is to buy it (see below).
        Reserving a card is also the only way to get a gold token (joker). If there is no gold left, you can still reserve a card, but you won’t get any gold.
        Buying a development card:
        To purchase a card, a player must spend the number of tokens indicated on the card. A joker token can replace any color. The spent tokens (including any jokers) are returned to the middle of the table.
        A player may purchase one of the face-up development cards in the middle of the table or a card in his hand that was reserved on a previous turn. 
        Each player makes distinct rows with the acquired development cards by sorting them by color, and staggering them vertically so that their bonuses and prestige point 
        values are visible.
        The bonuses and prestige points granted by each card must be visible to all at all times. 
        Important: when a development card from the middle of the table is acquired or reserved, it must immediately be replaced by a card of the same level.
        At all times during the game, there must be 4 face-up cards of each level (unless the deck in question is empty, in which case the empty spaces also remain empty).
        The bonuses:
        The bonuses a player has from development cards acquired on previous turns provide discounts on the purchase of new cards. Each bonus of a given color is equal to a token of that color.
        Thus, if a player has 2 blue bonuses and wants to purchase a card which costs 2 blue tokens and 1 green token, the player must only spend 1 green token. If a player has enough development cards (and therefore 
        bonuses), they can even purchase a card without spending any tokens.
        
        The nobles:
        At the end of their turn, each player checks the noble tiles in order to determine if they’re receiving a visit from one of them.
        A player can be visited if they have (at least) the quantity and type of bonuses indicated on the noble tile. 
        It is impossible to refuse the visit from a noble, which is not considered to be an action. 
        If a player has enough bonuses to be visited by more than one noble at the end of their turn, that player chooses the noble to be received. 
        The tile obtained is placed face-up in front of the player in question. 
        
        END OF THE GAME 
        When a player reaches 15 prestige points, complete the current round so that each player has played the same number of turns. 
        The player who then has the highest number of prestige points is declared the winner (don’t forget to count your nobles). 
        In case of a tie, the player who has purchased the fewest development cards wins.
        """,
    },
    "kingdomino": {
        "name": "Kingdomino",
        "category": "low-interaction-procedural-games",
        "rules_text": """
        INTRODUCTION 
        You are a Lord seeking new lands to expand your Kingdom. You must explore all the lands, wheat fields, lakes, mountains in order to spot
        the best plots. But be careful, as some other-Lords are also coveting theses lands…
        Note: Before your first game, assemble the 4 small castles.
        OBJECT OF THE GAME
        Connect your dominoes in order to build your kingdom in a 5x5 grid in a way to score the most prestige points.
        SETUP
        Place the box as indicated to the right. Each player takes:
        2-player games: two kings of their color.
        3- and 4-player games: one king of their color.
        Each player takes a starting tile (a square) and the castle of their color. They place the tile, face up, in front of them and then they place the castle on it.
        All the dominoes are thoroughly shuffled, numbered side up, and then they are randomly placed in the box insert to form the draw pile of the game:
        2 player games: first, remove 24 dominoes randomly, set them aside. Use the remaining 24. 
        3 player games: remove 12 dominoes randomly. Play with remaining 36.
        4 player games: use all 48 dominoes.
        A Then, from the draw pile, take the same number of dominoes as the number of kings in play (i.e. three dominoes for a 3-player game and four dominoes for a 2- or 4-player game). Display
        them next to the box, numbered side up. These dominoes must be displayed in the ascending order (the lowest number next is always placed next to the box). Finally, turn them on the land scape
        side.
        B A player takes all the kings in their hands, shuffle them thoroughly and then they get them out of their hands one after the other. When your king appears, place-it on an empty domino in the 
        line. Each tile can only have one king. It means that the last player doesn’t have any choice. (In a 2-player game, each player will choose 2 dominoes, one for each of their kings). 
        C When all the dominoes have been chosen, form a new line, as you previously did, by drawing new tiles.
        PLAYING THE GAME
        The playing order is determined by the positions of the kings on the dominoes line.  The player, whose king, is placed on the 1st domino of the line (the closest to the box) starts. 
        He must take the following actions:
        D 1: Add the chosen domino to their territory according the connection rules.
        D 2: Choose a new domino in the new line by placing their king on it. 
        Then, it is the turn of the player whose king is on the second domino to take their two actions, and so on, until the last player has taken their two actions. In a 2-player game, each player
        will take the D 1 and D 2 actions twice, once for each of their kings. Then, form a new dominoes line and a new turn can start. The game is played in 12 turns in 3- or 4-player games, and only 
        6 turns in 2-player games (as each player plays twice each turn).
        Connection rules:
        The players must build a kingdom in a 5x5 grid (each domino is composed of two squares). In order to place down their domino, the player must:
        - Either connect it to their starting tile (the starting domino can be considered as a wild domino, any landscape can be connected to this domino),
        - Or connect it to another domino matching at least 1 of its landscape (horizontally or vertically only).
        If you can’t add a domino to your kingdom following these rules, the domino must be discarded and you will not get points for it.
        All your dominoes must fit in 5x5 grid. If, due to bad planning, one or more of your dominoes could not fit, they are discarded. You will not get points for them.
        END OF THE GAME
        When the last dominoes are lined up, the players will take a last turn but they will only take the 1 action. Each player should have in front of them a 5x5 grid forming their kingdom. (Some
        kingdoms may not be complete if a player was forced to discard any dominoes – see above). Then, each player will calculate their prestige points for their kingdoms in the following way:
        - A kingdom is composed of different PROPERTIES (groups of connected, either horizontally or vertically, squares of the same type of landscape).
        - Each property will give you as much prestige points as the NUMBER OF SQUARES multiplied with the NUMBER OF SPECIFIC CROWNS (see back of rules) appearing on the property.
        - You can have multiple properties with the same type of landscape in the same kingdom.
        - A property without a specific crowns will give you no points.
        - Each player will add the points given by all their properties, the result is their final score.
        The player with the highest score is the winner. In case of a tie, the player with the most extended property (whether he owns any crowns or not) wins the game.
        If it is still a tie, the player who has the most crowns wins the game. If there is still a tie anyway, the players share the victory.
        ADDITIONAL RULES
        Dynasty: Play 3 rounds in a row. At the end of the 3 rounds, the player with the highest number of points wins the game.
        The middle Kingdom: score 10 additional points if your castle is in the center of your kingdom.
        Harmony: score 5 additional points if you territory is complete (no discarded dominoes).
        The Mighty Duel: With 2 players. After one or two practice games, the real champions battle to build the largest kingdoms: use ALL the dominoes to build a 7x7 grid (a pen and paper might
        be useful to keep your final score).
        You can mix these different variants if you want according to what you prefer.
        """,
    },
    "azul": {
        "name": "Azul",
        "category": "low-interaction-procedural-games",
        "rules_text": """
        Introduced by the Moors, azulejos (originally white and blue ceramic tiles) were fully embraced by the Portuguese, when their king Manuel I, on a 
        visit to the Alhambra palace in Southern Spain, was mesmerized by the stunning beauty of the Moorish decorative tiles. The king, awestruck by
        the interior beauty of the Alhambra, immediately ordered that his own palace in Portugal be decorated with similar wall tiles. Azul brings you, 
        a tile laying artist, to embellish the walls of the Royal Palace of Evora.
        
        Game Setup
        1. Give each player a player board (A). Flip your board to the side with the colored wall. (See Variant Play to play with the gray
        side of the player board). Each player must use the same side.
        2. Take 1 scoring marker (B) and place it on space “0” of your score track.
        3. Place the Factory displays (C) in a circle around the center of the table:
            • In a 2-player game, place 5 Factory displays.
            • In a 3-player game, place 7 Factory displays.
            • In a 4-player game, place 9 Factory displays.
        4. Fill the bag (D) with the 100 tiles (20 of each color) (E).
        5. The player who most recently visited Portugal takes the starting player marker (F) and then fills each Factory display with exactly 4 tiles randomly drawn from the bag.
        Return any unused player boards, scoring markers and Factory displays to the box.
        
        Object of the game
        To be the player with the most points at the end of the game. The game ends after the round in which at least one player has
        completed a horizontal line of 5 consecutive tiles on her wall.
        
        Gameplay
        The game is played over multiple rounds, each of which is composed of three phases:
        A. Factory offer
        B. Wall-tiling
        C. Preparing the next round
        
        A. Factory offer: The starting player places the starting player marker in the center of the table and then takes the first turn. Play then
        continues clockwise. On your turn, you must pick tiles in one of the following ways:
        EITHER
            a) Pick all tiles of the same color from any one Factory display and then move the remaining tiles from this Factory display to the center of the table.
        OR
            b) Pick all tiles of the same color from the center of the table. If you are the first player in this round to pick tiles from the
            center of the table, also take the starting player marker and place it onto the leftmost free space of your floor line.
            
        Then, add the tiles you picked to one of the 5 pattern lines on your player board (the first line has 1 space to hold 1 tile, the fifth line has 5).
            • Place the tiles, one by one, from right to left in your chosen pattern line.
            • If the pattern line already holds tiles, you may only add tiles of the same color to it.
            • Once all spaces of a pattern line are filled, that line is considered complete. If you have picked up more tiles than you can place in your chosen pattern line, you 
            must place the excess tiles in the floor line (see Floor line). 
        Your goal in this phase is to complete as many of your pattern lines as you can, because during the following Wall-tiling phase,
        you will only be able to move tiles from complete pattern lines to their corresponding lines on your wall to score points.
        
        In all later rounds, you must also comply with the following rule: You are not allowed to place tiles of a certain color in
         a pattern line whose corresponding line of your wall already holds a tile of that color.
         
        Floor line
        Any tiles you have picked that you cannot or do not want to place according to the rules, you must place in your floor line, filling
        its spaces from left to right. These tiles are considered as having fallen on the floor and give minus points in the Wall-tiling phase. 
        If all spaces of your floor line are occupied, return any further fallen tiles to the lid of the game box to store them for now. 
        This phase ends when the center of the table AND all Factory displays contain no more tiles. Then, continue with the Wall-tiling phase.
        
        B. Wall-tiling: This phase can be carried out by all players simultaneously, as they move tiles from their complete pattern lines over to their walls.
            A) Go through your pattern lines from top to bottom. Move the rightmost tile of each complete line to the space of the same color in 
            the corresponding line of your wall. Each time you move a tile, score points immediately (see Scoring).
            B) Then, remove all tiles from any pattern lines that now have no tile in the rightmost space. Place them into the lid of the game box to store them for now.
            Once that is done, any remaining tiles on the pattern lines stay on your player board for the next round.
        
        Scoring 
        Each tile you move over to your wall is always placed on the space matching its color and immediately scores as follows:
            • If there are no tiles directly adjacent (vertically or horizontally) to the newly placed tile, gain 1 point on the score track.
            • If there are any tiles adjacent, however, do the following: 
                First check if there are 1 or more tiles horizontally linked to the newly placed tile. If so, count all these linked tiles
                (including the newly placed one) and gain that many points.
                Then check if there are 1 or more tiles vertically linked to the newly placed tile. If so, count all these linked tiles (including the newly placed tile) and gain that many points.
                Finally, at the end of the Wall-tiling phase, check if you have any tiles in your floor line. For each tile in your floor line, you lose 
                the number of points indicated directly above it. Adjust your scoring marker on your score track accordingly (however, you can never drop below 0 points).
                Afterwards, remove all tiles in your floor line and place them into the lid of the game box. Note: If you have the starting player marker in your floor line, it counts as a normal tile there. But 
                instead of placing it in the lid, place it in front of you.
        
        C. Preparing the next round: If nobody has completed a horizontal line of 5 consecutive tiles on her wall yet (see End of the game), prepare the next round.
        The player with the starting player marker refills each of the Factory displays with 4 tiles from the bag as in the setup. If the bag is empty, refill it with all the tiles that you have placed in
        the lid of the game box and then continue filling the remaining Factory displays. Then, start the new round. In the rare case that you run out of tiles again while there are 
        none left in the lid, start the new round as usual even though not all Factory displays are properly filled.
        
        End of the game 
        The game ends right after the Wall-tiling phase in which at least one player has completed at least one horizontal line of 5 consecutive tiles on her wall.
        Once the game has ended, score additional points if you have
        achieved the following goals:
            • Gain 2 points for each complete horizontal line of 5 consecutive tiles on your wall.
            • Gain 7 points for each complete vertical line of 5 consecutive tiles on your wall.
            • Gain 10 points for each color of which you have placed all 5 tiles on your wall.
        The player with the most points on her score track wins the game. In the case of a tie, the tied player with more complete horizontal lines wins the game.
        If that does not break the tie, the victory is shared.
        
        Variant play
        For a slightly different game, use the gray side of the player boards. Rules are exactly the same as in the normal game, except that
        when you move a tile from a pattern line to the wall, you may place it on any space of its corresponding wall line. However, as the 
        game progresses, in each of the 5 vertical lines of your wall, no color may appear more than once. Also keep in mind that in each horizontal line, no color may appear more than once either.
        Special case: In the wall-tiling phase, it may happen that you are not able to move the rightmost tile of a certain pattern line over 
        to the wall because there is no valid space left for it. In this case, you must immediately place all tiles of that pattern line in your floor line (see Floor line).
        """,
    },
    "crazy-eights": {
        "name": "Crazy 8's",
        "category": "exception-heavy rule systems",
        "rules_text": """
        Set Up: 
        Pass out 5 cards faced down to all players. The remaining cards are placed in the center of the
        group. The top card from the center is flipped over and placed next to the pile.
        If the first card is an 8, the 8 is placed somewhere in the middle of the pile and a new starter card is flipped over.
        
        How to Play:
        Players try to get rid of their cards by placing them on top of the flipped up card in the center.
        Players may do so if the card they want to get rid of is the same number or suit of the card
        flipped up. 8s are wild and if a player plays an 8, they must state what suit the 8 will be for the
        next player. If a player cannot place any of their cards on the one in the center, they must draw
        cards from the pile until they can do so or until they’ve drawn a maximum of five cards.
        
        Scoring:
        After a player gets rid of all of their cards, the round is over and points are tallied. Cards
        remaining in players’ hands are counted as the following point values:
        - Cards 2 through 9 (except the 8) are worth their face value
        - Aces are worth 1 point
        - Cards 10 through King are worth 10 points
        - 8s are worth 50 points.
        Once a player reaches 100 points or above, the player with the lowest number of points wins the game.
        """,
    },
    
    "uno": {
        "name": "UNO",
        "category": "exception-heavy rule systems",
        "rules_text": """
        What you need to play Uno:
        Uno deck (usually 108 cards)
        2-10 players
        Paper and pen for scoring
        A flat surface to place the deck
        
        1- Distribute Cards
        All players draw one card. The one with the highest card becomes the dealer (the one who deals the cards). Cards with symbols count as zero. The dealer shuffles and deals 7 cards to each player.
        
        2- Set Up a DRAW Pile
        Place the remaining cards face down in the middle of the table. This becomes your DRAW pile from which you'll draw cards during the game.
        
        3- Lay the First Card
        The dealer draws the first card, flipping it symbol-side up next to the DRAW pile. This starts a new pile where you'll play your cards, known as the DISCARD pile.
        
        4- Start Playing Uno
        The game begins with the player to the dealer's left. You must play a card matching the color, number, or symbol of the first card in the DISCARD pile. The gameplay then continues to the next player.
        For the first card being a special card (also known as an action card), refer to step 6 for more information.
        
        5- Draw a Card
        If you cannot play a card, draw one from the DRAW pile. If it's playable, you can use it immediately if you want.
        If you can't play it, keep it and the turn passes to the next player.
        
        6- Special Cards
        Besides the regular number cards (0-9), Uno contains five types of special cards:
        Draw Two - The next player must draw 2 cards and lose their turn.
        Reverse - Changes the direction of play.
        Skip - The next player is skipped.
        Wild - Lets you choose the color to continue with, without playing another card.
        Wild Draw Four - Lets you choose the color, and the next player must draw four cards and lose their turn.
        
        7- Don't Forget to Say Uno!
        Remember to say "Uno!" when you have one card left. The game continues until someone has one card and declares, "Uno!".
        If a player forgets to say "Uno!" when they have one card left and is caught, that player must draw two cards.
        If no one notices and the next player plays a card or draws from the DRAW pile, the game continues without penalty.
        
        8- Who Wins?
        Play your last card to win the round. Being on your last card brings you closer to winning. If it's your turn and you can play your last card, you win.
        If you can't play your last card, draw a card from the DRAW pile. The player who has no cards left wins.
        
        9- Counting Points
        Tally the points on paper after each round. The first player to shed their cards earns points from the remaining cards of the opponents. Points are scored as follows:
        Number cards: Face value (0-9)
        Draw Two, Reverse & Skip cards: 20 points
        Wild & Wild Draw Four cards: 50 points
        Shuffle Hand & Custom cards: 40 points
        The first player to reach 500 points wins!
        """,
    },
    
    "fluxx": {
        "name": "Fluxx",
        "category": "exception-heavy rule systems",
        "rules_text": """
        OVERVIEW
        Fluxx is an easy game to learn because it starts out simple—Draw 1, Play 1—and becomes more complicated little by little. Many folks find 
        that the best way to learn is by jumping right into a game, but that usually works best if at least one player in the group has played a Fluxx game 
        before. So, if this is the first time for everyone, someone in the group needs to read these rules. But don’t worry, after you’ve played the game 
        a few times, everyone will understand!
        
        SET UP
        Place the Basic Rules card in the center of the table. Shuffle the deck and deal three cards to each player. Place the remainder of the deck face down next to
        the Basic Rules to form a Draw pile. At the beginning of the game, there will be no Goal or New Rule cards in play yet.
        
        GOING FIRST
        There is no rule for who gets to go first. You decide!
        
        HOW TO PLAY
        Fluxx is a game about change, so it’s a game that changes as you play it. It begins with just a couple of very simple rules, and becomes more complex as additional rules are added via special cards called 
        New Rules. Start by following the Basic Rules (draw one card & play one card), and adapt to all additional New Rules as they are played. Players take turns, going clockwise around the table, drawing and playing the indicated 
        number of cards until someone meets the current Goal condition.
        
        ON YOUR TURN
        1) Draw the number of cards currently required. 
        2) Play the number of cards currently required.
        3) Discard down to the current Hand Limit (if any).
        4) Comply with the current Keeper Limit (if any).
        
        When playing a card, you may choose any card in your hand. If you aren’t sure how a card works, try reading the full text aloud as you play it.
        
        CARD TYPES
        BASIC RULES: This is the starting point - the foundation on which the rest of the game is built. These initial rules will be superseded by New Rules during the course of play, but this 
        card should remain on the table at all times. The Basic Rules are: Draw 1 card per turn and Play 1 card per turn (with no other restrictions such as Hand or Keeper Limits).
        NEW RULE: To play a New Rule place it face up near the Basic Rules. If it contradicts a New Rule already in play, discard the old rule. New Rules take effect instantly, so all players must 
        immediately follow the New Rule as required. This will often cause the player whose turn it is to draw or play additional cards right away, or it may cause other players to immediately discard some of their cards.
        
        Examples: After drawing 1 card, you play the Draw 4 New Rule. Now the rules require you to Draw 4 cards on each turn, but since you only 
        took 1 card before, you must immediately draw 3 more cards. The next player draws 4 cards. He plays the Draw 2 which changes the 
        rules again, but he draws no more, having already gotten (at least) 2 cards. Since Draw 2 contradicts Draw 4, the Draw 4 is discarded.
        
        GOAL: To play a Goal place it face up in the center of the table, discarding the previous Goal (if any). The game begins with no Goal in play, so no one can win until one is played. The 
        Goal applies to everyone; as soon as someone meets these conditions, they win! (Even if it’s someone else’s turn!)  
        KEEPER: To play a Keeper take it out of your hand and place it on the table in front of you, face up. Most Goals require you to have a particular pair of Keepers, so playing a Keeper is 
        always a good thing. 
        ACTION: Actions are used once and discarded. Just do whatever the card says, then place it on the Discard Pile. Actions can sometimes cause major chaos, and yet at other 
        times, have no effect at all. Note that while some Actions may cause additional cards to be played, everything that happens as a result of an Action card is considered part of one “play".
        
        Examples: If you play the Action called Draw 2 and Use ‘em you will immediately draw two cards and play them both. If one of those cards 
        is Draw 3, Play 2 of them you’d keep going, drawing three more. cards, playing two cards and discarding the third. All of this activity would be counted as the playing of just one card.
        
        WINNING
        The game continues until someone meets the conditions of the current Goal. That player wins instantly, no matter whose turn it is!
        
        NOTES
        If the Draw pile runs out, shuffle the Discard pile, turn it over to make a new Draw pile, and keep playing. 
        Whenever something mentions a card “in play”, this refers to a card that is face up on the table, but not in the discard pile.
        
        Regarding Discarding: Discarding a card is not the same as playing it. When a card is played all instructions on that card must be followed, if possible. You cannot simply discard unwanted cards; you 
        can only discard if compelled to by a Hand Limit. (Yes, this means you could be forced to play a card that makes someone else win.)
        
        The game doesn’t end until there is a clear winner. If for some reason two or more players meet the winning conditions simultaneously, the game 
        continues until a single winner emerges. New players may join at any time by being dealt a hand of three cards.
        
        Regarding Creepers: Version 4.0 of this game included a new type of card called Creepers, but we took those cards back out because 
        we decided the original game is better without them. But you’ll find plenty of Creepers in Zombie Fluxx, Cthulhu Fluxx, Oz Fluxx, Monty Python Fluxx, etc.
        """,
    },
    
    "exploding-kittens": {
        "name": "Exploding Kittens",
        "category": "exception-heavy rule systems",
        "rules_text": """
        HOW IT WORKS
        In the deck of cards are some Exploding Kittens. You play the game by putting the deck face down and taking turns drawing cards until someone 
        draws an Exploding Kitten. When that happens, that person explodes. They are now dead and out of the game.
        This process continues until there’s only 1 player left, who wins the game. The more cards you draw, the greater your chances of drawing an Exploding Kitten.
        
        BASICALLY
        If you explode, you lose. And you are full of incendiary loser sadsauce.
        If you don't explode, you win. And you are full of greatness. Good job, buddy.
        And all of the other cards will lessen your chances of getting exploded by Exploding Kittens. 
        For example: You could use a See the Future Card to peek at the top few cards in the Draw Pile. If that reveals an Exploding Kitten you could then use a Skip Card 
        to end your turn and avoid drawing it.
        
        SETUP
        1- To start, remove all the Exploding Kittens (4) and Defuse Cards (6) from the deck.
        2- Shuffle the remaining deck and deal 4 cards face down to each player.
        3- Deal 1 Defuse Card to each player so that everyone has a hand of 5 cards total (including the Defuse Card).
        Each player starts with a Defuse Card; the most powerful card in the game. These are the only cards that can save you from Exploding Kittens. If you draw an Exploding Kitten, instead of getting exploded, you 
        can play the Defuse Card and reinsert the Kitten back into the Draw Pile anywhere you’d like in secret. Try to get as many Defuse Cards as possible.
        4- Insert enough Exploding Kittens back into the deck so that there is 1 fewer than the number of people playing. Remove any extra Exploding Kittens from the game.
        For a 4 player game, insert 3 Kittens. For a 3 player game, insert 2 Kittens. This ensures that everyone eventually explodes except for 1 person.
        5- Insert the extra Defuse Cards back in the deck. Two player variant: put only 2 of the extra Defuse Cards back in the deck. Remove the other 2 from the game.
        6- Shuffle the deck, and put it face down in the middle of the table.
        7- Pick a player to go first. (Some sample criteria: most impressive beard, most intimidating odor, shortest spleen, etc.)
        
        TAKING YOUR TURN
        Gather all 5 of your cards into your hand and look at them. Do one of the following:
            - Pass: Play no cards.
            - Play: Play a card by placing it FACE UP on top of the Discard Pile and following the instructions on the card. Read the text on a card to learn what it does. After you follow the instructions on the card, you can play
            more cards. You can play as many cards as you’d like. Cards with no instructions on them: Some cards don’t have any instructions on them (Cat Cards). These cards must be collected and played as matching Pairs If you play matching Pairs of Cat Cards, pick another 
            player and steal a random card from their hand.
        
        End your turn by drawing a card from the top of the Draw Pile into your hand and hoping it’s not an Exploding Kitten.
        (This is different from most games in that you END YOUR TURN by drawing a card.) Play continues clockwise around the table.
        Remember: Play as many or as few cards as you’d like, then draw a card to end your turn.
        
        ENDING THE GAME
        The last player who hasn't exploded wins the game. You won't ever run out of cards in the Draw Pile because you inserted enough Exploding Kittens to kill all but 1 player.
        
        THREE MORE THINGS
        A good strategy is to save your cards early in the game while your chance of exploding is low.
        You can always count the cards left in the Draw Pile to figure out the odds of exploding.
        There is no maximum or minimum hand size. If you run out of cards in your hand, there’s no special action to take. Keep playing. You’ll draw at least 1 more card on your next turn.
        
        SPECIFIC CARDS
        Exploding Kitten (4 cards): You must show this card immediately. Unless you have a Defuse Card, you’re dead. Discard all of your cards, including the Exploding Kitten.
        Defuse (6 cards): If you drew an Exploding Kitten, you can play this card instead of dying. Place your Defuse Card in the Discard Pile. Then take the Exploding Kitten, and without 
        reordering or viewing the other cards, secretly put it back in the Draw Pile anywhere you’d like. Want to screw over the player right after you? Put the Kitten right on top of the deck. If you’d 
        like, hold the deck under the table so that no one else can see where you put it. Your turn is over after playing this card.
        Nope (5 cards): Stop any action except for an Exploding Kitten or a Defuse Card. Imagine that any card beneath a Nope Card never existed. You can also play a 
        Nope on another Nope to negate it and create a Yup, and so on. Stop any action except for an Exploding Kitten or a Defuse Card. Imagine that any card 
        beneath a Nope Card never existed. You can play a Nope Card at any time before an action has begun, even if it’s not your turn. Any cards that have been noped are lost. Leave them in the Discard Pile. You can even play a Nope on 
        a SPECIAL COMBO.
        Attack (4 cards): Immediately end your turn(s) without drawing and force the next player to take 2 turns in a row. The victim of this card takes a turn as normal 
        (play-or-pass then draw). Then, when their first turn is over, it’s their turn again. (If the victim of an Attack Card plays an Attack Card, their turns are immediately over, and the next player must take 2 turns.)
        Skip (4 cards): Immediately end your turn without drawing a card. (If you play a Skip Card as a defense to an Attack Card, it only ends 1 of the 2 turns. 
        2 Skip Cards would end both turns.
        Favor (4 cards): Force any other player to give you 1 card from their hand. They choose which card to give you.
        Shuffle (4 cards): Shuffle the Draw Pile without viewing the cards until told to stop. (Useful when you know there’s an Exploding Kitten coming.)
        See the future (5 cards): Peek at the top 3 cards from the Draw Pile and put them back in the same order. Don’t show the cards to the other players.
        Cat cards (4 of each): These cards are powerless on their own, but if you collect any 2 matching Cat Cards, you can play them as a Pair to steal a random card from any other player. 
        They can also be used in Special Combos.
        
        SPECIAL COMBOS
        Two of a kind: Playing matching Pairs of Cat Cards (where you get to steal a random card from another player) no longer only applies to pairs of Cat 
        Cards. It now applies to ANY pair of cards with the same title (a pair of Shuffle Cards, a pair of Skip Cards, etc).
        Three of a kind: Exactly the same as Two of a Kind, but you get to name the card you want from the other player. If they have it, you get to take it. If not, you get nothing.
        5 different cards: If you play 5 different cards (any 5 cards with different titles), go through the Discard Pile to take any single card you’d like. 
        (Grab the Pile quickly to choose your card so that you don’t get “Noped!”) 
        When you play special combos, ignore theinstructions on the cards.
        
        """,
    },
    
    "mao": {
        "name": "Mao",
        "category": "exception-heavy rule systems",
        "rules_text": """
        Mao is half card game and half prank. The object of the game is to get rid of all of the cards in your hand by playing one card per turn. The biggest twist in this game is that you are not allowed to teach the rules to new players.
        They must figure it out by observing gameplay and making mistakes, hence the prank. These instructions are written for people who already have some knowledge of card playing terms, but there is a glossary of terms that beginners may
        not be familiar with in the final step.
        
        Step 1: Game Set-up
        
        The Deck
        The size of the deck is not important. Usually, you want about one 52 card deck for every 2 - 3 players. Extra cards, missing cards and non-matching card backs are also okay.
        
        The Deal
        Each player is dealt 7 cards. Once the cards are dealt the dealer will place the remaining cards face down in the middle of the playing area as the draw pile and place the top card face up next to the draw pile.
        
        Starting the Game
        Upon receiving their cards, players are not allowed to touch their cards until the dealer says, “The seven card game of Mao is now in session.” At this point game play will begin with the player to the left of the dealer and continue clockwise from there.
        
        Step 2: Gameplay
        
        The Basics
        On each player’s turn they may play one card of the same value or suit of the face up card in the middle of the play area. If the player is unable to do so, they must draw one card and knock on the table.
        
        Special Rules
        These are the rules that really give new players the hardest time.
            - Talking is not allowed during gameplay
            - Playing an 8 reverses the order of play.
            - Playing an Ace skips the next players turn
            - Jacks are wild cards. It can be played on any suit and the player calls out a new suit of their choosing. Play will continue as if the chosen suit is on top of the play pile.
            - When playing a spade card, you must name the card just played. For example, Jack plays the ace of spades, so he must say “Ace of spades.”
            
        Step 3: Sevens
        If a seven is played, the player must say "Have a nice day," and the next player must either draw a card or play another seven and say "Have a very nice day."
        If multiple sevens are played in a row, the player of each seven must add one "very" to the phrase "Have a very nice day," and when a player is unable to play a seven, they must draw one card for each seven played before their turn. This concludes the players turn. 
        
        Step 4: Penalties
        
        Giving Penalties
        Whenever a rule is broken, the player is penalized by being given one card from the draw pile. Any player can administer a penalty card, and upon giving the card, they must state what the penalized play has done to deserve the card.
        
        For example:
            1. Jim talks during the game. You give Jim one card and say, “Talking.”
            2. Suzy plays a seven, but forgets to say "Have a nice day." You give her one card and say, “Failure to say ‘have a nice day.’”
        
        Bad Calls
        If a player penalizes you improperly, you may give that player the penalty card they just gave you and one additional penalty card and say, "bad call."
        
        Step 5: Point of Order
        alking is not allowed in the game. This makes disputes on the rules not only difficult, but impossible during normal game play.
        If a break in the game is needed for any reason, any player can declare a point of order by saying “Point of Order.”
        
        Point of order rules
            - Talking is allowed
            - Players must refer to everyone, including themselves, in the third person.
            - Saying “point of order” is not allowed during a point of order. A penalty card will be given and explained by saying, “Saying P of O during a P of O.”
            - The point of order is ended when any player says, “Point taken.”
            
        Step 6: Ending the Game
        The game is won when a player plays his or her very last card and says, “Mao.” The winner of the game gets to make up one new rule for the next time the game is played. This rule cannot contradict an already existing rule.
        This rule is not told to the rest of the players. They must figure it out during gameplay.
        
        Step 7: Definitions
        Suit: The set of four different symbols (Pictured) that categorize a deck of playing cards. Those symbols are hearts (top left), spades (top right), clubs (bottom left), and diamonds (bottom right).
        Deck: The complete set of 52 playing cards.
        Hand: The cards that each individual player holds in his or her hand and plays out of.
        Deal: The act of distributing a deck of cards into each players hand to start a card game.
        """,
    },
    
    "monopoly": {
        "name": "Monopoly",
        "category": "thematic games with randomness",
        "rules_text": """
        AGES 8+
        2 to 8 Players
        Contents: Gameboard, 3 dice, tokens, 32 houses, I 2 hotels, Chance
        and Community Chest cards, Title Deed cards, play money and a Banker's tray.
        Now there's a faster way to play MONOPOLY. Choose to play by
        the classic rules for buying, renting and selling properties or use the
        Speed Die to get into the action faster. If you've never played the classic
        MONOPOLY game, refer to the Classic Rules beginning on the next page.
        If you already know how to play and want to use the Speed Die, just
        read the section below for the additional Speed Die rules.
        SPEED DIE RULES
        Learnins how to Play with the Speed Die is as fast as playing with i't.
            1. When starting the game, hand out an extra $1,000 to each player
                (two $5005 should work). The game moves fast and you'll need
                the extra cash to buy and build.
            2. Do not use the Speed Die until you've landed on or passed over
                GO for the first time. Once you collect that first $200 salary, you'll
                use the Speed Die for the rest of the game. This means that some
                players will start using the die before others.
            3. Once you start using the Speed Die, roll it along with the two
                white dice on your turn. Then do the following depending on
                what you rolled.
                    1, 2, or 3: Add this number to the roll of the two white
                        dice. You'll zoom around the board.
                    Bus: This lets you "get off the bus early." Look at the two white
                        dice. You can move the value of one die, the other die, or the
                        sum of both dice. So if you rolled a 1 and a 5, you can move
                    1 space, 5 spaces, or 6 spaces: it's your choice.
                    Mr. Monopoly: First, move the sum of the two white dice
                        and resolve the space you land on (such as drawing a card,
                        buying the property, paying rent, etc.). Then, one of two
                        things will happen depending on whether or not there is still
                        property in the bank.
                        YES, there is property in the bank -Advance to the NEXT
                        property that the bank still holds and buy it if you wish. If you
                        don't want to buy this property, move to the space anyway
                        and put the property up for auction.
                        NO, there are no more properties in the bank - Advance to the
                        NOCT property on which you will owe another player money.
        A few minor details:
            Only the white dice are used when determining if you rolled doubles.
            Do not look at the Speed Die.
            If you roll a three-of-a-kind (all of the dice show the same number),
            you can move anywhere you want on the board!
            If you get sent to jail during your move (either by landing on the "Go
            to Jail" space or by rolling doubles three times in a row) then your turn
            is over and you do not get to use the Speed Die for that turn.
            Use the white dice ONLY when rolling to get out of jail. L
            Use the sum of all three dice when determining how much to pay on
            a utility. Note: The Bus and Mr. Monopoly are valued at 0.
                
        CLASSIC MONOPOW RULES
        OBJECT: The object of the game IS to become the
        wealthiest player through buying, renting and selling
        property.
        
        PREPARATION: Place the board on a table and put
        the Chance and Community Chest cards facedown on
        their allotted spaces on the board. Each player chooses one token to
        represent himther while traveling around the board.
        
        Each player is given $1,500 divided as follows: 2 each of $500s,
        $100s and $50s; 6 $40s; 5 each of $10s, $ 5s and $1s.
        All remaining money and other equipment go to the Bank.
        Stack the Bank's money on edge in the compartments in the plastic Banker's tray.
        
        BANKER: Select as Banker a player who will also
        make a good Auctioneer A Banker who plays
        in the game must keep hislher personal funds
        separate from those of the Bank. When more than
        five persons play, the Banker may elect to act only
        as Banker and Auctioneer.
        
        THE BANK: Besides the Bank's money, the Bank
        holds the Title Deed cards and houses and hotels prior to purchase
        and use by the players. The Bank pays salaries and bonuses. It sells
        and auctions properties and hands out the~r proper Title Deed cards;
        it sells houses and hotels to the players and loans money when
        required on mortgages.
        
        The Bank collects all taxes, fines, loans and interest, and the price of
        all properties which it sells and auctions.
        The Bank nwer "goes broke." If the Bank runs out of money, the Banker
        may issue as much more as needed by writing on any ordinary paper.
        THE PLAY: Starting with the Banker, each player in turn throws the dice.
        The player with the highest total starts the play: Place your
        token on the corner marked "GO," throw the dice and move
        your token in the direction of the arrow the number of
        spaces indicated by the dice. After you have completed
        your play, the turn passes to the left. The tokens remain
        on the spaces qccupied and proceed from that point on
        the player's next turn. Two or more tokens may rest on the
        same space at the same time.
        According to the space your token reaches, you may be entitled to
        buy real estate or other properties - or obliged to pay rent, pay taxes,
        draw a Chance or Community Chest card, "Go to Jail," etc.
        If you throw doubles, you move your token as usual, the sum of the
        two dice, and are subject to any privileges or penalties pertaining to
        the space on which you land. Retaining the dice, throw again and move
        your token as before. If you throw doubles three times in succession,
        move your token immediately to the space marked "In Jail" (see JAIL).
        
        "GO": Each time a player's token lands on or passes over
        GO, whether by throwing the dice or drawing a card,
        the Banker pays himther a $200 salary.
        The $200 is paid only once each time kound
        the board. However, if a player passing GO on
        the throw of the dice lands 2 spaces beyond it
        on Community Chest, or 7 spaces beyond
        it on Chance, and draws the "Advance to GO" card, helshe collects
        $200 for passing GO the first time and another $200 for reaching it the
        second time by instructions on the card.
        
        BUYING PROPERTY: Whenever you land on an unowned property you
        may buy that property from the Bank at its printed price. You receive the
        Title Deed card showing ownership; place it faceup in front of you.
        If you do not wish to buy the property, the Banker sells it at auction
        to the highest bidder. The buyer pays the Bank the amount of the bid
        in cash and receives the Title Deed card for that property. Any player,
        including the one who declined the option to buy it at the printed
        price, may bid. Bidding may start at any price.
        
        PAYING RENT: When you land on property owned by another player,
        the owner collects rent from you in accordance with the list printed on
        its Title Deed card.
        If the property is mortgaged, no rent can be collected. When a
        property is mortgaged, its Title Deed card is placed facedown in front
        of the owner.
        It is an advantage to hold all the Title Deed cards in a color-
        group (e.g., Boardwalk and Park Place; or Connecticut, Vermont and
        Oriental Avenues) because the owner may then charge double rent
        for unimproved properties in that color-group. This rule applies to
        unmortgaged properties even if another property in that color-group is
        mortgaged.
        It is even more advantageous to have houses or hotels on properties
        because rents are much higher than for unimproved properties.
        The owner may not collect the rent if he/she fails to ask for it before
        the second player following throws the dice.
        
        "CHANCE" AND "COMMUNITY CHEST": When you land on either of
        these spaces, take the top card from the deck indicated, follow the
        instructions and return the card facedown to the bottom of the deck.
        The "Get Out of Jail Free" card is held until used and then returned to
        the bottom of the deck. If the player who draws it does not wish to use
        it, helshe may sell it, at any time, to another player at a price agreeable
        to both.

        "INCOME TAX": If you land here you have two options: You may
        estimate your tax at $900 and pay the Bank, or you may pay 10"%" of
        your total worth to the Bank. Your total worth is all your cash on hand,
        printed prices of mortgaged and unmortgaged properties and cost
        price of all buildings you own.
        You must decide which option you will take before you add up
        your total worth.

        "JAIL": You land in Jail when: (1) your token lands on the space
        marked "Go to Jail"; (2) you draw a card marked "Go to Jail"; or
        (3) you throw doubles three times in succession.
        When you are sent to Jail you cannot
        collect your $200 salary in that move
        since, regardless of where your token
        is on the board, you must move it
        directly into Jail. Your turn ends when
        you are sent to Jail.
        If you are not "sent" to Jail but in the ordinary course of play land on
        that space, you are "Just Visiting," you incur no penalty, and you move
        ahead in the usual manner on your next turn.
        You get out of Jail by: (1) throwing doubles on any of your next
        three turns; if you succeed in doing this you immediately move forward
        the number of spaces shown by your doubles throw; even though you
        had thrown doubles, you do not take another turn; (2) using the "Get
        Out of Jail Free" card if you have it; (3) purchasing the "Get Out of Jail
        Free" card from another player and playing it; (4) paying a fine of $50
        before you roll the dice on either of your next two turns.
        If you do not throw doubles by your third turn, you must pay the $50
        fine. You then get out of Jail and immediately move forward the number
        of spaces shown by your throw.
        Even though you are in Jail, you may buy and sell property, buy and
        sell houses and hotels and collect rents.
        
        "FREE PARKING": A player landing on this place does not
        receive any money, property or reward of any kind. This is just a "free"
        resting place.
        
        HOUSES: When you own all the properties in a color-group
        you may buy houses from the Bank and erect them on those properties.
        If you buy one house, you may put it on any
        one of those properties. The next house you
        buy must be erected on one of the unimproved
        properties of this or any other complete color-
        group you may own.
        The price you must pay the Bank for each
        house is shown on your ltle Deed card for the
        property on which you erect the house.
        The owner still collects double rent from an opponent who lands on
        the unimproved properties of hisher complete color-group.
        Following the above rules, you may buy and erect at any time as
        many houses as your judgement and financial standing will allow. But
        you must build evenly, i.e., you cannot erect more than one house on
        any one property of any color-group until you have built one house on
        every property of that group. You may then begin on the second row
        of houses, and so on, up to a limit of four houses to a property. For
        example, you cannot build three houses on one property if you have
        only one house on another property of that group.
        As you build evenly, you must also break down evenly if you sell
        houses back to the Bank (see SELLING PROPERTY).
        
        HOTELS: When a player has four houses on each property of a
        complete color-group, hdshe may buy a hotel from the Bank and erect
        it on any property of the color-group. Hdshe returns the four houses
        from that property to the Bank and pays the price for the hotel as shown
        on the Ttle Deed card. Only one hotel may be erected on any one
        property.
        
        BUILDING SHORTAGES: When the Bank has no houses to sell, players
        wishing to build must wait for some player to return or sell histher
        houses to the Bank before building. If there are a limited number of
        houses and hotels available and two or more players wish to buy more
        than the Bank has, the houses or hotels must be sold at auction to the
        highest bidder.
        
        SELLING PROPERTY: Unimproved properties, railroads and utilities
        (but not buildings) may be sold to any player as a private transaction
        for any amount the owner can get; however, no property can be sold to -
        another player if buildings are standing on any properties of that color-
        group. Any buildings so located must be sold back to the Bank before
        the owner can sell any property of that color-group.
        Houses and hotels may be sold back to the Bank at any time for one-
        half the price paid for them.
        All houses on one color-group must be sold one by one, evenly, in
        reverse of the manner in which they were erected.
        All hotels on one color-group may be sold at once, or they may be
        sold one house at a time (one hotel equals five houses), evenly, in
        reverse of the manner in which they were erected.

        MORTGAGES: Unimproved properties can be mortgaged through the
        Bank at any time. Before an improved property can be mortgaged, all
        the buildings on all the properties of its color-group must be sold back
        to the Bank at half price. The mortgage value is printed on each Title
        Deed card.
        No rent can be collected on mortgaged properties or utilities,
        but rent can be collected on unmortgaged properties in the
        same group.
        In order to lift the mortgage, the owner must pay the Bank the
        amount of the mortgage plus 10"%" interest. When all the properties of
        a color-group are no longer mortgaged, the owner may begin to buy
        back houses at full price.
        The player who mortgages property retains possession of it and
        no other player may secure it by lifting the mortgage from the Bank.
        However, the owner may sell this mortgaged property to another player
        at any agreed price. If you are the new owner, you may lift the mortgage
        at once if you wish by paying off the mortgage plus
        10"%" interest to the Bank. If the mortgage is not lifted
        at once, you must pay the Bank 10"%" interest when
        you buy the property and if you lift the
        mortgage later you must pay the Bank
        an additional 10"%" interest as well
        as the amount of the mortgage.
        
        BANKRUPTCY: You are declared bankrupt if you owe more than you
        can pay either to another player or to the Bank. If your
        debt is to another player, you must tum over to that
        player all that you have of value and retire from the
        game. In making this settlement, if you own houses or
        hotels, you must retum these to the Bank in exchange
        for money to the extent of one-half the amount paid
        for them; this cash is given to the creditor. If you have
        mortgaged property you also turn this property over
        to your creditor but the new owner must at once pay
        the Bank the amount of interest on the loan, which is 10"%" of the value of
        the property. The new owner who does this may then, at hislher option,
        pay the principal or hold the property until some later turn, then lift the
        mortgage. If helshe holds property in this way until a later turn, helshe
        must pay the interest again upon lifting the mortgage.
        Should you owe the Bank, instead of another player, more than you
        can pay (because of taxes or penalties) even by selling off buildings
        and mortgaging property, you must turn over all assets to the Bank. In
        this case, the Bank immediately sells by auction all property so taken,
        except buildings. A bankrupt player must immediately retire from the
        game. The last player left in the game wins.
        
        MISCELLANEOUS: Money can be loaned to a player only by the Bank
        and then only by mortgaging property. No player may borrow from or
        lend money to another player.
        """,
    },
    
    "risk": {
        "name": "Risk!",
        "category": "thematic games with randomness",
        "rules_text": """
        INTRODUCTION & STRATEGY HINTS
        In the classic “World Domination RISK®‘” game of military strategy, you are
        battling to conquer the world. To win, you must launch daring attacks,
        defend yourself on all fronts, and sweep across vast continents with
        boldness and cunning. But remember, the dangers, as well as the rewards,
        are high. Just when the world is within your grasp, your opponent might
        strike and take it all away!
        See pages 1l- 16 for gameplay variations and variations for RISK experts.
        
        Strategy. In all the RISK games, keep these 3 strategy hints in mind as you
        play, add armies, and fortify:
            1. Conquer whole continents: You will earn more armies that way.
            (This doesn’ t apply in Secret Mission Risk.)
            2. Watch your enemies: If they are building up forces on adjacent
            territories or continents, they may be planning an attack. Beware!
            3. Fortify borders adjacent to enemy territories for better defense if a
            neighbor decides to attack you.
        
        EQUIPMENT
        1 Tri-fold Game Board, 5 Dice: 2 white and 3 red, Deck of 56 RISK cards,
        6 Sets of armies, each a different color.
        
        The Game Board. The game board is a map of 6 continents divided into
        42 territories. Each continent is a different color and contains from 4 to 12
        territories. The numbers along the bottom (southern) edge of the board
        indicate the number of armies you will receive for a set of cards you trade
        in, as explained on page 7.
        
        The Armies. There are 6 complete sets of armies, each containing 3
        denominations of army pieces: Infantry (worth l), Cavalry (worth 5
        Infantry), and Artillery (worth 10 Infantry, or 2 Cavalry). Start the game by
        placing Infantry pieces; later in the game, you may trade in 5 Infantry for
        1 Cavalry, or 2 Cavalry (or 1 Cavalry and 5 Infantry) for 1 Artillery.
        
        The 56 RISK Cards: 42 marked with a territory and a picture of
        Infantry, Cavalry, or Artillery, 2 “wild” cards marked with all three pictures,
        but no territory, 12 Secret Mission cards used only in Secret Mission Risk,
        page 13.
        
        Note: The 12 Secret
        Mission cards are used
        only in the Secret Mission
        RISK variation. Remove
        them for all other games.
        
        WORLD DOMINATION RISK®
        OBJECT OF THE GAME
        To conquer the world by occupying every territory on the board, thus
        eliminating all your opponents.
        
        SETUP
        Unlike most games, RISK demands careful planning before you actually
        start to play. This Initial Army Placement sets the stage for the battles you’ ll
        fight later on.
        
        INITIAL ARMY PLACEMENT consists of these steps:
            1. Select a color and, depending on the number of players, count out the
            “armies” you’ ll need to start the game.
            If 2 are playing, see instructions on page 11.
            If 3 are playing, each player counts out 35 Infantry.
            If 4 are playing, each player counts out 30 Infantry.
            If 5 are playing, each player counts out 25 Infantry.
            If 6 are playing, each player counts out 20 Infantry.
            2. Roll one die. Whoever rolls the highest number takes one Infantry piece
            from his or her pile and places it onto any territory on the board, thus
            claiming that territory.
            3. Starting to the left of the first player, everyone in turn places one army
            onto any unoccupied territory. Continue until all 42 territories have
            been claimed.
            4. After all 42 territories are claimed, each player in turn places one
            additional army onto any territory he or she already occupies. Continue
            in this way until everyone has run out of armies. There is no limit to the
            number of armies you may place onto a single territory.
        To complete game SETUP:
            5. Shuffle the pack of RISK cards (remove the Mission cards) and place it,
            face down, by the side of the board. This pack forms the draw pile.
            6. Whoever placed the first army takes the first turn.
            
        PLAYING
        On your turn, try to capture territories by defeating your opponents’
        armies. But be careful: Winning battles will depend on careful planning,
        quick decisions and bold moves. You’ ll have to place your forces wisely,
        attack at just the right time and fortify your defenses against all enemies.
        Note: At any time during the game, you may trade in Infantry pieces for the
        equivalent (see page 4) in Cavalry or Artillery if you need to, or wish to.
        Each of your turns consists of three steps, in this order:
            1. Getting and placing new armies;
            2. Attacking, if you choose to, by rolling the dice;
            3. Fortifying your position.
        
        GETTING AND PLACING NEW ARMIES
        At the beginning of each turn, calculate how many new armies you’ ll add
        to your territories based on . . .
            1. The number of territories you occupy;
            2. The value of the continents you control;
            3. The value of the matched sets of RISK cards you trade in;
            4. The specific territory pictured on a traded-in card.
        
        Territories. At the beginning of every turn (including your first), count the
        number of territories you currently occupy, then divide the total by three
        (ignore any fraction). The answer is the number of armies you receive. Place
        the new armies on any territory you already occupy.
        
        Example: 11 territories = 3 armies
        14 territories = 4 armies
        17 territories = 5 armies
        You will always receive at least 3 armies on a turn, even if you occupy fewer
        than 9 territories.
        
        Continents. In addition, at the beginning of your turn you will receive
        armies for each continent you control. (To control a continent, you must
        occupy all its territories at the start of your turn.) To find the exact number
        of armies you’ ll receive for each continent, look at the chart in the lower
        left-hand corner of the game board.
        
        RISK CARDS
        Earning Cards. At the end of any turn in which you have captured at
        least one territory, you will earn one (and only one) RISK card. You are
        trying to collect sets of 3 cards in any of the following combinations:
            - 3 cards of same design (Infantry, Cavalry, or Artillery)
            - 1 each of 3 designs
            - any 2 plus a “wild” card
        If you have collected a set of 3 RISK cards, you may turn them in at the
        beginning of your next turn, or you may wait. But if you have 5 or 6 cards at
        the beginning of your turn, you must trade in at least one set, and may
        trade in a second set if you have one.

        Trading In Cards for Armies. At the beginning of subsequent turns,
        you may trade in matched sets of cards and take additional armies based on
        the total number of sets anyone has traded in so far. For quick reference,
        keep traded-in cards face down under the bottom edge of the game board
        to mark the value (in armies) of the next trade.
        
        The first set traded in - 4 armies
        The second set traded in - 6 armies
        The third set traded in - 8 armies
        The fourth set traded in - 10 armies
        The fifth set traded in - 12 armies
        The sixth set traded in - 15 armies
        
        After the sixth set has been traded in, each additional set is worth 5 more
        armies. Example: If you trade in the seventh set, you get 20 armies; if you
        trade in the eighth, you get 25 armies, and so on. “First” and “second” set,
        etc., refer to sets traded in by anyone during the game. Thus, if you trade in
        the third set in the game, you receive 8 armies, even if it’ s the first set you
        have traded in.
        Occupied territories. If any of the 3 cards you trade in shows the picture of
        a territory you occupy, you receive 2 extra armies. You must place both
        those armies onto that particular territory.
        Note: On a single turn, you may receive no more than 2 extra armies above
        and beyond those you receive for the matched sets of cards you trade in.
        Hints: No matter how many armies you receive at the start of your turn,
        deploy them carefully-either to prepare for an attack or to defend against
        one. It is good military strategy to move your armies to the front, heavily
        fortifying territories that border enemy territories.
        
        ATTACKING
        After placing your armies at the beginning of your turn, decide if you wish
        to attack at this time. The object of an attack is to capture a territory by
        defeating all the opposing armies already on it. The battle is fought by a roll
        of the dice. Study the board for a moment. Do you want to attack?
        If you choose not to attack, pass the dice to the player on your left. You
        may still fortify your position, if you wish (see page 10).
        If you choose to attack, you must follow these rules:
            - You may only attack a territory that’ s adjacent (touching) to one of your
            own, or connected to it by a dashed line. Examples: Greenland may
            attack the Northwest Territory, Ontario, Quebec and Iceland. North
            Africa may attack Egypt, Western Europe and Brazil. At the western and
            eastern edges of the board, Alaska is considered adjacent to, and may
            attack, Kamchatka.
            - You must always have at least two armies in the territory you’ re
            attacking from.
            - You may continue attacking one territory until you have eliminated all
            armies on it, or you may shift your attack from one territory to another,
            attacking each as often as you like and attacking as many territories as
            you like during one turn.
            
        To Attack. First announce both the territory you’ re attacking and the one
        you’ re attacking from. Then roll the dice against the opponent who
        occupies the opposing territory.
        Before rolling, both you and your opponent must announce the number
        of dice you intend to roll, and you both must roll at the same time.
        You, the attacker, will roll 1,2 or 3 red dice: You must have at least one
        more army in your territory than the number of dice you roll. Hint: The
        more dice you roll, the greater your odds of winning. Yet the more dice
        you roll, the more armies you may lose, or be required to move into a
        captured territory.
        The defender will roll either 1 or 2 white dice: To roll 2 dice, he or she
        must have at least 2 armies on the territory under attack. Hint: The more
        dice the defender rolls, the greater his or her odds of winning-but the
        more armies he or she may lose.
        
        To Decide a Battle. Compare the highest die each of you rolled. If yours
        (the attacker’ s) is higher, the defender loses one army from the territory
        under attack. But if the defender’ s die is higher than yours, you lose one
        army from the territory you attacked from; put it back in your clear plastic
        box. If each of you rolled more than one die, now compare the two
        next-highest dice and repeat the process.
        
        Notes:
            - * In case of a tie, the defender always wins.
            - The attacker can never lose more than 2 armies on a single roll.
       
        Capturing territories. As soon as you defeat the last opposing army on
        a territory, you capture that territory and must occupy it immediately. To
        do so, move in at least as many armies as the number of dice you rolled in
        your last battle. Remember: In most cases, moving as many armies as you
        can to the front is advantageous, because armies left behind can’ t help
        you when you are attacking. Also remember you must always leave at least
        one army behind on the territory you attacked from. During the game,
        every territory must always be occupied by at least one army.
        Ending your attack. You may end your attack(s) at any time. If you have
        captured at least one territory, first take the top RISK card from the draw
        pile. (No matter how many territories you’ ve captured on your turn, you
        may take only one RISK card.) Your last step is to fortify your position, if
        you wish (see below). Finally, pass the dice.
       
        Eliminating an opponent. If during your turn you eliminate an
        opponent by defeating his or her last army on the game board, you win any
        RISK cards that player has collected.
        If winning them gives you 6 or more cards, you must immediately trade
        in enough sets to reduce your hand to 4 or fewer cards, but once your
        hand is reduced to 4,3, or 2 cards, you must stop trading.
        But if winning them gives you fewer than 6, you must wait until the
        beginning of your next turn to trade in a set.
       
        Note: When you draw a card from the deck at the end of your turn (for
        having won a battle), if this brings your total to 6, you must wait until
        your next turn to trade in.
       
        FORTIFYING YOUR POSITION
        No matter what you’ ve done on your turn, you may, if you wish, end your
        turn by fortifying your position. You are not required to win a battle or even
        to try an attack to do so. Some players refer to this as the “free move.”
        To fortify your position, move as many armies as you’ d like from one (and
        only one) of your territories into one (and only one) of your adjacent
        territories. Remember to move troops towards borders where they can help
        in an attack!
        In moving your armies from one territory to another, you must leave at least
        one army behind.
       
        WINNING
        The winner is the first player to eliminate every opponent by capturing all
        42 territories on the board. 
       
        WORLD DOMINATION RISK®
        FOR 2 PLAYERS
        Read the complete World Domination rules first.
        This version is played like regular RISK with one important exception:
        Along with your armies and those of your opponent, there are also
        “neutral” armies on the board that act as a buffer between you and your
        opponent. This feature gives the 2-player version much the same strategic
        flavor as the regular RISK game.
        
        SETUP
        INITIAL ARMY PLACEMENT
        You and your opponent each select a complete set of armies. Then either of
        you selects a third set to be “neutral.” Take 40 Infantry pieces from each of
        the 3 sets and claim territories in the following manner:
            1. Remove the Secret Mission cards and the 2 “wild” cards from the RISK
            card deck. Shuffle thoroughly and deal the cards, face down, into 3 equal
            piles. Both you and your opponent choose a different pile. The
            remaining pile is “neutral.”
            2. Place one of your Infantry onto each of the 14 territdries shown on the
            RISK cards in your pile. Your opponent does the same. Then place one
            “neutral” Infantry onto each of the remaining 14 “neutral” territories.
            3. After every territory on the board has been claimed, you and your
            opponent take turns placing your remaining armies: Place 2 Infantry
            onto any 1 or 2 of the territories you occupy. Then place 1 “neutral”
            army onto any “neutral” territory you want, placing it to block your
            opponent’ s possible advance.
        To complete game SETUP:
            4. After all the armies have been placed on the board, return the two “wild”
            cards to the RISK card deck, shuffle the deck and start to play.
        
        ATTACKING
        On your turn, you may attack any territory adjacent to one of your own.
        Whenever you attack a “neutral” territory, your opponent rolls to defend
        that “neutral” territory.
        “Neutral” armies cannot attack and never receive reinforcements during
        the game.
        
        WINNING
        To win, be the first to eliminate your opponent by capturing all of his or her
        territories. You do not have to eliminate the “neutral” armies.
        Usually, all “neutral” armies are eliminated before the end of the game. If
        this happens, don’ t worry. Play continues until one player defeats the other.
        
        CAPITAL RISK
        FOR A SHORTER “WORLD DOMINATION” GAME
        
        OBJECT OF THE GAME
        To capture all opposing Headquarters-while still controlling your own
        territory.
        If you wish, you may shorten the game even further:
        4 players: Capture any 2 opposing Headquarters while controlling your
        own.
        5 or 6 players: Capture any 3 opposing Headquarters while controlling your
        own.
        
        EQUIPMENT
        Same as in World Domination Risk. Remember to remove the Secret
        Mission cards.
        
        SETUP
        1. After deploying your armies at the beginning of the game, select one of
        the territories you’ ve claimed and make it your Headquarters. Then,
        without revealing the territory you’ ve chosen, find its matching RISK
        card and place it face down in front of you.
        
        2. After everyone in turn has selected a Headquarters, all players turn their
        cards face up, thus revealing the location of their Headquarters.
        
        PLAYING
        All World Domination Risk Rules apply, with these additions:
            - If you capture an opposing Headquarters, place the Headquarters card
            you’ ve won face up in front of you to prove you’ ve captured it.
            - If at any point your Headquarters is captured by an opponent, you are
            not eliminated from the game. Simply give your card to that opponent
            and continue playing.
            - You may not use a Headquarters card as part of a matched set of RISK
            cards. Be sure to keep all Headquarters cards out of the way during the
            game.

        SECRET MISSION RISK
        for 3 to 6 players
        Read the complete World Domination rules first.
        
        OBJECT OF THE GAME
        To be the first player to complete the Mission described on your own
        Mission card. This game is suitable for from 3 to 6 players.
        
        EQUIPMENT
        Use all the equipment of the World Domination game, plus the 12 Mission
        cards. These cards give each player a different mission; when that mission
        has been completed, that player automatically wins the game.
        
        SETUP
        INITIAL, ARMY PLACEMENT
        1. Select a color and, depending on the number of players, count out the
        “armies” you’ ll need to start the game.
            If 3 are playing, each player counts out 35 Infantry.
            If 4 are playing, each player counts out 30 Infantry.
            If 5 are playing, each player counts out 25 Infantry.
            f 6 are playing, each player counts out 20 Infantry.
        To complete game SETUP:
        2. Before play begins, elect one player to be the General. If fewer than 6 are
        playing, the General removes the Mission cards that refer to the unused
        colors.
        3. The General shuffles the Mission cards and, starting to the left, deals one
        card face down to each player. The remaining Mission cards are put
        back in the box; no one, including the General, may look at them.
        4. The General removes the 2 Wild Cards from the deck of RISK cards,
        shuffles, and deals out all the cards, starting with the player to the left.
        (In a 4- or 5-player game, 2 players will each receive one extra card.)
        These cards determine which territories each of you will occupy at the
        beginning of the game.
        5. Each player places one army on each of his or her territories. When
        you’ ve done this, go around the table in turn, placing another army on
        each of your territories. There is no limit to the number of armies that
        can occupy a single territory. Continue until all troops have been
        deployed across the map.
        6. The General now collects the RISK cards, replaces the 2 Wild Cards,
        shuffles the deck, and puts it to the side, face down.
        7. Game play continues as in the standard World Domination game.
        
        WINNING
        The player who completes his or her mission first-and reveals the Mission
        card to prove it-wins.
        Important note: In Secret Mission RISK, it is possible that you will
        accomplish your mission with the aid (usually unintentional) of another
        player. For example, if your mission is to destroy all the yellow troops and
        another player actually removes the final yellow armies from the board,
        that player has helped you complete your Secret Mission.
        """,
    },
    
    "clue": {
        "name": "Clue",
        "category": "thematic games with randomness",
        "rules_text": """
        CLASSIC DETECTIVE GAME
        For 3 to 6 players / Ages 8 to adult
        
        Object
        Mr. Boddy— apparently the victim of foul play— is found in one of the rooms of
        his mansion. To win, you must determine the answers to these three questions:
        Who done it? Where? and with What Weapon?
        
        Equipment
        • Clue ® Game Board: This shows nine rooms in Mr. Boddy’ s mansion
        • 6 colored tokens, each representing one of the Suspects:
            Colonel Mustard— yellow; Miss Scarlet— red; Professor Plum— purple;
            Mr. Green— green; Mrs. White— white; and Mrs. Peacock— blue
        • 6 miniature weapons: Rope, Lead Pipe, Knife, Wrench, Candlestick, Revolver
        • Pack of cards: One card for each of the six Suspects, six Weapons and nine Rooms
        • Pad of detective “notebooks” to aid in your investigation
        • Confidential “Case File” envelope
        • 1 die
        Setup
        1. Look on the board for the START space and Suspect name nearest you. Take that
        Suspect token as your playing piece and put it on that space. If fewer than six are
        playing, be sure to place the remaining token(s) onto the appropriate name(s)—
        they might, after all, be involved in the crime, and they must be on the premises!
        2. Place each of the weapons in a different room. Select any six of the nine rooms.
        3. Place the empty envelope marked “Case File CONFIDENTIAL” onto the “X” in the
        center of the board.
        4. Sort the pack of cards into three groups: Suspects, Rooms and Weapons. Shuffle each
        group separately and place each face down on the table. Then— so no one can see
        them— take the top card from each group and place it into the envelope. The Case File
        now contains the answers to the questions: Who? Where? What Weapon?
        5. Shuffle together the three piles of remaining cards. Then deal them face down
        clockwise around the table. (It doesn’ t matter if some players receive more cards than
        others.) Secretly look at your own cards: Because they’ re in your hand, they can’ t be in
        the Case File— which means none of your cards was involved in the crime!
        6. Take a detective’ s notebook sheet and, so no one can see what you write, fold it in half:
        Check off the cards that are in your hand, if you wish.
        7. Miss Scarlet— the player with the red token— always plays first. Play then proceeds, in
        turn, to the first player’ s left.
        
        GAME PLAY
        Moving Your Token
        On each turn, try to reach a different room of the mansion. To start your turn, move your
        token either by rolling the die or, if you’ re in a corner room, using a Secret Passage:
        Rolling
        Roll the die and move your token the number of squares you rolled.
        • You may move horizontally or vertically, forward or backward, but not diagonally.
        • You may change directions as many times as your roll will allow. You may not,
        however, enter the same square twice on the same turn.
        • You may not enter or land on a square that’ s already occupied by another suspect.
        
        Secret Passages
        The rooms in opposite corners of the mansion are connected by Secret Passages.
        If you’ re in one of these rooms at the start of your turn, you may, if you wish, use a Secret
        Passage instead of rolling. To move through a Secret Passage, announce that you wish to
        do so, then move your token to the room in the opposite corner.
        Entering and Leaving a Room
        You may enter or leave a room either by rolling the die and moving through
        a door, or by moving through a Secret Passage.
        • A door is the opening in the wall, not the space in front of the doorway.
            When you pass through a door, do not count the doorway itself as a space.
        • You may not pass through a door that’ s blocked by an opponent’ s token.
        • As soon as you enter a room, stop moving. It doesn’ t matter if you roll
            a number that’ s higher than you need to enter.
        • You may not re-enter the same room on a single turn.
        • It is possible that your opponents might block any and all doors and trap
            you in a room. If this happens, you must wait for someone to move and
            un-block a door so you can leave!
        
        Making a Suggestion
        As soon as you enter a room, make a Suggestion. By making Suggestions throughout the
        game, you try to determine— by process of elimination— which three cards are in the
        confidential Case File envelope. To make a Suggestion, move a Suspect and a Weapon
        into the room that you just entered. Then suggest that the crime was committed in that
        Room, by that Suspect, with that Weapon.
        Example: Let’ s say that you’ re Miss Scarlet and you enter the Lounge. First move another
        Suspect— Mr. Green, for instance— into the Lounge. Then move a weapon— the Wrench,
        perhaps— into the Lounge. Then say, “I suggest the crime was committed in the Lounge
        by Mr. Green with the Wrench.”
        Remember two things:
            • You must be in the Room that you mention in your Suggestion.
            • Be sure to consider all tokens— including spare Suspects and including
                yourself!— as falling under equal suspicion.
        
        Proving a Suggestion True or False
        As soon as you make a Suggestion, your opponents, in turn, try to prove it false. The first
        to try is the player to your immediate left. This player looks at his or her cards to see if one
        of the three cards you just named is there. If the player does have one of the cards named,
        he or she must show it to you and no one else. If the player has more than one of the cards
        named, he or she selects just one to show you.
        If that opponent has none of the cards that you named, then the chance to prove your
        Suggestion false passes, in turn, to the next player on the left.
        As soon as one opponent shows you one of the cards that you named, it is proof that this
        card cannot be in the envelope. End your turn by checking off this card in your notebook.
        (Some players find it helpful to mark the initials of the player who showed the card.)
        If no one is able to prove your Suggestion false, you may either end your turn or make
        an Accusation now.

        Making an Accusation
        When you think you’ ve figured out which three cards are in the envelope, you may,
        on your turn, make an Accusation and name any three elements you want. First say,
        “I accuse (Suspect) of committing the crime in the (Room) with the (Weapon).”
        Then, so no one else can see, look at the cards in the envelope.
        In a Suggestion, the Room you name must be the Room where your token is located.
        But in an Accusation, you may name any room.
        Remember: You may make only one Accusation during a game.
        If Your Accusation Is Incorrect
        If any one of the cards that you named is not inside the Case File:
        • Secretly return all three cards to the envelope.
        • You may make no further moves in the game, and therefore cannot win, but you do
            remain involved in the investigation.
        
        • You do continue to try to prove your opponents’ Suggestions false.
        • Your opponents may continue to move your token into the various Rooms where
            they make Suggestions.
        • If after making a false Accusation your token is blocking a door, move it into that
            room so that other players may enter.
        
        Winning
        You win the game if your Accusation is completely correct— that is, if you find in the
        envelope all three of the cards that you named. When this happens, take out all three
        cards and lay them out for everyone to see.
        Special Notes About Suggestions
        1. When you make a suggestion, you may, if you wish, name one or more of the cards
            that you hold in your own hand. You might want to do this to gain information or to
            mislead your opponents.
        2. You may, if you wish, make a Suggestion and an Accusation on the same turn.
        3. You may make only one Suggestion after entering a particular room. To make your
            next Suggestion, you must either enter a different room or, sometime after your next
            turn, re-enter the room that you most recently left. You may not forfeit a turn to
            remain in a particular room. But if you’ re trapped in a room because your opponents
            are blocking the door(s), you must remain there until a door is unblocked and you
            can move out of the Room.
        4. You may make a Suggestion that includes a Suspect or Weapon that’ s already in your
            Room. In this case, transferring one or both of those items is not necessary. When a
            transfer is necessary, leave the item(s) in the new location after the Suggestion is made.
        5. If yours was the Suspect transferred, you may, on your next turn, do one of two things:
            Move from the Room in one of the usual ways OR Make a Suggestion for that room.
            If you decide to make a Suggestion, do not roll the die or move your token.
        6. There is no limit to the number of Suspects or Weapons that may be in one Room
            at one time.
        """,
    },
    
    "forbidden-island": {
        "name": "Forbidden Island",
        "category": "thematic games with randomness",
        "rules_text": """
        2-4 Players | Ages 10 and up
        Forbidden Island was the secluded retreat of an ancient mystical empire known as
the Archeans. Legend has it that the Archeans possessed the ability to control the
Earth’s core elements – fire, wind, water, and earth – through four sacred treasures: The Crystal
of Fire, The Statue of the Wind, The Ocean’s Chalice, and The Earth Stone. Because of their
potential to cause catastrophic damage if they fell into enemy hands, the Archeans kept the
treasures secretly hidden on Forbidden Island and designed it to sink if intruders ever attempted to
claim them. In the centuries since the mysterious collapse of their empire, Forbidden Island
remained undiscovered ... until now. Will your team be the first to breach its borders,
capture the treasures, and make it out alive?

Object
Your team of adventurers must work together to keep Forbidden Island from sinking, in order
to buy enough time to capture its four treasures. Once you’ve captured them, you must make it
to Fools’ Landing and escape by helicopter to win. If however, the island sinks before you can
complete your tasks, the mission ends in defeat!
Setup
1. Create Forbidden Island: Shuffle the 24 Island tiles and randomly
place them face up (non blue and white side) into a grid as follows: First make a 4 x 4 square
of tiles in the center of the playing area. Then place 2 tiles next to each of the 2 middle tiles on
every side of the square. (Important Note: Leave a small gap between the tiles.) This forms
Forbidden Island and your pawns will move on it like a game board.

2. Place the Treasures: Place the 4 treasure figurines – The Earth Stone,
The Statue of the Wind, The Crystal of Fire, and The Ocean’s Chalice – around the island.
Your team will try to capture these treasures during the course of the game by discarding 4
matching Treasure cards on a corresponding Island tile. Take a moment to locate the 8 tiles on
which you can claim treasures. Each treasure can be claimed on one of two tiles, as indicated
by the symbol in the bottom left corner: The Earth Stone, The Crystal of Fire, The Ocean’s Chalice, The Statue of the Wind.

3. Divide the Cards: Separate the cards into three decks according to card
back: Flood deck (blue back), Treasure deck (red back), and Adventurer cards (6 cards).

4. The Island Starts to Sink: Shuffle the Flood deck and place it face
down on one side of the island to form the Flood draw pile. Draw the top 6 cards (1 at a time)
and place them face up next to the draw pile to form the Flood discard pile. For each card
drawn, flip the corresponding Island tile over to its “flooded” (blue and white) side.

5. The Adventurers Appear:
Shuffle the 6 Adventurer cards and randomly deal 1 to each player. Each of you will take on the role of an adventurer with
a special power that only you can do during the game. Take a moment to read aloud your roles and powers written on the
bottom of the cards so that your teammates know your strengths. You’ll find the game will be easier to win if you cooperate and
take advantage of these special powers. Take a pawn matching the color of your Adventurer card and place it on the
corresponding Island tile. (Look for the matching pawn icon in the lower right corner of the Gates and Fools’ Landing tiles.) Put any extra Adventurer cards and
pawns back in the box. Note: It’s OK to start on a flooded tile.

6. Hand Out Treasure Deck Cards:
Thoroughly shuffle the Treasure deck and deal 2 cards to each player. Place your cards face up in front of you so that both
you and your teammates can easily see them. If anyone gets a Waters Rise! card, give them a replacement card and shuffle
the Waters Rise! card back into the Treasure deck. Place the Treasure deck face down by one side of the island. Note: There
will be a Treasure discard pile right next to the Treasure deck.

7. Set the Water Level: Place the Water Level marker
on the left side of the Water Meter and set it to the appropriate starting difficulty level, according to the type of game you want to play. (For example,
if this is your first time playing a cooperative game, set it to the Novice level.)

Note: You may look through both Treasure and Flood discard piles at anytime during the game.

Order of Play
The player who last visited an island goes first and play continues to the left. On every turn, do the following three things in order:
1. Take up to 3 actions.
2. Draw 2 Treasure deck cards.
3. Draw Flood cards equal to the water level.

The parts of each turn are described below. Also note that the back of every Adventurer card shows a quick reference guide.

1. Take Up to 3 Actions
You may take up to 3 actions each turn (could be 0, 1, or 2). Your teammates are allowed (and encouraged!) to give you advice on the best actions to take during your turn. Select a combination of any of the following 4 actions:
• Move
• Shore Up
• Give a Treasure Card
• Capture a Treasure

Move
You may, for 1 or more actions, move your pawn to an adjacent Island tile: either up, down, left, or right, but never diagonally. You may
move onto a flooded tile, but may not move onto (or over) the space of a missing tile.

Exceptions:
- The Explorer may also move diagonally.
- The Pilot may move to any tile once per turn for 1 action.
- The Navigator may move other players up to 2 adjacent tiles per action.
- The Diver may move through one or more adjacent missing and/or flooded tiles for 1 action.

Shore Up
You may, for 1 or more actions, shore up any adjacent Island tile (up, down, left, right), or the Island tile your pawn is on. To shore
up a tile, simply flip it over so its un-flooded side is facing up.

Exceptions:
- The Engineer may shore up 2 tiles for 1 action.
- The Explorer may also shore up tiles diagonally.

Give a Treasure Card
You may give 1 or more of your Treasure cards to another player if both of your pawns are on the same
island tile. It costs 1 action for each card you give away. (See “Hand Limit” for restrictions.) You may not give
Special Action cards.

Exceptions:
The Messenger may give cards without having to be on the same tile.

You may, for 1 action, capture a treasure by discarding 4 matching Treasure cards from your
hand if your pawn is on either corresponding island tile.

Notes
• When you capture a treasure, discard cards to the Treasure discard pile and move the figurine in front of you.
• You may capture a treasure on a flooded tile.

2. Draw 2 Treasure Deck Cards
After taking actions, you must draw 2 cards from the top of the Treasure deck and add them to your face up hand. Draw cards 1 at a time. If you draw a Waters Rise! card, do not add it to your hand, but follow the instructions on the card and then discard it to the Treasure discard pile.

Treasure Cards
There are 5 of each Treasure card in the Treasure deck. The aim is to collect 4 of the same Treasure card in order to find the
corresponding treasure of Forbidden Island. You can give Treasure cards to other players using the Give a Treasure Card action.

Special Action Cards
There are 2 types of Special Action cards in the Treasure deck – Helicopter Lifts (3) and Sandbags (2) – that will help your team during
the game. These cards are taken into your hand and can be played at any time — even on another player’s turn. Playing a Special Action
card does not require an action. Discard these cards to the Treasure discard pile immediately when played.

Note: You may use the power of a Special Action card if you are forced to discard it.

Waters Rise! Cards
There are 3 Waters Rise! cards in the Treasure deck. When you draw a Waters Rise! card, you must immediately do the following:
1. Move the Water Level marker up to cover the next tick mark on the Water Meter. Note how many cards will now be drawn at the end of
your turn by looking at the number on the right of the meter.
2. Take all of the cards from the Flood discard pile, shuffle them, and then place them face down on top of the Flood draw pile. This means
that previously drawn cards will be drawn again soon!
3. Discard the Waters Rise! card to the Treasure discard pile.

Notes:
• If you draw a Waters Rise! card, you do not get a replacement card.
• If you draw 2 Waters Rise! cards in a row, shuffle the Flood discard pile only once but move the Water Level marker up 2 tick marks.
• If you draw a Waters Rise! card but there are no cards in the Flood discard pile, just move the Water Level marker up 1 tick mark.

When the Treasure Deck Runs Out
When the last card of the Treasure deck is drawn, immediately shuffle the Treasure discard pile and turn it over to form a new Treasure deck.

Hand Limit
You may only have 5 cards in your hand, including Treasure and Special Action cards. If you ever find that you have 6 or more cards (for example because you drew more cards or received cards from another player) you must immediately choose and discard the excess to the Treasure discard pile. If you choose to discard a Special Action card, you may use its action before discarding.

3. Draw Flood Cards
After drawing 2 Treasure cards, you must now take on the role of Forbidden Island! Draw a number of cards from the top of the Flood draw pile equal to
the current Water Meter level. (For example, if the level is at 3, draw 3 cards.) Draw cards 1 at a time and place them face up onto the Flood discard pile. For each card drawn, find the matching Island tile and do one of the following:
• If the matching Island tile is un-flooded, flip it over to its flooded side.
• If the matching Island tile is already flooded, it sinks into the abyss! Remove it and the matching Flood card from the game and place them out of play.

Note: You cannot play a Sandbag card to save a flooded tile once you’ve revealed the matching Flood card.

Pawns on Flooded Tiles
If a pawn is on a tile that becomes flooded, lift the pawn off the tile, flip it and then return the pawn to the tile.
If a pawn is on a tile that must be removed, it must immediately “swim” to an adjacent tile (up, down, left, or right) that is still part of the island (even flooded). If a pawn is on a tile that is removed and cannot move to an adjacent tile, it sinks into the abyss and everyone loses the game!

Exceptions: The Diver may swim to the nearest tile. The Explorer may swim diagonally. The Pilot may fly to any tile.

When the Flood Draw Pile Runs Out
If the Flood draw pile ever runs out, immediately shuffle the Flood discard pile and stack the cards face down to form a new Flood draw pile. If this happens in the middle of a turn, continue drawing Flood cards as necessary from the new pile.

Game End
ù
Winning the Game
Get to Fools’ Landing! Once you have collected all four treasures, everyone must move their pawns to the Fools’ Landing tile. Then, one player must discard a Helicopter Lift
card to lift your team off of Forbidden Island for the win!
Note: You may win if Fools’ Landing is flooded.

Losing the Game
There are four possible ways to lose:
1. If both Temples, Caves, Palaces, or Gardens tiles sink before you collect their respective treasures.
2. If the Fools’ Landing tile sinks.
3. If any player is on an Island tile that sinks and there is no adjacent tile to swim to.
4. If the water level reaches the skull and crossbones.

Difficulty
Once you’ve won the Novice game, try starting the water level at the Normal, Elite, or
Legendary difficulty settings. Also, try playing with a different mix of adventurers.

A Word from Gamewright
It’s a great honor to introduce the latest creation by cooperative game master, Matt Leacock. There are so many things we love about this unique game: from the rich illustrations, to the collaborative nature of play, to the innovative set of rules, to the infinite possibilities generated
by the tiles and cards. Don’t be surprised if your pulse starts pounding faster soon after you start playing – it’s a game that instantly generates an electrifying atmosphere of tension and excitement!

        
        """,
    },
    
    "the-game-of-life": {
        "name": "The Game of Life",
        "category": "thematic games with randomness",
        "rules_text": """
Objective
Navigate life’s ups and downs—career, family, pets, and surprises—and be the wealthiest player by the end of the game.
The player with the most money after retirement wins!

Ages: 8+
Players: 2-4

Contents
- Gameboard with spinner
- 100 cards
- 5 Spin to Win tokens
- 4 cars
- 24 people pegs
- 12 pet pegs
- Money pack

Setup

Remove all pegs from their frame carefully (use an emery board or sandpaper if needed). Discard the frame.
Give each player:
- 1 car and matching Spin to Win token
- 1 pink or blue peg
- 1 pet peg
Separate the cards into five decks:
- House cards
- Action cards
- Career cards
- College Career cards
- Pet cards
Place them next to the board.
Choose a banker to handle salaries, bank loans, and cash.
Each player chooses a path:
- College: Pay $100K tuition; better chance at higher-paying careers.
- Career: Draw two Career cards, pick one as your job, and return the other to the bottom of the deck.
Pop pegs into your car and announce your pet’s name. You’re ready to start!

Gameplay
Turn Order: The youngest player goes first. Play proceeds to the left.

On Your Turn:
- Spin the spinner and move your car the number of spaces shown.
- Follow the instructions for the space you land on (see Board Spaces).
- Your turn ends, and the next player spins.

Board Spaces

Payday:
Pass a Payday space: Collect your salary from the bank.
Land on a Payday space: Collect salary plus $100K bonus.

Action:
Draw the top Action card, read it aloud, and follow the instructions. Keep the card; it’s worth money at the end of the game.

Spin to Win®:
Place tokens on the Spin to Win wheel numbers. Spin until a token number comes up—winner gets $200K!

Baby Spaces:
Add the indicated number of baby pegs to your car.

House Spaces:
Buy a house: Draw two House cards, pick one, pay the bank, and return the other to the deck. Multiple houses are allowed.
Sell a house: Spin the spinner; match the color in the center (red or black) to collect the sale price. Return the card to the deck.

Pet Spaces:
Draw a Pet card, read aloud, follow the instructions, and keep it for end-game scoring.

STOP! Spaces

Graduation STOP!
Draw two College Career cards, pick one, and place it face-up as your job. Spin again.

Get Married STOP!
Pop a peg in your car for your spouse. Spin for cash gifts: Red = $50K, Black = $100K. Spin again.

Night School STOP!
Change Career: Pay $100K, draw a College Career card, keep it if you like, return your old Career card. Spin again.
Keep Career: Spin again and continue on your path.

Family STOP!
Family Path: Spin again and add kids.
Life Path: Spin again and continue on the main path.

Risky STOP!
Risky Road: Spin again for chance to win or lose big.
Safe Route: Spin again along the safer path.

Out of Money?
Take a bank loan if needed. Each $50K borrowed = 1 loan certificate. Repay anytime with $60K per certificate. Unpaid loans are deducted from your final wealth.

Retirement

When you reach the Retirement space, choose:

Millionaire Mansion or Countryside Acres
Park your car and wait for other players. Collect retirement bonuses:
1st: $400K
2nd: $300K
3rd: $200K
4th: $100K
End of the Game

Sell your houses (spin for the value) and collect cash.
Collect $100K per Action card.
Collect $100K per Pet card.
Collect $50K per baby.
Subtract $60K per bank loan.
The wealthiest player wins!

Frequently Asked Questions (FAQ)

Can you win The Game of Life without a college degree?
Yes, but it’s harder. The benefits of a higher salary from having a college degree often make it easier to accumulate wealth, which is crucial for winning. However, depending on the strategy and other factors like Life tiles, you can still win by making smart financial moves.

How do Life tiles affect the outcome of the game?
Life tiles are crucial for your final score. Each tile is worth a random number of points (often ranging from 10,000 to 50,000). You earn Life tiles by making certain decisions in the game, like starting a family or pursuing certain career paths. Make sure to grab as many Life tiles as possible to maximize your chances of winning.

What happens if you run out of money?
Running out of money in The Game of Life doesn’t immediately end the game, but it can put you at a serious disadvantage. You might need to take out a loan or rely on financial decisions that could cost you in the long run. Keep track of your expenses and be cautious about your spending.

Can you change your career path?
Yes, in The Game of Life, you can change careers if you land on a specific space that allows it. This gives you a chance to increase your salary or improve your financial situation. However, you may need to give up a stable position to start a new career, so make sure it aligns with your goals.

What should I do if I have too many kids?
Having kids in The Game of Life gives you extra Life tiles and can be a great strategy for earning points. However, they also come with a cost. If you have too many kids early on, the added expenses can drain your finances. Be sure to weigh the potential bonuses against the financial burden of raising multiple children in the game.

Is The Game of Life purely based on luck?
While much of the game depends on the luck of the spin, your decisions, such as whether to go to college or when to retire, can influence your chances. Strategic moves can give you an edge, even though luck plays a significant role in determining your fate. 
        """,
    },
    
    "mafia": {
        "name": "Mafia",
        "category": "social/party games",
        "rules_text": """
        Game Core
Welcome to Mafia, a rite-playing game in which players become characters
suspected in having Mafia connections. Two teams: the Honest and the
Mafia will compete against each other. For the Honest team players, the
task is to stop Mafia before it eliminates them. Mafia members have to hide
their identity and pose as Honest players in order to manipulate the other
team players towards self-destruction. It is in each player’s best interest
to prove his or her innocence (or if you are a Mafia member, to hide your
guilt) by accusing and interrogating their fellow suspects, until all members
of the opposing team are eliminated from the game.
Pre-game Instructions
Prepare a deck of cards, paper, pencils and at least six players. When all
players have assembled, count how many people are in. From the deck,
take as many cards as there are players according to the following list:
6-7 players: 2 black cards + others red / 8-10 players: 3 black cards +
others red / 11-13 players: 4 black cards + others red / 14-16 players:
5 black cards + others red
Inform the players of the number of the black cards included.
Game schedule
Sunrise Phase: First step is to divide the players into two teams. Each
player gets one card from the prepared and shuffled deck, secretly looks
at the card’s color and returns the card to the deck. Then everybody
closes their eyes and lowers their heads. Someone starts counting aloud
(usually the person who dealt the cards). After number 5, s/he continues
to count silently until 15, then s/he resumes counting aloud until 20.
During the silent period, the players who got black cards, should open
their eyes, raise their heads, and look at each other, then close their eyes
and lower their heads again. On count 20, everybody should open their
eyes. Now, all players are divided into two teams. Mafia are the players
who saw each other and therefore know each other. Honest people are
the players who saw nothing, don’t know each other, and don’t know who
the Mafia members are. This is the only advantage of Mafia: they know
each other. Honest players have to suspect everybody, but they have an
advantage of being the majority. The main struggle during the next phase
will be between the informed minority and the uninformed majority.
Day Phase: Talk ... At any moment, any player may put another
player in the “suspected to be the Mafia” position. S/he should (better)
provide grounds for the suggestion. Everyone (including the accused)
has a right to argue. But when the accuser asks to vote, everyone should
vote by raising their hands. If the majority of the players (not counting
the accused) votes for “Guilty as member of the Mafia,” the suspected
player is “sentenced to death” and s/he is out of the game until the
end of the round. If the accuser fails to get the majority on her/his side,
the game continues with the same number of players. Accusations may
happen any number of times during the discussion. Players who are
eliminated from the game do not reveal their identity until the end of the
game and should not try to help others who are still in the game. There
is no way to know the team identity of the “dead” unless you have
the next phase.
Night Phase: This is the only phase when you can find out if all Mafia mem-
bers have been eliminated. So, once in a while, someone should propose
to have a “Mafia Night.” If the majority of the players who are still in the
game agrees, the Night begins. Everyone takes a pencil and a piece of
paper, and secretly writes on it. Honest people must write “honest” on
the note, while members of the Mafia must write the name of the person,
whom they want to eliminate from the game. After that, everybody puts
their notes in the middle and someone reads them. The number of the
notes with the names will reflect the number of survived Mafia members,
so the players will know if they have “killed” an Honest person or a Mafia
member during the day. If the same name appears on all Mafia notes,
the named person is “murdered” and is out of the game until the end of
the round. In any other case, the named players survive the Mafia attack
and the game continues with the same number of players.
For example, if three members of the Mafia are in the game, there should
be three notes with names on them. Only if all three notes have the same
name, that person is “murdered.” If only one member of Mafia is still in the
game, her/his single shot will be enough to eliminate somebody.
The game ends when there are no shots during Mafia Night or all Honest
people have been eliminated. Start again.
Pointers for the beginners
1. Players are free to introduce new procedures during the game, but
no one has to follow them unless s/he finds their usage at that moment
reasonable.
2. Accidental or purposeful peeking by red card holders during the
Sunrise Phase should be discouraged, however it will not give any
advantage during the game. The trick of the game is always to persuade
others to accept your knowledge and never to have the knowledge per
se. By the way, this is the reason for my reservations about including
different knowledge bearing characters (inspector, angel, seer). The only
knowledge in the game is Mafia connections, everything else is artificial.
3. Paper and pencils should be the same for everybody. Otherwise, it will
be easy to find who have written what during the Mafia Night.
4. For a new group, unless a clear leader emerges, the first round may
be a little slow. In the second round people who were unjustly eliminated
have enough drive to prevent it from happening again. The third game
is great without any reservations. If a group has someone who played
before, s/he should provide initial leadership from the beginning.
Scoring
If Mafia wins, each surviving Mafia player receives a number of points
equal to the initial number of the Honest players. If Honest wins, every
Honest player receives a number of points equal to the number of
surviving Honest players.
        """,
    },
    
    "werewolf": {
        "name": "Werewolf",
        "category": "social/party games",
        "rules_text": """
        1. GATHER PLAYERS
Werewolf is a great party game. You need at least 7 people to play. Gather up your village, and let's setup your
character deck.
An odd number of players works best, although it's not mandatory.
2. BUILD THE DECK
Every player gets a character card. You always have 1 Moderator, 1 Seer, 1 Doctor, and 2 Werewolves. The rest of the
players should all be Villagers.
Have more than 15 players? Add a Werewolf for every 4 players.
3. SHUFFLE & DEAL
Once you have a complete character deck, shuffle and deal them out face down. Each player should look at their card,
but they must keep it a secret.
Game Play
The game alternates between Night and Day rounds, starting with the Night. At the start of Night, the Moderator tells all
players, "Close your eyes." Everyone begins slapping their knees (or table) to cover up any noises of the Night. Then,
the moderator prompts the following characters to wake up one by one....
Werewolves
AWAKEN
The moderator says, "Werewolves, open your eyes" The Werewolves do so, and look around to recognize one another.
The Moderator should also note who the Werewolves are.
HUNT
The Moderator says "Werewolves, choose someone to kill" The Werewolves, while still slapping their knees, silently
agree on 1 person by pointing, all other players remain with their eyes closed.
SLEEP
When the Werewolves have agreed on a victim, and the Moderator understands who they picked, the Moderator says,
"Werewolves, close your eyes."
The Doctor
AWAKEN
The Moderator awakens the Doctor and says, "Doctor, who would you like to heal?" The Doctor can select anyone
they'd like to keep alive, hopefully not wasting their ability on a Werewolf.
HEAL
The Doctor points to who they'd like to heal, confirming with the Moderator. The person chosen, which could be
themself, will survive if the Werewolves chose the same player to kill.
SLEEP
After the Doctor confirms with the Moderator, the Doctor goes back to sleep. If someone was killed, and then saved by
the Doctor, the Moderator will let the Village know by saying, "Someone has been saved", at the beginning of the Day.
The Seer
AWAKEN
The moderator says "Seer, open your eyes. Seer, pick someone to ask about." The Seer opens their eyes and silently
points at another player.
SEE
The moderator silently signs thumbs-up if the seer pointed at a Werewolf, and thumbs-down if the Seer pointed at a
Villager.
SLEEP
The Seer now has information they can use to persuade the Village. The Moderator then says, "Seer, close your eyes"
and the Seer goes back to sleep.
DAYTIME
The moderator says, "Everybody open your eyes; it's now daytime" and then announces who has been killed (or saved)
last night. If someone was killed, that person is immediately out of the game, and they do not reveal their character.
INTRODUCTIONS
On the first day, go around and have everyone introduce themselves. For example, "Hey, I'm Matt. I'm the baker here in
town, and I'm a Villager." You do not have to give away your real identity.
DISCUSSION
Players discuss who they think are the Werewolves. Who's telling the truth or lying to survive? Characters may choose
to share or withhold information they've discovered, but but be careful, you may become a target.
ACCUSATIONS
If someone is accused, and the accusation is supported by a second player, the accused gets 30 seconds to defend
themselves, and then it's put up to a vote to decide their fate.
VOTING
After a player has had a chance to defend themselves, a vote is held to decide whether or not to kill off the player. A
majority vote is needed to do so. If not, the Village discussion continues.
TIME LIMIT
To keep the game moving along, you can put a time limit for reach day, and if the village doesn't chose someone to kill,
they miss their opportunity. Five minutes is recommend for daytime.
NIGHT FALL
Once a player is voted to be killed or the time limit has expired for the Day, Night begins again. If certain characters
have been killed off, they are still "woken up" in order to conceal their identities.
WINNING
VILLAGERS
The Villagers win and saved the Village if they kill all of the Werewolves.
WEREWOLVES
The Werewolves win if the number of Werewolves equal the number of Villagers left.
        """,
    },
    
    "dixit": {
        "name": "Dixit",
        "category": "social/party games",
        "rules_text": """
        Contents
- One game board inside the box (scoring track)
- 84 cards
- 36 voting tokens in 6 different colours numbered from 1 to 6
- 6 wooden rabbits (rabbeeples!)

Setup
Each player chooses one rabbit and place it on the space 0 of the scoring track. Shuf-
fle the 84 images and give 6 of them to each player. Make a draw pile with the re-
maining cards.
- With 4 players, each one takes 4 voting tokens (from 1 to 4).
- With 5 players, each one takes 5 voting tokens (from 1 to 5).
- With 6 players, each one takes 6 voting tokens (from 1 to 6).
Note: Do not show your hand of cards to anyone.
Game turn
The storyteller
One player is the storyteller for the turn. He looks at the 6 images in his hand. From one
of these, he makes up a sentence and says it out loud (without showing the card to the
other players).
The sentence can take different forms: it can be made of one word or more, it can even
be a sound. The sentence can be either invented or be inspired from an existing work
of art (poetry or song sample, movie title, proverb, etc).
Who is the storyteller for the first turn? The first player to describe one of their cards
aloud will be the storyteller for the first turn.
Choosing a card for the storyteller
The other players select amongst their 6 images the one that best matches the
sentence made up by the storyteller.
Then, each of them gives their selected card to the storyteller, without showing it to the others.
The storyteller shuffles his card with all the received cards. He then randomly places
them face up on the table. The card on the left will be number 1, the one next to it will
be number 2, and so on…
Finding the storyteller’s image: the vote
The goal of the other players is to find which image is from the storyteller amongst the
displayed ones. Each player secretly votes for the card that he believes belongs to the
storyteller (who doesn’t vote).
To do so, he places face down in front of him the voting token corresponding to the
image he voted for. Once everybody has voted, all the voting tokens are revealed
and placed on their corresponding images.
Note: You’re not allowed to vote for your own image.
Scoring
- If all players have found the storyteller’s image, or if none have found it, then the
storyteller doesn’t score any points and everyone else scores 2 points.
- In any other case, the storyteller scores 3 points and so do the players who found
his image.
- Each player, except the storyteller, scores one point for each vote that was placed
on their image.
The players move their rabbits along the scoring track by the same number of spaces
as points scored.
End of turn
Each player draws a new card to bring their hand up to 6 once more. The storyteller
for the new turn is the player to the left of the current one (and we keep going clock-
wise for the following turns).
Game end
The game ends when the last card from the pack has been drawn. The player who’s
the furthest on the scoring track is the winner..
Game Tips
If the sentence given by the storyteller describes the image too precisely, all the play-
ers will easily find it and so he won’t score any points.
On the other hand, if his sentence has very little to do with the image, it’s quite likely
that nobody will vote for him, and again he will score no points.
So the challenge for the storyteller is to find a sentence that is neither too descriptive,
nor too abstract, so that there is a chance that only some players find it, but not all.
At the beginning, this can be fairly hard to achieve, but you’ll see that the inspiration
comes more easily after a few turns.
Variants
3 players: each player has 7 cards, instead of 6. Every player except the storyteller
gives 2 cards, instead of one. So we end up with 5 displayed cards to choose from.
Scoring: When only one player has found the storyteller’s card, they both score 4
points, instead of 3.
Mimes or songs: in this variant, the storyteller has the possibility to either sing a
song or some music that could be somehow related to the card, or even mime it. The
rest of the game stays the same.
Finally, nothing prevents you from mixing the different variants together or creating
some of your own!
        """,
    },
    
    "codenames": {
        "name": "Codenames",
        "category": "social/party games",
        "rules_text": """
        SETUP
Players split up into two teams of similar
size and skill. You need at least four
players (two teams of two) for a standard
game. Variants for two or three players
can be found on the back page.
Each team chooses one player to be
their spymaster. Both spymasters sit on
the same side of the table. The other
players sit across from their spymasters.
They are field operatives.
Randomly choose 25 codenames and
place them on the table in a 5-by-5 grid.
Note: While shuffling the codename
cards, be sure to flip over half the deck
once in a while. This will mix the words
more thoroughly.
THE KEY
Each game has one key that reveals the secret identities of the cards on the table. The spymasters
should choose the key card randomly and slide it into the stand between them. Any side can be up.
Don't think about it. Just slide it into the stand. And don't let the field operatives see it.
The key corresponds to the grid on the table. Blue squares correspond to words that Blue Team must
guess (blue agents). Red squares correspond to words that Red Team must guess (red agents). Pale
squares are innocent bystanders, and the black square is an assassin who should never be contacted at all!
STARTING TEAM
The four lights around the edge of the key card indicate which team starts. The starting
team has 9 words to guess. The other team has 8. The starting team will give the first clue
of the game.
AGENT CARDS
8 red agents 8 blue agents
The red agent cards go in a stack in
front of the red spymaster. The blue
agent cards should be in front of the
blue spymaster. This helps everyone
remember which team they are on.
1 double agent
The double agent belongs to whichever
team starts. Flip it to that team's color.
It will be one of that team's agent cards
for the duration of the game.
7 innocent bystanders 1 assassin
The innocent bystander cards and the
assassin should be kept in between,
where both spymasters can reach them
easily.
GAME OVERVIEW
Spymasters know the secret identities of 25 agents. Their teammates know the agents only by their
codenames.
Spymasters take turns giving one-word clues. A clue may relate to multiple words on the table. The field
operatives try to guess which words their spymaster meant. When a field operative touches a word, the
spymaster reveals its secret identity. If the field operatives guess correctly, they may continue guessing,
until they run out of ideas for the given clue or until they hit a wrong person. Then it is the other team's
turn to give a clue and guess. The first team to contact all their agents wins the game.
GAME PLAY
Teams take turns. The starting team is indicated by the 4 lights on the edges of the key card.
GIVING A CLUE
If you are the spymaster, you are trying to think of a one-word clue that relates to some of the words
your team is trying to guess. When you think you have a good clue, you say it. You also say one
number, which tells your teammates how many codenames are related to your clue.
Example: Two of your words are NUT and BARK. Both of these grow on trees, so you say tree: 2 .
You are allowed to give a clue for only one word (cashew: 1 ) but it's fun to try for two or more. Getting
four words with one clue is a big accomplishment.
One Word
Your clue must be only one word. You are not allowed to give extra hints. For example, don't say,
"This may be a bit of a stretch…" You are playing Codenames. It's always a bit of a stretch.
Your clue cannot be any of the codenames visible on the table. On later turns, some codenames will
be covered up, so a clue that is not legal now might be legal later.
MAKING CONTACT
When the spymaster gives a clue, his or her field operatives try to figure out what it means. They can
debate it amongst themselves, but the spymaster must keep a straight face. The operatives indicate
their official guess when one of them touches one of the codenames on the table.
• If the field operative touches a card belonging to his or her team, the spymaster covers the word
with an agent card in that color. The operatives get another guess (but not another clue).
• If the field operative touches an innocent bystander, the spymaster covers it with an innocent
bystander card. This ends the turn.
• If the field operative touches a card belonging to the other team, the word is covered by one of
the other team's agent cards. This ends the turn. (And it helps the other team.)
• If the field operative touches the assassin, the word is covered by the assassin card. This ends the
game! The team that contacted the assassin loses.
Tip: Before saying your clue out loud, make sure it doesn't relate to the assassin.
Number of Guesses
The field operatives must always make at least one guess. Any wrong guess ends the turn
immediately, but if the field operatives guess a word of their team's color, they can keep guessing.
You can stop guessing at any time, but usually you want to guess as many words as the spymaster
said. Sometimes you might even want to guess one more:
Example: Red Team's first clue was tree: 2 . The red operative wanted to guess ORANGE and NUT.
She guessed ORANGE first. That was an innocent bystander, so she did not get a chance to guess NUT.
Blue Team took a turn and correctly guessed two words. Now it is Red Team's turn again.
The red spymaster says river: 3 . The red operative is pretty sure the AMAZON is a river, so she touches
that card. The spymaster covers it with a red agent card, so she gets to go again. A river has a BED,
so she touches that codename. It's also red, so she can go again.
She's not sure of the third river word. She picks
NUT. This has nothing to do with river . She is
guessing a word from the previous clue.
NUT is a red word. The operative has made
3 correct guesses for the clue river: 3 . She is
allowed one final guess. She can try to find the
third river word, or she can try to find the other
tree word. Or she can stop at three and let Blue
Team have a turn.
You are allowed only one extra guess. In the
example above, the red operative would be
allowed 4 guesses because her spymaster said
the number 3 . When the field operatives say
they are done guessing (or when they guess
wrong) it is the other team's turn.
GAME FLOW
Spymasters take turns giving clues. After
a spymaster gives a clue, his or her team starts
guessing. Their turn ends when they guess
wrong, when they decide to stop, or when they
have made the maximum number of guesses
for that clue. Then it is the other team's turn.
ENDING THE GAME
The game ends when one team has all their
words covered. That team wins.
It is possible to win on the other team's turn if
they guess your last word.
The game can end early if a field operative
makes contact with the assassin. That
operative's team loses.
Setup for the Next Game
Do other people want a chance to be
spymasters? Setup for the second game
is easy. Remove the cards covering the
codenames and put them back in their stacks.
Now just flip over the 25 codenames, and
you're ready to go!
PENALTY FOR INVALID CLUES
If a spymaster gives an invalid clue, the
team's turn ends immediately. As an additional
penalty, the other team's spymaster may cover
one of his or her words with an agent card
before giving the next clue.
But if no one notices that a clue is invalid, it
counts as valid.
KEEPING A STRAIGHT FACE
The spymaster is expected to keep a straight
face. Do not reach for any card while your
teammates are considering the words. When
a teammate touches a word, consult the key
card and cover the word with the card of
the corresponding color. When a teammate
chooses a word of the correct color, you
should act as though it was exactly the word
you meant, even if it wasn't.
If you are a field operative, you should focus
on the table when you are making your
guesses. Do not make eye contact with the
spymaster while you are guessing. This will
help you avoid nonverbal cues.
When your information is strictly limited to
what can be conveyed with one word and one
number, you are playing in the spirit of the game.
WHAT'S THE TIMER FOR?
Sorry. We almost forgot. You see, we don't
use the sand timer very often.
If a player is thinking too long, any player can
flip the sand timer and ask the slow player to
make a decision before time runs out.
If you are having trouble, you can even use
the sand timer on yourself. If you can't find
a good clue before time runs out, just give
a clue for your hardest word and keep thinking
while the other team plays.
If you prefer to play with strict time
limits, you can download our timer app at
codenamesgame.com.
VALID CLUES
We playtested various rules. Some groups like the rules one way. Some like the rules another way.
You should experiment to find out what your group likes.
FIRM RULES
Some clues are invalid because they violate the
spirit of the game.
Your clue must be about the meaning of the
words. You can't use your clue to talk about
the letters in a word or its position on the table.
Gland is not a valid clue for ENGLAND. You
can't tie BUG, BED, and BOW together with
a clue like b: 3 nor with a clue like three: 3 .
However …
Letters and numbers are valid clues, as long
as they refer to meanings. You can use X: 1 as
a clue for RAY. You can use eight: 3 as a clue
for BALL, FIGURE, and OCTOPUS.
The number you say after your clue can't be
used as a clue. Citrus: 8 is not a valid clue for
LEMON and OCTOPUS.
You must play in English. A foreign word is
allowed only if the players in your group would
use it in an English sentence. For example,
you can't use Apfel as a clue for APPLE and
BERLIN, but you can use strudel .
You can't say any form of a visible word
on the table. Until BREAK is covered up by
a card, you can't say break , broken , breakage ,
or breakdown .
You can't say part of a compound word on the
table. Until HORSESHOE is covered up, you
can't say horse , shoe , unhorsed , or snowshoe .
HOMONYMS & SPELLING
English has a lot of homonyms. For example,
night sounds like knight , but these two words
don't mean the same thing.
Same-sounding words with different
meanings and different spellings are
considered different words. So you can't give
knight -related clues for NIGHT.
Words that are spelled the same are
considered the same even though they might
have different pronunciations and meanings.
For example, actors take a bow and the bow is
part of a ship, so you could use bow as a clue
for THEATER and SHIP. You could also use it as
a clue for archery-related things, even though
that bow is pronounced differently.
You are allowed to spell out your clue. For
example, if you want your teammates to guess
THEATER and STRING, you can spell out b-o-w
without committing to a pronunciation. You can
give the clue k-n-i-g-h-t even when NIGHT is
one of the codenames on the table. (But you
can't use t-h-e-a-t-r-e when THEATER is on
the table. Theatre and theater are different
forms of the same word.)
You should spell out your clue if someone
asks. If you aren't that strong on spelling, ask
the opposing spymaster for help.
Tip: Spelling is not just for homonyms. It's also
useful when the room is noisy or when the
players have very different accents.
DON'T BE TOO STRICT
England and island were originally compound words, but in this century, island is a valid clue for
ENGLAND. Even land is a valid clue for ENGLAND. And anybody who says you can't say sparrow when
ROW is on the table is just trying to cause trouble.
If the opposing spymaster allows it, the clue is valid. If you aren't sure, ask your opponent. (Quietly,
so the others can't hear.)
FLEXIBLE RULES
Sometimes you have to make judgment calls
about what is valid and what is not. Different
groups may prefer to play the game differently.
Compound Words
English has three ways to write a compound
word. Greenhouse is one word. Pack rat is two
words. Mother-in-law is hyphenated. Technically,
only greenhouse can be a one-word clue.
You can decide to allow any compound words.
However, in no case should a player be allowed
to invent compound words. Lunar squid is not
a valid clue for MOON and OCTOPUS.
Proper Names
Proper names are always valid clues if they
follow the other rules. George is a valid clue, but
you might want to specify whether you mean
George Washington or George W. Bush . Your
group can agree to count proper names as one
word. This would also allow titles such as The
Three Musketeers . Even if you don't allow multi-
word proper names, you might want to make an
exception for place names like New York .
Spymasters should not be allowed to make up
names, not even names that turn out to be
real. Sue Mee is not a valid clue for CHINA and
LAWYER.
Acronyms and Abbreviations
Technically, CIA is not one word. But it is
a great clue. You can decide to allow common
abbreviations like UK , lol , and PhD . And words
like laser , radar , and sonar are always allowed,
even though they originated as acronyms.
Homonyms
Some people prefer to allow a more liberal use
of homonyms. You can allow knight to be a clue
for night -related things if that makes the game
more fun for you.
Rhymes
Rhymes are always valid when they refer to
meanings. Snail is a valid clue for MAIL because
this rhyme is a common phrase. Snail is also
a valid clue for WHALE because they are both
animals. Snail is not a valid clue for SCALE
because their main association is through the
sound of the words. (If someone in your group
has a job weighing snails, however, this clue is
perfectly fine.)
Some people like to allow any kind of rhyming
clue. If you decide to allow this, just remember
that you aren't allowed to indicate you are giving
a rhyming clue. Your operatives will have to
figure that out for themselves.
EXPERT CLUE: ZERO
You are allowed to use 0 as the number part
of your clue. For example, feathers: 0 means,
"None of our words relate to feathers ."
If 0 is the number, the usual limit on guesses
does not apply. Field operatives can guess
as many words as they want. They still must
guess at least one word.
If you're not sure why this is useful, don't
worry. You'll figure it out.
EXPERT CLUE: UNLIMITED
Sometimes you may have multiple unguessed
words related to clues from the previous
rounds. If you want your team to guess more
than one of them, you may say unlimited
instead of a number. For example feathers:
unlimited .
The disadvantage is that the field operatives
do not know how many words are related to
the new clue. The advantage is that they may
guess as many words as they want.
TWO-PLAYER GAME
If there are only two of you, you can play on the same team. This two-player variant also works for
larger groups of people who don't feel like competing against each other. You will try to get a high
score against a simulated opponent.
Set up the game as usual. One player will be the spymaster and the rest will be field operatives.
The other team has no players, but you still need their stack of agent cards.
Your team should go first, so be sure to pick a key
card that makes you the starting team.
Play your turns as usual. Try to avoid enemy agents and the assassin.
The spymaster simulates the enemy team by covering
up 1 of their words each time they get a turn. The
spymaster gets to choose which word is covered, so
there is a bit of strategy here.
If your team contacts the assassin, or if all the enemy
agents are contacted, you lose. There is no score.
If your team wins, give yourselves a score based on how
many agent cards are still left in the enemy's stack.
Note: Your score will be determined by how many turns you needed and also by how many enemy
agents you contacted accidentally.

8 That is … difficult to believe.
7 Mission impossible.
6 Wow!
5 MI6 will be giving you a call.
4 Top secret clearance.
3 Your watches are synchronized.
2 Okay. But you can do better.
1 Well, a win is a win, right?

THREE-PLAYER GAME
Three players who want to be on the same team can play as described above. If two players want
to compete against each other, they can be spymasters and the third player can be their operative.
Setup and game play are as usual, except that the single field operative is working for both sides.
(Just like spies in real life!) The winning spymaster is determined in the usual way. The field operative
tries to do a good job for both sides.
        """,
    },
    
    "the_resistance": {
        "name": "The Resistance",
        "category": "social/party games",
        "rules_text": """
        Contents:
11 Character Cards (10 Characters & 1 Leader)
5 Team Cards
20 Vote Cards (10 Approve & 10 Reject Cards)
10 Mission Cards (5 Success & 5 Failure Cards)
15 Plot Cards (Cards used in “The Plot Thickens” expansion)
6 Score Markers (3 Blue & 3 Red Markers)
1 Round Marker (Black disc)
Score Tableau
Objective:
The Resistance is a social deduction game with secret identities. Players
are either members of the Resistance attempting to overthrow a malignant
government, or Spies trying to thwart the Resistance. The Resistance wins
the game if three Missions are completed successfully; the Spies win if
three Missions fail. The Spies can also win if the Resistance is unable to
organize the Mission Team at any point in the game (5 failed votes on a
single mission).
A fundamental rule of the game is that players may say anything that they
want, at anytime during the game. Discussion, deception, intuition, social
interaction and logical deductions are all equally important to winning.
The Cards:
Character Cards - Determine the player’s affiliation (each player is either
a resistance operative or a spy). A player’s Character Card may not be
revealed at any point in the game, nor the character art discussed.
Leader Card - Designates the players that will form the Mission Team.
Team Cards - Allocate positions on the Mission Team.
Vote Cards - Approve or reject the Leader’s Mission Team.
Mission Cards - Determine Mission success or failure.
Plot Cards - Additional actions used in “The Plot Thickens” expansion.
Set Up:
Place the tableau in the center of the play area with the Score Markers, Team
cards and Mission cards adjacent to the Tableau. Place the Round marker on
the Tableau’s 1st Mission space. Give each player a set of two Vote cards.
Randomly select a Leader; the Leader receives the Leader card. Use the chart
below to determine the number of Resistance Operatives and Spies that will be
in the game.
Players 5 6 7 8 9 10
Resistance 3 4 4 5 6 6
Spies 2 2 3 3 3 4
Shuffle the appropriate numbers of Character cards. Deal one card to each
player face down. Each player secretly looks at the role assigned to them on the
Character card.
Spies Reveal:
After all the players know their affiliation, the Leader must ensure that all
the Spies know one another by repeating the following script:
“Everyone close your eyes”
“Spies open your eyes. Spies look around and make sure that you know
all the other Spies”
“Spies close your eyes. Everyone’s eyes should be closed.”
“Everyone open your eyes.”
Game Play:
The game consists of several Rounds; each Round is comprised of a Team
building phase and a Mission phase.
Build the Team
The team building phase consists of the Leader picking the players that he
would like on the Mission Team followed by all the players voting to
approve/reject the Mission Team.
Mission Team Assignment: After appropriate discussion, the Leader takes
the required number of Team cards (using the chart below) and assigns each
Team card to any player including himself. Note a player may only be
assigned one Team card.
Players 5 6 7 8 9 10
1st Mission Team 2 2 2 3 3 3
2nd Mission Team 3 3 3 4 4 4
3rd Mission Team 2 4 3 4 4 4
4th Mission Team 3 3 4 5 5 5
5th Mission Team 3 4 4 5 5 5
Mission Team Vote: After appropriate discussion, the Leader calls for a vote
on the Team assignments. Each player, including the Leader, secretly selects
one Vote card. When all players have their selected Vote card ready, the
Leader asks for the Votes to be revealed. The Mission Team is approved
if the majority of Votes are affirmative and fails if a majority rejected the
assignments; a tied vote is also a rejection. If the Mission Team is approved,
play continues in the Mission phase. If the Mission Team is rejected,
the Leader passes in a clockwise manner and the Team building phase is
repeated.
The Spies win the game if five Mission Teams are rejected in a single
round (5 failed Votes).
Example: The Leader passes
Team cards to Paul (himself)
and Charles, then calls for the
Vote.
Example: Paul, Charles, Candice
and Ian Approve, Ralph Rejects -
the Vote is approved, play continues
in the Mission Phase.
Conduct the Mission
Each player on the Mission Team must secretly decide to either support or
sabotage the Mission. The Leader passes a set of Mission Cards to each Mission
Team member. Each player on the Mission selects a Mission Card and plays
it face down in front of themselves. The Leader collects and shuffles the played
Mission Cards before revealing. The Mission is successful only if all the Cards
revealed are Mission Success cards. The Mission fails if one (or more) Mission
Fail cards have been played.
Note: The Resistance Operatives must select the Mission Success card; Spies may
select either the Mission Success or Mission Fail card.
Note: The 4th Mission in games of 7 or more players requires at least two Mission
Fail cards to be a failed mission.
Note: It’s suggested that two different players shuffle the played and discarded
Mission cards before revealing.
After the Mission has been completed, advance the Round marker to the next
Mission space on the Tableau. Indicate a Mission Success with a Blue Marker
or Mission Fail with a Red Marker in the Mission Space. The Leader passes in
a clockwise manner and the Team building phase of the next Round begins.
Example: Paul gives
himself and Charles a
set of two Mission cards.
Paul selects the Mission
Success card and places
it face down in front
of him, Charles places
the Mission Fail card
face down in front of
himself.
Paul takes the two Mission cards and shuffles them
before revealing that the Mission failed.
Game End:
The game ends immediately after either three successful or three failed
Missions. The Resistance wins if three Missions are successful. The Spies win if
three Missions fail.
Notes:
Information in The Resistance comes at multiple levels. First are players’ voting
patterns, second are Mission results, and third are cues that you can discern
from player interactions. Resistance Operatives must use all the information at
hand to root out the Spy infestation.
It’s not easy to overthrow a powerful government. You can expect the Spies
will win a significant proportion of the time with the core game rules,
particularly when played with more than 7 players. The Plot cards in the “The
Plot Thickens” expansion (included) provide additional information for the
Resistance Operatives, and opportunities for the Spies to be more deceitful.
Variants:
The Resistance is a game highly dependent upon the group playing it, feel free
to experiment with different variants. Two popular variants are:
Targeting - The Leader proposes both the Mission and the Team. Each
Mission can only be attempted once and the 5th Mission can only be
attempted after two Missions have been successful.
Blind Spies - Skip the Spies Reveal Step
Additional details on these and many other variants can be found at
www.IndieBoardsAndCards.com
        """,
    },  
}