""" 
A Simple text based Tic Tac Toe game.
"""
from game_logo import logo
from os import system, name

PLAYER1_SYMBOL = "|X|"
PLAYER2_SYMBOL = "|O|"
BLANK_SYMBOL = "|_|"


def clear():
    """Clear the Screen Output"""
    # for Windows
    if name == "nt":
        _ = system("cls")
    # for Mac and linux(here, os.name is 'posix')
    else:
        _ = system("clear")


def board():
    row1 = ["|_|", "|_|", "|_|"]
    row2 = ["|_|", "|_|", "|_|"]
    row3 = ["|_|", "|_|", "|_|"]
    return row1, row2, row3


def in_use(game_board, symbol, row, column):
    if (
        game_board[row - 1][column - 1] == PLAYER1_SYMBOL
        or game_board[row - 1][column - 1] == PLAYER2_SYMBOL
    ):
        print(f"{row} {column} already in use)")
        return True
    else:
        game_board[row - 1][column - 1] = symbol


def check_for_win(game_board, symbol):
    for n in range(3):
        if (
            game_board[n][0] == symbol
            and game_board[n][1] == symbol
            and game_board[n][2] == symbol
        ):
            return True
        elif(
            game_board[0][n] == symbol
            and game_board[1][n] == symbol
            and game_board[2][n] == symbol
        ):
            return True
      
    if (
        game_board[0][0] == symbol
        and game_board[1][1] == symbol
        and game_board[2][2] == symbol
        or game_board[2][0] == symbol
        and game_board[1][1] == symbol
        and game_board[0][2] == symbol
    ):
        return True


def check_for_draw(game_board):
    n = len(game_board)
    if (
        BLANK_SYMBOL not in game_board[n - n]
        and BLANK_SYMBOL not in game_board[n + 1 - n]
        and BLANK_SYMBOL not in game_board[n + 2 - n]
    ):
        return True


def game():
    end_game = False
    row1, row2, row3 = board()
    game_board = [row1, row2, row3]
    current_player = PLAYER1_SYMBOL

    while end_game is False:
        position = input(
            f"{current_player.replace('|','')} - Pick a position on the board e.g. 11 for row 1 column 1? "
        )
        row = int(position[0])
        column = int(position[1])

        while in_use(game_board, current_player, row, column):
            position = input(
                f"{current_player.replace('|','')}- Pick another position on the board e.g. 11 for row 1 column 1? "
            )
            row = int(position[0])
            column = int(position[1])

        print(f"{row1}\n{row2}\n{row3}")

        if check_for_win(game_board, current_player):
            print(f"{current_player.replace('|','')} wins")
            end_game = True

        elif check_for_draw(game_board):
            print("The game is a DRAW")
            end_game = True

        else:
            if check_for_draw(game_board):
                print("Draw")
                end_game = True
            elif check_for_draw(game_board):
                print("Draw")
                end_game = True

        current_player = PLAYER2_SYMBOL if current_player == PLAYER1_SYMBOL else PLAYER1_SYMBOL

           
def main():
    play_again = True
    while play_again:
        clear()
        print(logo)
        game()
        start_again = input(
            f"Would you like another game? 'y' press any other key to exit\n\n"
        ).lower()
        if start_again != "y":
            play_again = False


if __name__ == "__main__":
    main()
