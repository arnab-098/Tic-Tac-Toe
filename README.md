# Tic-Tac-Toe

A Python-based implementation of the classic Tic-Tac-Toe game featuring a graphical user interface (GUI) and an AI opponent powered by the Minimax algorithm.

## Features

* **Single-Player Mode**: Play against an AI that uses the Minimax algorithm for optimal moves.
* **Graphical User Interface**: Interactive GUI built with Tkinter for an engaging user experience.
* **Game State Evaluation**: Real-time assessment of game outcomes—win, lose, or draw.
* **Zobrist Hashing**: Efficient board state representation for quick evaluations.([GitHub][1])

## Technologies Used

* **Programming Language**: Python
* **GUI Library**: Tkinter
* **AI Algorithm**: Minimax
* **Hashing Technique**: Zobrist Hashing

## Project Structure

* `main.py`: Entry point of the application.
* `gameGUI.py`: Handles the graphical user interface components.
* `menu.py`: Manages the game menu and navigation.
* `minimaxAI.py`: Contains the AI logic using the Minimax algorithm.
* `resultChecker.py`: Evaluates the game board for win/draw conditions.
* `zobristHash.py`: Implements Zobrist hashing for board state representation.([GitHub][4], [GitHub][1], [GitHub][3])

## Getting Started

### Prerequisites

* Python 3.x installed on your system.

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/arnab-098/Tic-Tac-Toe.git
   cd Tic-Tac-Toe
   ```



2. **Run the game:**

   ```bash
   python main.py
   ```



## How It Works

* The GUI is built using Tkinter, providing an interactive platform for users.
* The AI opponent uses the Minimax algorithm to determine the best possible move at each turn.
* Zobrist hashing is employed to efficiently represent and evaluate board states, optimizing the AI's performance.([GitHub][1])

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

---

For more projects by the author, visit [arnab-098's GitHub profile](https://github.com/arnab-098/).
