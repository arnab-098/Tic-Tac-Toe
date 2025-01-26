from PyQt5.QtWidgets import (
    QWidget,
    QPushButton,
    QGridLayout,
    QVBoxLayout,
    QLabel,
)
from PyQt5.QtCore import Qt

from gameGUI import TicTacToe


class MenuScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Tic Tac Toe Menu")
        self.setGeometry(100, 100, 400, 400)

        layout = QVBoxLayout()
        self.setLayout(layout)

        label = QLabel("Choose Board Size:")
        label.setStyleSheet("font-size: 18px;")
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)

        button_layout = QGridLayout()
        layout.addLayout(button_layout)

        self.buttons = []
        for idx, size in enumerate([3, 4, 5]):
            button = QPushButton(f"{size}x{size}")
            button.setStyleSheet(
                "font-size: 18px; padding: 20px; width: 100px; height: 100px;"
            )
            button.setFixedSize(100, 100)
            button.clicked.connect(lambda checked, s=size: self.start_game(s))
            button_layout.addWidget(button, idx // 3, idx % 3, alignment=Qt.AlignCenter)
            self.buttons.append(button)

    def start_game(self, size):
        self.hide()
        self.game_window = TicTacToe(size)
        self.game_window.show()
