# 🎮 Number Guessing Game (Python)

A simple command-line game built with Python where the computer thinks of a number between 1 and 100, and the player has to guess it within a limited number of attempts based on the chosen difficulty level.

---

## 🧠 Game Description

- The computer randomly selects a number between **1 and 100**.
- The player chooses a difficulty:
  - `easy` → 10 attempts
  - `hard` → 5 attempts
- The player then guesses the number within the allowed attempts.
- Feedback is given for each guess:
  - “Too high”
  - “Too low”
  - “You got it!”

---

## 🚀 How to Run

1. Make sure you have Python installed.
2. Clone or download this repository.
3. Run the script:

```bash
python number_guessing_game.py

```
### Sample Output 
```
Welcome to the number guessing game!
I'm thinking of a number between 1 and 100.
Choose difficulty: 'easy' or 'hard': easy
You have 10 attempts remaining.
Make a guess: 50
Too high!
You have 9 attempts remaining.
Make a guess: 25
Too low!
...
You got it! The number was 32.
```
