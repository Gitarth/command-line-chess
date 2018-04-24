Computer Science 470
======================
chessAi
----------------------

A python program to play chess against an AI in the terminal.

## Task 1
For this task, first I created a play_game.py file and copied main.py over to it. Then I edited the method startGame(board, playerSide, ai); I commented out a section and added 
 ```python
 if board.currentSide == playerSide:
            # printPointAdvantage(board)
            # move = None
            # command = input("It's your move."
            #                 " Type '?' for options. ? ")
            # if command.lower() == 'u':
            #     undoLastTwoMoves(board)
            #     continue
            # elif command.lower() == '?':
            #     printCommandOptions()
            #     continue
            # elif command.lower() == 'l':
            #     printAllLegalMoves(board, parser)
            #     continue
            # elif command.lower() == 'r':
            #     move = getRandomMove(board, parser)
            # elif command.lower() == 'exit' or command.lower() == 'quit':
            #     return
            try:
                # Calling the the getRandomMove so the player input is random.
                move = getRandomMove(board, parser)
            except ValueError as error:
                print("%s" % error)
                continue
            makeMove(move, board)
```

