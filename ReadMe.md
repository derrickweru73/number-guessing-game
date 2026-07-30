# Number Guessing Game

## Project Overview

**Number Guessing Game** is a Python console application where the computer randomly generates a number between **1 and 100**, and the player attempts to guess it within a limited number of attempts based on the selected difficulty level. The game provides instant feedback after every guess, gives hints after multiple incorrect attempts, records high scores, and displays a leaderboard to encourage competition.

## Problems it Solves

- **Enhances Logical Thinking:** Encourages players to use reasoning and deduction instead of random guessing.
- **Improves Python Programming Skills:** Demonstrates fundamental programming concepts such as loops, functions, conditional statements, exception handling, file handling, and random number generation.
- **Creates an Interactive Learning Experience:** Provides immediate feedback (`Too High` or `Too Low`) after each guess, making learning fun and engaging.
- **Tracks Player Performance:** Saves player scores to a text file and displays a leaderboard, allowing users to monitor and improve their performance over time.

## Features

- **Random Number Generation:** Uses `random.randint(1, 100)` to generate a secret number.
- **Difficulty Levels:** Choose between:
  - Easy (**10 attempts**)
  - Medium (**7 attempts**)
  - Hard (**5 attempts**)
- **Guess Feedback:** Displays `Too High` or `Too Low` after each incorrect guess.
- **Attempt Counter:** Tracks attempts used and shows the remaining guesses.
- **Game Over Detection:** Ends the game when the player guesses correctly or runs out of attempts.
- **Hint System:** After three incorrect guesses, the game provides hints such as whether the number is even or odd, divisible by `5`, or greater than `50`.
- **High Score Storage:** Saves the player's username and score in `highscores.txt`.
- **Leaderboard:** Displays saved scores sorted from the fewest attempts to the highest.
- **Input Validation:** Prevents invalid or non-numeric input from crashing the game.
- **Menu-Driven Interface:** Allows players to play the game, view the leaderboard, or exit the application.

## Project Structure

```text
NumberGuessingGame/
│
├── main.py
├── highscores.txt
└── README.md
```

## Technologies Used

- Python 3
- `random` Module
- File Handling
- Functions
- Conditional Statements (`if`, `elif`, `else`)
- Loops (`while`)
- Exception Handling (`try` / `except`)
- Lists
- Tuples
- Sorting

## Core Python Concepts Demonstrated

- Variables
- User Input
- Functions
- While Loops
- Conditional Statements
- Random Number Generation
- File Handling
- Lists
- Tuples
- Exception Handling
- Sorting
- Menu-Driven Programming

## How the Game Works

1. Enter your username.
2. Select a difficulty level.
3. The computer generates a random number between `1` and `100`.
4. Guess the number.
5. The game responds with:
   - `Too High`
   - `Too Low`
6. After three incorrect guesses, a hint is displayed.
7. The game ends when:
   - You guess the correct number, or
   - You run out of attempts.
8. Winning scores are automatically saved to `highscores.txt` and can be viewed from the leaderboard.

## Installation

### Prerequisites

- Python 3.x
- Visual Studio Code (Recommended)

### Clone the Repository

```bash
git clone https://github.com/yourusername/NumberGuessingGame.git
```

### Open the Project

```bash
cd NumberGuessingGame
```

### Run the Game

```bash
python main.py
```

## Sample Gameplay

```text
========== MAIN MENU ==========
1. Play Game
2. View Leaderboard
3. Exit

Choose an option: 1

Enter your username: Derrick

Choose Difficulty
1. Easy
2. Medium
3. Hard

Remaining Attempts: 7

Guess: 60
Too High!

Guess: 30
Too Low!

Guess: 45
Too Low!

Hint!
The number is EVEN.
The number is divisible by 5.

Guess: 50

Congratulations!
You guessed the correct number.
```

## High Score Example

```text
Derrick,4
Faith,3
James,6
```

## Future Improvements

- Add multiple hint levels based on the remaining attempts.
- Implement different game modes such as Timed Mode and Endless Mode.
- Allow players to choose custom number ranges.
- Save only the top 10 highest scores.
- Add player statistics and game history.
- Add sound effects and animations.
- Introduce multiplayer mode.
- Package the game as a standalone executable.

## Contribution

You can contribute by:

- Improving the game interface.
- Adding more hint categories.
- Enhancing the leaderboard.
- Optimizing the game logic.
- Fixing bugs.
- Adding new game modes.

### How to Contribute

1. Fork the repository.
2. Create a new branch.

```bash
git checkout -b feature-name
```

3. Make your changes.

4. Commit your changes.

```bash
git commit -m "Added new feature"
```

5. Push your changes.

```bash
git push origin feature-name
```

6. Create a Pull Request.

## Author

**Developed by Derrick Weru**

## License

This project is for educational purposes and is free to use, modify, and distribute for learning and academic projects.