import os

position = ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ']


def clear_screen():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')


def update_board(index, value):
    position[index-1] = ' ' + value + ' '


def reset_board():
    global position
    position = ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ']


def display_board():
    horizontalSeperation = '-----------'
    horizontalRow = '   ' + '|' + '   ' + '|' + '   '
    print(horizontalRow)
    print(position[0] + '|' + position[1] + '|' + position[2])
    print(horizontalRow)
    print(horizontalSeperation)
    print(horizontalRow)
    print(position[3] + '|' + position[4] + '|' + position[5])
    print(horizontalRow)
    print(horizontalSeperation)
    print(horizontalRow)
    print(position[6] + '|' + position[7] + '|' + position[8])
    print(horizontalRow)


if __name__ == '__main__':
    update_board(2, 'X')
    display_board()
    print(position)
