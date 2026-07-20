# Number Guessing Game (CLI)

An interactive command-line Number Guessing Game built with Python. The application generates a random number and challenges the user to guess it with helpful hints and attempt tracking.

## Features

- **Random Number Generation**: Dynamically generates a random integer within a configurable range (e.g., 1 to 100).
- **Smart Hints**: Tells the player whether their guess is "Too High" or "Too Low" after every attempt.
- **Attempt Counter**: Tracks the total number of attempts taken to guess the correct number.
- **Robust Error Handling**: Prevents game crashes if the user inputs text or invalid values instead of numbers.
- **Replay Option**: Allows players to start a new game session without restarting the script.

## Technologies Used

- **Python 3**
- Standard Python Libraries: `random`, `sys`

## How to Run

1. Ensure Python 3 is installed on your system.
2. Open your terminal or command prompt in the project directory.
3. Run the application:

```bash
python guessing_game.py