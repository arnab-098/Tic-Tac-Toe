from PyQt5.QtWidgets import (
    QWidget,
    QPushButton,
    QGridLayout,
    QVBoxLayout,
    QMessageBox,
)
from PyQt5.QtCore import pyqtSignal

from minimaxAI import MiniMaxAI
from resultChecker import ResultChecker


class TicTacToe(QWidget):
    backToMenu = pyqtSignal()  # Signal to notify when back button is pressed

    player = "X"
    computer = "O"
    playerStarts = True

    def __init__(self, size=3):
        super().__init__()
        self.gridSize = size
        self.board = [["_" for _ in range(self.gridSize)] for _ in range(self.gridSize)]
        self.AI = MiniMaxAI(self.gridSize)
        self.checker = ResultChecker(self.gridSize)
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Tic Tac Toe")
        self.setGeometry(
            100, 100, 300, 350
        )  # Adjusted height to make space for back button

        # Main layout (vertical)
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)

        # Grid layout for board
        self.grid_layout = QGridLayout()
        self.main_layout.addLayout(self.grid_layout)

        self.buttons = [
            [QPushButton("") for _ in range(self.gridSize)]
            for _ in range(self.gridSize)
        ]

        for i in range(self.gridSize):
            for j in range(self.gridSize):
                button = self.buttons[i][j]
                button.setFixedSize(100, 100)
                button.setStyleSheet("font-size: 24px;")
                button.clicked.connect(lambda checked, x=i, y=j: self.on_click(x, y))
                self.grid_layout.addWidget(button, i, j)

        # Back button layout
        self.back_button = QPushButton("Back to Menu")
        self.back_button.setFixedHeight(40)
        self.back_button.clicked.connect(self.back_to_menu)
        self.main_layout.addWidget(self.back_button)

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
        for i in range(self.gridSize):
            for j in range(self.gridSize):
                self.buttons[i][j].setEnabled(True)

    def computerTurn(self):
        for i in range(self.gridSize):
            for j in range(self.gridSize):
                self.buttons[i][j].setEnabled(False)

        x, y = self.AI.findBestMove(self.board)

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
        return self.checker.getResult() in ["O", "X"]

    def check_draw(self):
        return self.checker.getResult() == "D"

    def reset_board(self):
        for i in range(self.gridSize):
            for j in range(self.gridSize):
                self.buttons[i][j].setText("")
                self.board[i][j] = "_"

        self.playerStarts = not self.playerStarts

        if self.playerStarts:
            self.playerTurn()
        else:
            self.computerTurn()

    def back_to_menu(self):
        self.backToMenu.emit()
        self.close()
