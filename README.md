# Vityarthi_Project
#  Multi-Player Number Game

## Overview
A Python command-line game where multiple players take turns guessing a randomly generated number between 1 and 100. Players earn points by correctly guessing the secret number.

##  What it does
 * Multiplayer support: Play with as many friends as you want.
 * Helpful hints: The game nudges you if your guess is "too high" or "too low" so you aren't completely in the dark.
 * Keeps score: You can play multiple rounds, and whoever nails the exact number gets a point.
 * Leaderboards: Shows the current standings between rounds and crowns a final winner at the end.
 * Bulletproof inputs: I added input validation, so accidentally typing "potato" instead of a number won't crash the whole game.
##  How to run it
This is written in pure Python 3 and only uses the built-in random module. That means zero setup—no external libraries, no pip install required.
 * Make sure you have Python 3 installed.
 * Download or clone this project.
 * Open your terminal in the project folder and run:
```bash
python Multi_player_number_game.py
```
(Just replace Multi_player_number_game.py if you rename the file!)
##  How a match goes down
 * Setup: The game asks how many people are playing and gets everyone's name.
 * The Secret: It secretly locks in a number from 1 to 100.
 * The Hunt: You take turns guessing. Pay attention to the hints!
 * The Win: First person to guess it correctly steals the point for that round.
 * Again? Choose whether to play another round or end the game to see the final scoreboard.
## Exception Handling
If you want to test the edge cases, go for it. I explicitly built the game to handle:
 * Invalid/negative player counts.
 * People trying to bypass entering a name (empty inputs).
 * Guesses outside the 1–100 range.
 * Complete gibberish (letters/symbols) when it asks for a number.
 * Weird inputs when it asks y/n to continue playing.
## Future Improvements
This is just a fun educational project for now, but if I keep working on it, I'd love to add:
 * A countdown timer (to add a little panic to your turn).
 * Difficulty levels and a strict limit on the total number of guesses allowed.
 * Maximum number of guesses
 * Player statistics
 * Different scoring systems
 * Graphical user interface
 * Player stats to track win rates over time.
 * A real GUI so we can graduate from the command line.

## License
Educational project created for learning Python programming.
