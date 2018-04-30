Computer Science 470
======================
chessAi
----------------------

A python program to play chess against an AI in the terminal.

## Task 1
For this task, first I created a play_game.py file and copied main.py over to it. Then I edited the method startGame(board, playerSide, ai); I commented out a section and added 
 ```python
 if board.currentSide == playerSide:
            try:
                # Calling the the getRandomMove so the player input is random.
                move = getRandomMove(board, parser)
            except ValueError as error:
                print("%s" % error)
                continue
            makeMove(move, board)
```

## Task 2 
For this task, I implemented an alpha-beta pruning algorithm. The algorithm accepts a couple of new parameters such as alpha, beta and depth. Using these parameters, it then does pruning to get rid of moves that are bad. First I made an instance of the AI.py class. Using this instance I generated a moveTree, and using the moveTree I got all the bestLegalMoves. The idea I am approaching here is that, the agent iterates all the possible moves in the legalBestMoves, and for each moves, it iterates over all the legalMoves. I then create two nested functions within it, `def alphaBetaMax(...)` and `def alphaBetaMin(...)`. Each of these functions take in an alpha, beta, and depth. Each function has a var value that is initialize. Then I check for the base case, being 
```python
if (depth == 0 or board.isCheckmate or board.isStalemate):
    return (board.getPointAdvantageOfSide(board.currentSide),)
```
Once the base case is set, all the agent needs to do is iterate over all the possible legalBestMoves and since its recursive it'll grow until the base case is hit and then return the points of the agents side. Once the agent has the values, it will start pruning and finding the bestMove from the list legalBestMoves. I tend to shuffle up the list so that its not predictable everytime. Unfortunately, it seems to always be either a stalemate or a loss. The method returns a tuple of `(score, action)` where score is value and action is the bestMove.
