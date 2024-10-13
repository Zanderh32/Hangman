# Hangman Game in Python

This project is a Python implementation of the classic **Hangman** game. Players try to guess the hidden word one letter at a time, with each incorrect guess leading to a part of the hangman figure being drawn. The game ends when the player guesses the word correctly or runs out of guesses.

## Features

- **Random Word Selection**: A word is chosen randomly from a predefined word list.
- **Player Input**: Players guess one letter at a time, trying to discover the hidden word.
- **Win Condition**: The player wins by guessing all the letters of the word before making too many incorrect guesses.
- **Lose Condition**: If the player guesses incorrectly more than 6 times, they lose the game.
- **Feedback**: The game provides real-time feedback on the guessed letters, the current state of the word, and the number of incorrect guesses.

## How It Works

1. **Word Selection**:
   - A word is randomly selected from a word list (`wordlist.txt`), which should be located in the same directory as the program.
   
2. **Gameplay**:
   - The player is prompted to input a letter for each guess.
   - If the letter is in the word, it is revealed in its correct position(s).
   - If the letter is incorrect, the guess is counted against the player.

3. **End Game**:
   - The game ends when the player correctly guesses the entire word or exceeds 6 incorrect guesses. If the player loses, the correct word is displayed.
