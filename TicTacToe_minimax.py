
from math import inf as infinity
from random import choice
USER = -1
CPU = +1
board = [ [0, 0, 0],[0, 0, 0],[0, 0, 0],]
mark = [ [0, 0, 0],[0, 0, 0],[0, 0, 0],]    #Used to draw the board state
def title():       
    print(' _______________________________________________________________ ')
    print("|  _____  _  ____     _____  ____  ____     _____  ____  _____  |")
    print("| /__ __\/ \/   _\   /__ __\/  _ \/   _\   /__ __\/  _ \/  __/  |")   
    print("|   / \  | ||  / _____ / \  | / \||  / _____ / \  | / \||  \    |")  
    print("|   | |  | ||  \_\____\| |  | |-|||  \_\____\| |  | \_/||  /_   |") 
    print("|   \_/  \_/\____/     \_/  \_/ \|\____/     \_/  \____/\____\  |")
    print("|                       by  YASH MUNJAL                         |")
    print('|_______________________________________________________________|\n')

def evaluate(board):   #Evaluates the leaves of game tree

    if wins(board, CPU):
        score = +1
    elif wins(board, USER):
        score = -1
    else:
        score = 0

    return score

def game_end(board):   # Checks whether user or cpu has won the game

    return wins(board, USER) or wins(board, CPU)

def empty_cells(board):   #Returns list of empty cells
    cells = []

    for x, row in enumerate(board):
        for y, box in enumerate(row):
            if box == 0:
                cells.append([x, y])

    return cells


def valid(x, y):   #Checks whether the move is valid or not
    if [x, y] in empty_cells(board):
        return True
    else:
        return False


def wins(board, player):    # Checks whether the player(cpu or user) has won or not

    win_state = [
        [board[0][0], board[0][1], board[0][2]], [board[1][0], board[1][1], board[1][2]],[board[2][0], board[2][1], board[2][2]], [board[0][0], board[1][0], board[2][0]],[board[0][1], board[1][1], board[2][1]],[board[0][2], board[1][2], board[2][2]], [board[0][0], board[1][1], board[2][2]],[board[2][0], board[1][1], board[0][2]],
    ]
    if [player, player, player] in win_state:
        return True
    else:
        return False

def set_marker(x, y, player):  # Sets the marker at a cell

    if valid(x, y):
        board[x][y] = player
        return True
    else:
        return False


def minimax(board, depth, player):  # MINIMAX function to obtain optimal move

    if player == CPU:
        move = [-1, -1, -infinity]
    else:
        move = [-1, -1, +infinity]

    if depth == 0 or game_end(board):
        score = evaluate(board)
        return [-1, -1, score]

    for box in empty_cells(board):
        x, y = box[0], box[1]
        board[x][y] = player
        score = minimax(board, depth - 1, -player)
        board[x][y] = 0
        score[0], score[1] = x, y

        if player == CPU:
            if score[2] > move[2]:
                move = score  # max value
        else:
            if score[2] < move[2]:
                move = score  # min value

    return move

def draw_board(board, cpu_marker, user_marker):  #Draws the current state of game board

    for x in [0,1,2]:
        for y in [0,1,2]:
            if board[x][y]==-1:
                mark[x][y]=user_marker
            elif board[x][y]==1:
                mark[x][y]=cpu_marker
            elif board[x][y]==0:
                mark[x][y]=' '

    print()
    print('                               reference:')
    print('     |    |     ',10*' ','     |    |   ',)
    print('  '+mark[0][0]+'  | '+mark[0][1]+'  | '+mark[0][2]+'   ',10*' ','  1  | 2  | 3  ')
    print('-----+----+-----',10*' ',"-----+----+-----")
    print('     |    |     ',10*' ',"     |    |     ")
    print('  '+mark[1][0]+'  | '+mark[1][1]+'  | '+mark[1][2]+'   ',10*' ',"  4  | 5  | 6   ")
    print('-----+----+-----',10*' ',"-----+----+-----")
    print('     |    |     ',10*' ',"     |    |      ")
    print('  '+mark[2][0]+'  | '+mark[2][1]+'  | '+mark[2][2]+'   ',10*' ',"  7  | 8  | 9    \n\n")

def cpu_chance(cpu_marker, user_marker):  # Calls minimax to obtain cpu's move

    depth = len(empty_cells(board))
    if depth == 0 or game_end(board):
        return

    print('Cpu turn')
    draw_board(board, cpu_marker, user_marker)

    if depth == 9:
        x = choice([0, 1, 2])
        y = choice([0, 1, 2])
    else:
        move = minimax(board, depth, CPU)
        x, y = move[0], move[1]

    set_marker(x, y, CPU)


def user_chance(cpu_marker, user_marker):  # Ask's user for the positon to place marker

    depth = len(empty_cells(board))
    if depth == 0 or game_end(board):
        return

    move = -1
    moves = {
        1: [0, 0], 2: [0, 1], 3: [0, 2],
        4: [1, 0], 5: [1, 1], 6: [1, 2],
        7: [2, 0], 8: [2, 1], 9: [2, 2],
    }

    print('User turn')
    draw_board(board, cpu_marker, user_marker)

    while move < 1 or move > 9:
        try:
            move = int(input('Enter the position to place your marker(1-9): '))
            coord = moves[move]
            can_move = set_marker(coord[0], coord[1], USER)

            if not can_move:
                print('Already Occupied')
                move = -1
        except (KeyError, ValueError):
            print('Bad choice')


def main():  #Main Function
    title()
    user_marker = ''  # X or O
    cpu_marker = ''  # X or O
    first = ''  # if human is the first

    # User chooses X or O to play
    while user_marker != 'O' and user_marker != 'X':
        try:
            print('')
            user_marker = input('Choose a marker to play (X or O)\nChosen: ').upper()
        except (KeyError, ValueError):
            print('Choose a valid marker!')

    # cpu's marker
    if user_marker == 'X':
        cpu_marker = 'O'
    else:
        cpu_marker = 'X'

    # User chance
    while first != 'Y' and first != 'N':
        try:
            first = input('First to start?[y/n]: ').upper()
        except (KeyError, ValueError):
            print('Bad choice')

    # Main loop 
    while len(empty_cells(board)) > 0 and not game_end(board):
        if first == 'N':
            cpu_chance(cpu_marker, user_marker)
            first = ''

        user_chance(cpu_marker, user_marker)
        cpu_chance(cpu_marker, user_marker)

    # Game over
    if wins(board, USER):
        print('User turn')
        draw_board(board, cpu_marker, user_marker)
        print('USER WINS!')
    elif wins(board, CPU):
        print('Cpu turn')
        draw_board(board, cpu_marker, user_marker)
        print('CPU WINS!')
    else:
        draw_board(board, cpu_marker, user_marker)
        print('DRAW!')
    
    while True:
        restart = input('Do you want to play again?(y/n):  ').upper()
        if restart=='Y':
            main()
        elif restart=='N':
            print('Nice playing with you ! Bbye !')
            exit()        


if __name__ == '__main__':
    main()
