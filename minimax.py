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
        self.hash.initTable()
        self.moveSet = dict()

    def setSymbols(self, player, computer):
        self.player = player
        self.computer = computer

    def isMovesLeft(self, board):
        for i in range(self.SIZE):
            for j in range(self.SIZE):
                if board[i][j] == "_":
                    return True
        return False

    def evaluate(self, board):
        self.checker.check(board)
        result = self.checker.getResult()
        if result == self.computer:
            return 20
        elif result == self.player:
            return -20
        return 0

    def minimax(self, board, depth, alpha, beta, isMax):
        hash = self.hash.computeHash(board)
        if hash in self.moveSet:
            return self.moveSet[hash]

        score = self.evaluate(board)
        if score == 20:
            self.moveSet[hash] = 20
            return score - depth
        if score == -20:
            self.moveSet[hash] = -20
            return score + depth
        if not (self.isMovesLeft(board)):
            self.moveSet[hash] = 0
            return 0

        if isMax:
            self.moveSet[hash] = self.maxTurn(board, depth, alpha, beta, isMax)
            return self.moveSet[hash]
        else:
            self.moveSet[hash] = self.minTurn(board, depth, alpha, beta, isMax)
            return self.moveSet[hash]

    def maxTurn(self, board, depth, alpha, beta, isMax):
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

    def minTurn(self, board, depth, alpha, beta, isMax):
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
