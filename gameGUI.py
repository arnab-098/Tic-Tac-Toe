from PyQt5.QtWidgets import (
    QWidget,
    QPushButton,
    QGridLayout,
    QMessageBox,
    QVBoxLayout,
    QLabel,
)
from PyQt5.QtCore import Qt

from minimax import MiniMax
from resultChecker import ResultChecker


class TicTacToe(QWidget):
    def __init__(self, size=3):
        super().__init__()
        self.gridSize: int = int(size)
        self.board = [["_" for _ in range(self.gridSize)] for _ in range(self.gridSize)]
        self.minimaxAI = MiniMax(self.gridSize)
        self.checker = ResultChecker(self.gridSize)
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Tic Tac Toe")
        self.setGeometry(100, 100, 300, 300)

        self.grid_layout = QGridLayout()
        self.setLayout(self.grid_layout)

        self.buttons = [
            [QPushButton("") for _ in range(self.gridSize)]
            for _ in range(self.gridSize)
        ]
        self.player = "X"
        self.computer = "O"

        for i in range(self.gridSize):
            for j in range(self.gridSize):
                button = self.buttons[i][j]
                button.setFixedSize(100, 100)
                button.setStyleSheet("font-size: 24px;")
                button.clicked.connect(lambda checked, x=i, y=j: self.on_click(x, y))
                self.grid_layout.addWidget(button, i, j)

    def on_click(self, x, y):
        button = self.buttons[x][y]
        if button.text() != "":
            return
        button.setText(self.player)
        self.board[x][y] = self.player

        self.checker.check(self.board)
        if self.check_winner():
            QMessageBox.information(self, "Game Over", "Player wins!")
            self.reset_board()
        elif self.check_draw():
            QMessageBox.information(self, "Game Over", "It's a draw!")
            self.reset_board()
        else:
            self.computerTurn()

    def playerTurn(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].setEnabled(True)

    def computerTurn(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].setEnabled(False)

        x, y = self.minimaxAI.findBestMove(self.board)

        self.board[x][y] = self.computer
        button = self.buttons[x][y]
        button.setText(self.computer)

        self.checker.check(self.board)
        if self.check_winner():
            QMessageBox.information(self, "Game Over", "Computer wins!")
            self.reset_board()
        elif self.check_draw():
            QMessageBox.information(self, "Game Over", "It's a draw!")
            self.reset_board()
        else:
            self.playerTurn()

    def check_winner(self):
        O_win = self.checker.getResult() == "O"
        X_win = self.checker.getResult() == "X"
        return O_win or X_win

    def check_draw(self):
        return self.checker.getResult() == "D"

    def reset_board(self):
        for i in range(self.gridSize):
            for j in range(self.gridSize):
                self.buttons[i][j].setText("")
                self.board[i][j] = "_"

        self.swap_symbols()

        if self.computer == "X":
            self.computerTurn()
        else:
            self.playerTurn()

    def swap_symbols(self):
        self.player, self.computer = self.computer, self.player
        self.minimaxAI.setSymbols(self.player, self.computer)
