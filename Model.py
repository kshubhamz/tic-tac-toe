from board import *


def win_check(board):

    # Conditions for winning:
    condition1 = board[0] == board[1] == board[2] != '   '
    condition2 = board[0] == board[3] == board[6] != '   '
    condition3 = board[0] == board[4] == board[8] != '   '
    condition4 = board[1] == board[4] == board[7] != '   '
    condition5 = board[2] == board[5] == board[8] != '   '
    condition6 = board[2] == board[4] == board[6] != '   '
    condition7 = board[3] == board[4] == board[5] != '   '
    condition8 = board[6] == board[7] == board[8] != '   '

    # Checking if the player has won:
    win = condition1 or condition2 or condition3 or condition4 or condition5 or condition6 or condition7 or condition8
    if win:
        return True
    else:
        return False


def welcome_message():
    print('Hey there, Welcome! We are pleased to see you here.')


def thanks_message():
    print('Hope to see you again. Thank You!!!')


def player_choice():
    while True:
        marker = input('Player 1: What do you want? X or O ').upper()
        if marker == 'X':
            return 'X', 'O'
        elif marker == 'O':
            return 'O', 'X'
        else:
            print('Please enter either X or O. Thank You!!!')


def player_ready():
    while True:
        choice = input('Do you want yo play the game? (Y for Yes & N for No): ').upper()
        if choice == 'Y':
            display_board()
            return True
        elif choice == 'N':
            return False
        else:
            print('Please enter either Y or N. Thank You!!!')


def play_again():
    while True:
        choice = input('Do you want to play again? (Y for Yes N for No): ').upper()
        if choice == 'Y':
            return True
        elif choice == 'N':
            return False
        else:
            print('Please enter either Y or N. Thank You!!!')


def position_input():
    while True:
        positionOnBoard = int(input('Enter the position(1-9): '))
        if positionOnBoard > 9 or positionOnBoard < 1:
            print("Please enter a valid value!")
        elif not check_validity(positionOnBoard):
            print('Kindly check the board! You are not allowed to modify the filled up position.')
        else:
            return positionOnBoard


def check_validity(positionOnBoard):
    return position[positionOnBoard-1] == '   '
