import random


class ZobristHash:
    def __init__(self, size: int) -> None:
        self.SIZE = size
        return

    def randomInt(self):
        min = 0
        max = pow(2, 64)
        return random.randint(min, max)

    def indexOf(self, piece):
        if piece == "X":
            return 0
        elif piece == "O":
            return 1
        else:
            return -1

    def initTable(self):
        self.ZobristTable = [
            [[self.randomInt() for _ in range(2)] for _ in range(self.SIZE)]
            for _ in range(self.SIZE)
        ]

    def computeHash(self, board):
        h = 0
        for i in range(self.SIZE):
            for j in range(self.SIZE):
                if board[i][j] != "-":
                    piece = self.indexOf(board[i][j])
                    h ^= self.ZobristTable[i][j][piece]
        return h
