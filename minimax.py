from ast import BitOr
from resultChecker import ResultChecker


class MiniMax:
    def __init__(self, size: int) -> None:
        self.player = "X"
        self.computer = "O"
        self.size = size
        self.checker = ResultChecker(size)

    def setSymbols(self, player, computer):
        self.player = player
        self.computer = computer

    def isMovesLeft(self, board):
        for i in range(self.size):
            for j in range(self.size):
                if board[i][j] == "_":
                    return True
        return False

    def evaluate(self, board):
        self.checker.check(board)
        result = self.checker.getResult()
        if result == self.computer:
            return 10
        elif result == self.player:
            return -10
        return 0

    def minimax(self, board, depth, isMax):
        score = self.evaluate(board)

        if score == 10:
            return score - depth

        if score == -10:
            return score + depth

        if not (self.isMovesLeft(board)):
            return 0

        if isMax:
            best = -1000

            for i in range(self.size):
                for j in range(self.size):
                    if board[i][j] == "_":
                        board[i][j] = self.computer

                        best = max(best, self.minimax(board, depth + 1, not isMax))

                        board[i][j] = "_"
            return best

        else:
            best = 1000

            for i in range(self.size):
                for j in range(self.size):
                    if board[i][j] == "_":
                        board[i][j] = self.player

                        best = min(best, self.minimax(board, depth + 1, not isMax))

                        board[i][j] = "_"
            return best

    def findBestMove(self, board):
        bestVal = -1000
        bestMove = (-1, -1)

        for i in range(self.size):
            for j in range(self.size):
                if board[i][j] == "_":
                    board[i][j] = self.computer

                    moveVal = self.minimax(board, 0, False)

                    board[i][j] = "_"

                    if moveVal > bestVal:
                        bestMove = (i, j)
                        bestVal = moveVal

        return bestMove
