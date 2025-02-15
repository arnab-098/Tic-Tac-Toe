class ResultChecker:
    def __init__(self, size: int) -> None:
        self.size = size
        self.result = str()

    def check(self, board: list[list[str]]):
        self.result = self.checkRows(board)
        if self.result != "_":
            return
        self.result = self.checkColumns(board)
        if self.result != "_":
            return
        self.result = self.checkDiagonals(board)
        if self.result != "_":
            return
        if self.isMovesLeft(board):
            self.result = "_"
        else:
            self.result = "D"

    def getResult(self):
        return self.result

    def isMovesLeft(self, board):
        for i in range(self.size):
            for j in range(self.size):
                if board[i][j] == "_":
                    return True
        return False

    def checkRows(self, board):
        for i in range(self.size):
            key = board[i][0]
            if key == "_":
                continue
            for j in range(1, self.size):
                if board[i][j] != key:
                    key = "_"
                    break
            if key != "_":
                return key
        return "_"

    def checkColumns(self, board):
        for i in range(self.size):
            key = board[0][i]
            if key == "_":
                continue
            for j in range(1, self.size):
                if board[j][i] != key:
                    key = "_"
                    break
            if key != "_":
                return key
        return "_"

    def checkDiagonals(self, board):
        if board[0][0] == "_" or board[0][-1] == "_":
            return "_"
        key = board[0][0]
        for i in range(1, self.size):
            if board[i][i] != key:
                key = "_"
                break
        if key != "_":
            return key
        key = board[0][-1]
        for i in range(1, self.size):
            if board[i][-1 * i - 1] != key:
                key = "_"
                break
        return key
