# 🇯🇵 Hiragana Quiz Game (Python)

A simple and interactive command-line game built in Python to help practice and memorize Japanese Hiragana characters. 

I created this project to combine my programming logic studies with my personal goal of learning the Japanese language.

## How it Works
The game acts as a flashcard quiz in the terminal:
* The program randomly draws a Hiragana symbol.
* The player must type the correct sound (Romaji) for that symbol.
* **Life System:** The player starts with 3 lives. Every wrong answer costs 1 life.
* The game tracks the score and ends if the player loses all lives or types 'exit'.

## Technologies & Concepts Used
* **Python 3**
* **Dictionaries (`dict`):** Used to map the Japanese symbols (keys) to their respective sounds (values).
* **Lists & `random` module:** To dynamically shuffle and pick the symbols.
* **Control Flow:** `while` loops for the core game loop, and `if/elif/else` statements for answer validation and life tracking.

## How to Run
1. Clone this repository to your machine.
2. Open your terminal and navigate to the project folder.
3. Run the following command:
   ```bash
   python QUIZ.py