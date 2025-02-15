import math
from collections import defaultdict

from resultChecker import ResultChecker
from zobristHash import ZobristHash


class MiniMaxAI:
    MIN = -math.inf
    MAX = math.inf
    EVALUATION_FUNCTION_POS_VAL = 100
    EVALUATION_FUNCTION_NEG_VAL = -100

    player = "X"
    computer = "O"

    def __init__(self, size: int) -> None:
        self.size = size
        self.checker = ResultChecker(size)
        self.hash = ZobristHash(size)
        self.transpositionTable = {}

    def findBlankCells(self, board):
        center = self.size // 2
        return sorted(
            [
                (i, j)
                for i in range(self.size)
                for j in range(self.size)
                if board[i][j] == "_"
            ],
            key=lambda cell: abs(cell[0] - center) + abs(cell[1] - center),
        )

    def searchHashMap(self, hash, depth):
        if hash in self.transpositionTable:
            storedValue, storedDepth = self.transpositionTable[hash]
            if storedDepth <= depth:
                return storedValue
        return None

    def minimax(self, board, depth, alpha, beta, isMaximizingPlayer):
        hash = self.hash.computeHash(board)
        moveValue = self.searchHashMap(hash, depth)
        if moveValue is not None:
            return moveValue

        self.checker.check(board)
        boardResult = self.checker.getResult()

        if boardResult == self.computer:
            moveValue = self.EVALUATION_FUNCTION_POS_VAL - depth
        elif boardResult == self.player:
            moveValue = self.EVALUATION_FUNCTION_NEG_VAL + depth
        elif boardResult == "D":
            moveValue = 0
        else:
            moveValue = (
                self.maxTurn(board, depth, alpha, beta)
                if isMaximizingPlayer
                else self.minTurn(board, depth, alpha, beta)
            )

        self.transpositionTable[hash] = (moveValue, depth)
        return moveValue

    def maxTurn(self, board, depth, alpha, beta):
        best = self.MIN
        moves = self.findBlankCells(board)
        for i, j in moves:
            board[i][j] = self.computer
            best = max(best, self.minimax(board, depth + 1, alpha, beta, False))
            board[i][j] = "_"
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best

    def minTurn(self, board, depth, alpha, beta):
        best = self.MAX
        moves = self.findBlankCells(board)
        for i, j in moves:
            board[i][j] = self.player
            best = min(best, self.minimax(board, depth + 1, alpha, beta, True))
            board[i][j] = "_"
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best

    def findBestMove(self, board):
        bestVal = self.MIN
        bestMove = (-1, -1)
        moves = self.findBlankCells(board)
        for i, j in moves:
            board[i][j] = self.computer
            moveVal = self.minimax(board, 0, self.MIN, self.MAX, False)
            board[i][j] = "_"
            if moveVal > bestVal:
                bestMove = (i, j)
                bestVal = moveVal
        return bestMove
