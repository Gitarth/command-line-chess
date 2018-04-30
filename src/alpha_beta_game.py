from Board import Board
from InputParser import InputParser
from AI import AI
import sys
import random

import math as Math
import pdb

WHITE = True
BLACK = False


def askForPlayerSide():
    playerChoiceInput = input(
        "What side would you like to play as [wB]? ").lower()
    if 'w' in playerChoiceInput:
        print("You will play as white")
        return WHITE
    else:
        print("You will play as black")
        return BLACK


def askForDepthOfAI():
    depthInput = 2
    try:
        depthInput = int(input("How deep should the AI look for moves?\n"
                               "Warning : values above 3 will be very slow."
                               " [n]? "))
    except:
        print("Invalid input, defaulting to 2")
    return depthInput


def printCommandOptions():
    undoOption = 'u : undo last move'
    printLegalMovesOption = 'l : show all legal moves'
    randomMoveOption = 'r : make a random move'
    quitOption = 'quit : resign'
    moveOption = 'a3, Nc3, Qxa2, etc : make the move'
    options = [undoOption, printLegalMovesOption, randomMoveOption,
               quitOption, moveOption, '', ]
    print('\n'.join(options))


def printAllLegalMoves(board, parser):
    for move in parser.getLegalMovesWithNotation(board.currentSide, short=True):
        print(move.notation)


def getRandomMove(board, parser):
    legalMoves = board.getAllMovesLegal(board.currentSide)
    randomMove = random.choice(legalMoves)
    randomMove.notation = parser.notationForMove(randomMove)
    return randomMove

def getAlphaBetaMove(board, parser):
    import MoveNode as MoveNode
    depth = 1
    AIagent = AI(board, True, depth)
    legalMoves = board.getAllMovesLegal(board.currentSide)
    bestMove = None
    moveTree = AIagent.generateMoveTree()
    legalBestMoves = AIagent.bestMovesWithMoveTree(moveTree)

    def alphaBetaMax(alpha, beta, depth):
        global bestMove
        value = -float(999999)
        if (depth == 0):
            return (board.getPointValueOfSide(board.currentSide),)
        random.shuffle(moveTree)
        for move in moveTree:
            #for m in legalMoves:
            if (move in legalBestMoves):
                value = max(value, alphaBetaMin(alpha, beta, depth - 1)[0])
                if (value >= beta):
                    return beta, move.move
                if (value > alpha):
                    alpha = value
                    bestMove = move.move
                    bestMove.notation = parser.notationForMove(bestMove)
        #return {'alpha': alpha, 'bestMove': bestMove}
        return alpha, bestMove
        #return bestMove
    
    def alphaBetaMin(alpha, beta, depth):
        global bestMove
        value = float(999999)
        if (depth == 0):
            return (-board.getPointValueOfSide(board.currentSide),)
        
        random.shuffle(moveTree)
        for move in moveTree:
            #for m in legalMoves:
            if (move in legalBestMoves):
                value = min(value, alphaBetaMax(alpha, beta, depth - 1)[0])
                if (value <= alpha):
                    return alpha, move.move
                if (value < beta):
                    beta = value
                    bestMove = move.move
                    bestMove.notation = parser.notationForMove(bestMove)
        #return {'beta': beta, 'bestMove': bestMove}
        return beta, bestMove
        #return bestMove
    
    score, action = alphaBetaMax(-999999, 999999, 3)
    return score, action

# def alphaBetaMove(board, parser, alpha, beta, depth):
#     import MoveNode as MoveNode

#     AIagent = AI(board, True, depth)
#     legalMoves = board.getAllMovesLegal(board.currentSide)
#     bestMove = None
#     moveTree = AIagent.generateMoveTree()

#     if (depth == 0 or board.isCheckmate or board.isStalemate):
#         return (board.getPointValueOfSide(board.currentSide),)

#     if (board.currentSide == playerSide):
#         bestValue = -999999
#         for move in moveTree:
#             for legalMove in legalMoves:
#                 value = alphaBetaMove(board, parser, alpha, beta, depth - 1)
#                 bestValue = max(bestValue, value)
#                 alpha = max(alpha, bestValue)
#                 if (beta <= alpha):
#                     bestMove = legalMove
#                     bestMove.notation = parser.notationForMove(bestMove)
#                     break
#         return bestValue, bestMove
#     else:
#         bestValue = 999999
#         for move in moveTree:
#             for legalMove in legalMoves:
#                 value = alphaBetaMove(board, parser, alpha, beta, depth - 1)
#                 bestValue = min(bestValue, value)
#                 beta = min(beta, bestValue)
#                 if (beta <= alpha):
#                     bestMove = legalMove
#                     bestMove.notation = parser.notationForMove(bestMove)
#                     break
#         return bestValue, bestMove

def makeMove(move, board):
    print("Making move : " + move.notation)
    board.makeMove(move)


def printPointAdvantage(board):
    print("Currently, the point difference is : " +
          str(board.getPointAdvantageOfSide(board.currentSide)))


def undoLastTwoMoves(board):
    if len(board.history) >= 2:
        board.undoLastMove()
        board.undoLastMove()


def startGame(board, playerSide, ai):
    parser = InputParser(board, playerSide)
    while True:
        print()
        print(board)
        print()
        if board.isCheckmate():
            if board.currentSide == playerSide:
                print("Checkmate, you lost")
            else:
                print("Checkmate! You won!")
            return

        if board.isStalemate():
            if board.currentSide == playerSide:
                print("Stalemate")
            else:
                print("Stalemate")
            return

        if board.currentSide == playerSide:
            #printPointAdvantage(board)
            try:
                move = getAlphaBetaMove(board, parser)[1]
                #move = alphaBetaMove(board, parser, -999999, 999999, 3)[1]
            except ValueError as error:
                print("%s" % error)
                continue
            makeMove(move, board)

        else:
            print("AI thinking...")
            move = ai.getBestMove()
            move.notation = parser.notationForMove(move)
            makeMove(move, board)

board = Board()
playerSide = askForPlayerSide()
print()
aiDepth = askForDepthOfAI()
opponentAI = AI(board, not playerSide, aiDepth)

try:
    startGame(board, playerSide, opponentAI)
except KeyboardInterrupt:
    sys.exit()
