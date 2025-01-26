from resultChecker import ResultChecker
from zobristHash import ZobristHash


class MiniMax:
    def __init__(self, size: int) -> None:
        self.player = "X"
        self.computer = "O"
        self.SIZE = size
        self.MIN = -1000
        self.MAX = 1000
        self.checker = ResultChecker(size)
        self.hash = ZobristHash(size)
        self.transpositionTable = dict()

    def setSymbols(self, player, computer):
        self.player = player
        self.computer = computer

    def minimax(self, board, depth, alpha, beta, isMax) -> int:
        hash = self.hash.computeHash(board)

        if hash in self.transpositionTable:
            return self.transpositionTable[hash]

        self.checker.check(board)
        boardResult = self.checker.getResult()

        if boardResult == self.computer:
            self.transpositionTable[hash] = 10 - depth
        elif boardResult == self.player:
            self.transpositionTable[hash] = -10 + depth
        elif boardResult == "D":
            self.transpositionTable[hash] = 0
        elif isMax:
            self.transpositionTable[hash] = self.maxTurn(
                board, depth, alpha, beta, isMax
            )
        else:
            self.transpositionTable[hash] = self.minTurn(
                board, depth, alpha, beta, isMax
            )

        return self.transpositionTable[hash]

    def maxTurn(self, board, depth, alpha, beta, isMax) -> int:
        best = self.MIN

        for i in range(self.SIZE):
            for j in range(self.SIZE):
                if board[i][j] == "_":
                    board[i][j] = self.computer
                    best = max(
                        best, self.minimax(board, depth + 1, alpha, beta, not isMax)
                    )
                    board[i][j] = "_"

                    alpha = max(alpha, best)
                    if beta <= alpha:
                        return best

        return best

    def minTurn(self, board, depth, alpha, beta, isMax) -> int:
        best = self.MAX

        for i in range(self.SIZE):
            for j in range(self.SIZE):
                if board[i][j] == "_":
                    board[i][j] = self.player
                    best = min(
                        best, self.minimax(board, depth + 1, alpha, beta, not isMax)
                    )
                    board[i][j] = "_"

                    beta = min(beta, best)
                    if beta <= alpha:
                        return best

        return best

    def findBestMove(self, board):
        bestVal = self.MIN
        bestMove = (-1, -1)

        for i in range(self.SIZE):
            for j in range(self.SIZE):
                if board[i][j] == "_":
                    board[i][j] = self.computer

                    moveVal = self.minimax(board, 0, self.MIN, self.MAX, False)

                    board[i][j] = "_"

                    if moveVal > bestVal:
                        bestMove = (i, j)
                        bestVal = moveVal

        return bestMove
