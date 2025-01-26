#!/bin/python3


import sys
from PyQt5.QtWidgets import QApplication

from menu import MenuScreen


def main() -> None:
    try:
        app = QApplication(sys.argv)
        menu = MenuScreen()
        menu.show()
        sys.exit(app.exec_())
    except KeyboardInterrupt:
        print("Terminating Program")
        sys.exit()


if __name__ == "__main__":
    main()
