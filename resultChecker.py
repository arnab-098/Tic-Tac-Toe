class ResultChecker:
    def __init__(self, size: int) -> None:
        self.size = size
        self.result = str()

    def check(self, board: list[list[str]]):
        self.board = board
        self.result = self.checkRows()
        if self.result != "_":
            return
        self.result = self.checkColumns()
        if self.result != "_":
            return
        self.result = self.checkDiagonals()
        if self.result != "_":
            return
        self.result = "_" if self.moveLeft() else "D"

    def getResult(self):
        return self.result

    def moveLeft(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == "_":
                    return True

    def checkRows(self):
        for i in range(self.size):
            key = self.board[i][0]
            if key == "_":
                continue
            for j in range(self.size):
                if self.board[i][j] != key:
                    key = "_"
                    break
            if key != "_":
                return key
        return "_"

    def checkColumns(self):
        for i in range(self.size):
            key = self.board[0][i]
            if key == "_":
                continue
            for j in range(self.size):
                if self.board[j][i] != key:
                    key = "_"
                    break
            if key != "_":
                return key
        return "_"

    def checkDiagonals(self):
        if self.board[0][0] == "_" or self.board[0][-1] == "_":
            return "_"
        key = self.board[0][0]
        for i in range(self.size):
            if self.board[i][i] != key:
                key = "_"
                break
        if key != "_":
            return key
        key = self.board[0][-1]
        for i in range(self.size):
            if self.board[i][-1 * i - 1] != key:
                key = "_"
                break
        return key
