import random
import os


def clear():
    os.system('clear')
# made this with little googling and stackflow change 'cls' for windows

# Displaying a emty  board
# FINAL
def display_board(board):
    clear()
    print('  |   |')
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('-' * 8)
    print('  |   | ')
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('-' * 8)
    print('  |   | ')
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])


# Input player marker, if player chooses X, O will be assigned to
# player 2 and vice-versa
# FINAL
def player_input():
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input('Choose X or O : ').upper()
    if marker == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']


# Step3
def place_marker(board, marker, position):
    board[position] = marker


# Step 4
def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or
            (board[4] == mark and board[5] == mark and board[6] == mark) or
            (board[1] == mark and board[2] == mark and board[3] == mark) or
            (board[7] == mark and board[4] == mark and board[1] == mark) or
            (board[8] == mark and board[5] == mark and board[2] == mark) or
            (board[9] == mark and board[6] == mark and board[3] == mark) or
            (board[1] == mark and board[5] == mark and board[9] == mark) or
            (board[7] == mark and board[5] == mark and board[3] == mark))


# Step 5- To decide who goes first and return a output
def choose_first():
    first_player = random.randint(1, 2)
    if first_player == 1:
        return 'Player1'
    else:
        return 'Player2'


# Step 6:a function that returns a boolean if a space on the board is free.
def space_check(board, position):
    return board[position] == ' '


# Step 7:checks if the board is full;returns True if full else False
def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True


# Step 8: input next position and goto step 6
def player_choice(board):
    position = 0
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input('What is your next move? (1-9)'))
    return position


# Step 9: Ask the player if they want to play again
def replay():
    return input('Play Again? Press Y or N:').lower().startswith('y')


##DRIVING METHOD
print('Welcome to TicTacToe')
while True:
    # Reset the board
    theBoard = [' '] * 10
    player1marker, player2marker = player_input()
    turn = choose_first()
    print(f'{turn} will go first')
    gameRunning = True
    while gameRunning:
        if turn == 'Player1':
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1marker, position)

            if win_check(theBoard, player1marker):
                display_board(theBoard)
                print('Player1 WON THE GAME!')
                gameRunning = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The Game is Tie')
                    break
                else:
                    turn = 'Player2'

        else:
            # Player2 turn
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2marker, position)

            if win_check(theBoard, player2marker):
                display_board(theBoard)
                print('Player2 WON THE GAME!')
                gameRunning = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a Tie')
                    break
                else:
                    turn = 'Player1'
    if not replay():
        break
