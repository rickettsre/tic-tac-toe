# tic-tac-toe
Text Based Tic Tac Toe Game
# Day 83 - 100 DAYS OF PYTHON COURSE

===========================================================

# _Task_

Tic tac toe

You can choose how you want your game to look. The simplest is to create a game board using "|" and "\_" symbols. But the design is up to you.

Using what you have learnt about Python programming, you will build a text-based version of the Tic Tac Toe game. The game should be playable in the command line just like the Blackjack game we created on Day 11. It should be a 2-player game, where one person is "X" and the other plays "O".

Using what you have learnt about Python programming, you will build a text-based version of the Tic Tac Toe game. The game should be playable in the command line just like the Blackjack game we created on Day 11. It should be a 2-player game, where one person is "X" and the other plays "O".

This is a simple demonstration of how the game works:

https://www.google.com/search?q=tic+tac+toe

You can choose how you want your game to look. The simplest is to create a game board using "|" and "\_" symbols. But the design is up to you.

If you have more time, you can challenge yourself to build an AI player to play the game with you. Morse Code.

# Rough Notes

Create a virtual environment:

# Linux

mkdir my-code
cd my-code
python3 -m venv .venv
source .venv/bin/activate

.venv/bin/python3 -m pip install --upgrade pip

e.g. pip3 install requirements:

pip3 install jupyter pandas matplotlib plotly.express

python -m pip freeze > requirements.txt

# Windows

md my-code
cd my-code
py -3 -m venv .venv

.venv\Scripts\activate.bat
.venv\Scripts\python.exe -m pip install --upgrade pip
e.g. pip3 install requirements:

pip3 install jupyter pandas matplotlib plotly.express
python -m pip freeze > requirements.txt

1. Create a text base logo using an ascii art generator e.g. https://patorjk.com/software/taag/#p=display&v=1&f=Doom&t=Tic%20Tac%20Toe

cat logo.py

logo = """

---

|\_ _(_) |\_ _| |_ _|  
 | | _ **\_ | | ** \_ **_ | | _** **\_
| | | |/ **| | |/ _` |/ \_\_| | |/ _ \ / _ \
 | | | | (\_\_ | | (_| | (** | | (\_) | **/
\_/ |\_|\_**| \_/\__,_|\_**| \_/\_**/ \_**|

|

"""

cat ghost*logo.py
logo = """
.-') * ('-. ) (`-.      .-') _            _   .-')                _  .-')    .-')      ('-.
(  OO) )  _(  OO)  ( OO ).   (  OO) )          ( '.( OO )_             ( \( -O )  ( OO ).  _(  OO)
/     '._(,------.(_/.  \_)-./     '._  .-----. ,--.   ,--.).-'),-----. ,------. (_)---\_)(,------.
|'--...__)|  .---' \  `.' / |'--...**)/ ,-. \| `.'   |( OO'  .-.  '|   /`. '/ _ | | .---'
'--. .--'| | \ /\ '--. .--''-' | || |/ | | | || / | |\ :` `. | |
| | (| '--. \ \ | | | .' / | |'.'| |\_) | |\| || |_.' | '..`''.)(| '--.
| | | .--' .' \_) | | .' /** | | | | \ | | | || . '.'.-.\_) \ | .--'
| | | `---. /  .'.  \    |  |   |       ||  |   |  |   `' '-' '| |\ \ \ / | `---.
   `--' `------''--'   '--'   `--' `-------'`--' `--'     `-----' `--' '--' `-----' `------'
"""

# Rough Notes

Computer Creates and Displays Board

3 ROWS 3 COLUMNS

Load Logo

Display board

Max goes is 3\*3 = 9

Ask player 1 to pick a position
NB Player 1 --> X
Player 2 --> 0

Decision are there enough goes left squares < 9?

No --> game over
Yes -->

Decision is there square already occupied?
Yes --> ask to choose again
No--> Continue put X in square

Check board
Decision Are there 3 in X in a row on the board
if yes Player 1 wins end game
No Player 2 goes:

Ask player 2 to go:

Decision are there enough goes left squares < 9?

No --> game over
Yes -->

Decision is there square already occupied?
Yes --> ask to choose again
No--> Continue put 0 in square

Check board
Decision Are there 3 in 0 in a row on the board
if yes Player 2 wins end game
No Player 1 goes:

Diplay board

## 0,0 0,1 0,2

## 1,0, 1,1, 1,2

## 2,0, 2,1, 2,2

##
