from Model import *
from board import *

welcome_message()
if player_ready():
    while True:
        # Confirming choices of player
        player1Choice, player2Choice = player_choice()
        tie = False

        # 1 Game:
        for i in range(9):
            # Taking input from Player1:
            if i % 2 == 0:
                print('PLAYER 1:-')
                position1 = position_input()
                update_board(position1, player1Choice)
                display_board()
                if win_check(position):
                    print('Hey Player1, You have won the game!')
                    break

            # Taking input from player2:
            else:
                print('PLAYER 2:-')
                position2 = position_input()
                update_board(position2, player2Choice)
                display_board()
                if win_check(position):
                    print('Hey Player2, You have won the game!')
                    break

            # Checking if board has all positions filled
            if i == 8:
                tie = True
        if tie:
            print('Game Tied!!!')

        # Resetting the board after a win or tie:
        reset_board()

        # If players want to play again:
        if play_again():
            continue
        else:
            thanks_message()
            break
else:
    thanks_message()