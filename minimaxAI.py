import math
import copy
import multiprocessing as mp
import random

from resultChecker import ResultChecker
from zobristHash import ZobristHash


def minimax_worker(args):
    (
        board,
        i,
        j,
        size,
        computer,
        player,
        EVALUATION_FUNCTION_POS_VAL,
        EVALUATION_FUNCTION_NEG_VAL,
    ) = args

    checker = ResultChecker(size)
    hash_obj = ZobristHash(size)
    transpositionTable = {}

    def searchHashMap(hash_key, depth):
        if hash_key in transpositionTable:
            storedValue, storedDepth = transpositionTable[hash_key]
            if storedDepth <= depth:
                return storedValue
        return None

    def minimax(board_local, depth, alpha, beta, isMaximizingPlayer):
        hash_key = hash_obj.computeHash(board_local)
        moveValue = searchHashMap(hash_key, depth)
        if moveValue is not None:
            return moveValue

        checker.check(board_local)
        boardResult = checker.getResult()

        if boardResult == computer:
            moveValue = EVALUATION_FUNCTION_POS_VAL - depth
        elif boardResult == player:
            moveValue = EVALUATION_FUNCTION_NEG_VAL + depth
        elif boardResult == "D":
            moveValue = 0
        else:
            moveValue = (
                maxTurn(board_local, depth, alpha, beta)
                if isMaximizingPlayer
                else minTurn(board_local, depth, alpha, beta)
            )

        transpositionTable[hash_key] = (moveValue, depth)
        return moveValue

    def maxTurn(board_local, depth, alpha, beta):
        best = -math.inf
        center = size // 2
        moves = sorted(
            [
                (x, y)
                for x in range(size)
                for y in range(size)
                if board_local[x][y] == "_"
            ],
            key=lambda cell: abs(cell[0] - center) + abs(cell[1] - center),
        )
        for x, y in moves:
            board_local[x][y] = computer
            best = max(best, minimax(board_local, depth + 1, alpha, beta, False))
            board_local[x][y] = "_"
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best

    def minTurn(board_local, depth, alpha, beta):
        best = math.inf
        center = size // 2
        moves = sorted(
            [
                (x, y)
                for x in range(size)
                for y in range(size)
                if board_local[x][y] == "_"
            ],
            key=lambda cell: abs(cell[0] - center) + abs(cell[1] - center),
        )
        for x, y in moves:
            board_local[x][y] = player
            best = min(best, minimax(board_local, depth + 1, alpha, beta, True))
            board_local[x][y] = "_"
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best

    board_copy = copy.deepcopy(board)
    board_copy[i][j] = computer
    moveVal = minimax(board_copy, 0, -math.inf, math.inf, False)
    return (i, j, moveVal)


class MiniMaxAI:
    MIN = -math.inf
    MAX = math.inf
    EVALUATION_FUNCTION_POS_VAL = 100
    EVALUATION_FUNCTION_NEG_VAL = -100
    THRESHOLD = {5: 16}

    player = "X"
    computer = "O"

    def __init__(self, size: int) -> None:
        self.size = size

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

    def simpleAI(self, board):
        blank_cells = self.findBlankCells(board)
        checker = ResultChecker(self.size)

        for i, j in blank_cells:
            board[i][j] = self.computer
            checker.check(board)
            if checker.getResult() == self.computer:
                board[i][j] = "_"
                return (i, j)
            board[i][j] = "_"

        for i, j in blank_cells:
            board[i][j] = self.player
            checker.check(board)
            if checker.getResult() == self.player:
                board[i][j] = "_"
                return (i, j)
            board[i][j] = "_"

        return random.choice(blank_cells)

    def findBestMove(self, board):
        bestVal = self.MIN
        bestMove = (-1, -1)
        moves = self.findBlankCells(board)

        if self.size >= 5 and len(moves) > self.THRESHOLD[self.size]:
            return self.simpleAI(board)

        args = [
            (
                board,
                i,
                j,
                self.size,
                self.computer,
                self.player,
                self.EVALUATION_FUNCTION_POS_VAL,
                self.EVALUATION_FUNCTION_NEG_VAL,
            )
            for i, j in moves
        ]

        with mp.Pool(mp.cpu_count()) as pool:
            results = pool.map(minimax_worker, args)

        for i, j, moveVal in results:
            if moveVal > bestVal:
                bestMove = (i, j)
                bestVal = moveVal

        return bestMove
