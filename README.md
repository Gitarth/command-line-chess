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

