# Dice Game Roller

A command-line dice game built with Python. Roll dice, see results in ASCII art, and enjoy a classic game experience in your terminal.

## Features

- Roll virtual dice with randomized outcomes
- Display dice rolls using ASCII art for visual fun
- Interactive command-line interface
- Simple game flow with replay option

## Tech Stack

- Python: Core language for game logic
- Pipenv: Virtual environment and dependency management
- SQLite: Lightweight database for storing game data
- ASCII Art: For dice face visualization

## Getting Started

### Prerequisites

- Python 3.7 or higher
- Pipenv for environment management

## Installation

Clone the repository:
git clone https://github.com/JENNIFER754-DEL/dice-game-roller.git
cd dice-game-roller
Create and activate the virtual environment using pipenv:
pipenv install
pipenv shell
Run the game:
python run.py

## Project Structure

dice-game-roller/
├── Pipfile
├── Pipfile.lock
├── README.md
├── create_db.py
├── dice_game.db
├── run.py
├── dice_roller/
│ ├── init.py
│ ├── ascii_art.py
│ ├── cli.py
│ ├── game.py
│ └── models.py
└── migrations/

## Usage

### Starting the Game

pipenv run python run.py

### Gameplay Instructions

- Enter your name when prompted.
- Press Enter to roll the dice.
- The result of the roll will be displayed with ASCII dice.
- You can choose to roll again (`y`) or quit (`n`).

## Customization

You can easily customize:

- **Dice Faces:** Modify the dice layouts in `dice_roller/ascii_art.py`.
- **Messages or Prompts:** Customize text and instructions in `dice_roller/cli.py`.
- **Game Flow:** Modify `dice_roller/game.py` to add new rules or scoring systems.

## Contributors

Jennifer Wanjiru (https://github.com/JENNIFER754-DEL)

## Contributing

Want to contribute?

1. Fork the repository  
2. Create a new branch (`git checkout -b feature/my-feature`)  
3. Commit your changes (`git commit -m "Add my feature"`)  
4. Push to the branch (`git push origin feature/my-feature`)  
5. Open a Pull Request

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

- Python docs for `random` and `input()`
- Inspiration from traditional dice games
- ASCII Art reference from open-source community