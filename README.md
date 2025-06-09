# Tic-Tac-Toe CLI Game

A simple command-line Tic-Tac-Toe game implemented in Python.

## Features

*   Play Tic-Tac-Toe against another player.
*   Text-based interface.

## Setup

This project uses Poetry for dependency management, though there are currently no external dependencies beyond Python itself.

1.  **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```
2.  **Ensure Python is installed** (Version 3.x recommended).
3.  **Install Poetry (if you want to manage dependencies using it):**
    Follow the instructions on the [official Poetry website](https://python-poetry.org/docs/#installation).
4.  **Install dependencies (if any were added):**
    ```bash
    poetry install
    ```

## How to Run the Game

You can run the game directly using Python:

```bash
python -m dj_tictactoe.Main
```

Alternatively, if you have Poetry installed and are inside the project directory, you might be able to run it via Poetry (though a script would need to be defined in `pyproject.toml` for `poetry run <script_name>`):

```bash
poetry run python -m dj_tictactoe.Main
```

Follow the on-screen prompts to play the game. Enter the number of the cell (1-9) where you want to place your mark.
