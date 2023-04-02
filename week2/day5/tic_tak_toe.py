import sys
print('*' * 10, 'Tic-Tac-Toe!', '*' * 10)
board = list(range(1, 10))


def draw_board(bord):
    print('-' * 13)
    for i in range(3):
        print('|', board[0 + i*3], '|', board[1 + i*3], '|', board[2 + i*3])
        print('-' * 13)


def player_input(board):
    row = int(input('Print row: '))
    column = int(input('Print column: '))
    if row == 1 and column == 1:
        board[0] = 'x'
    if row == 1 and column == 2:
        board[1] = 'x'
    if row == 1 and column == 3:
        board[2] = 'x'
    if row == 2 and column == 1:
        board[3] = 'x'
    if row == 2 and column == 2:
        board[4] = 'x'
    if row == 2 and column == 3:
        board[5] = 'x'
    if row == 3 and column == 1:
        board[6] = 'x'
    if row == 3 and column == 2:
        board[7] = 'x'
    if row == 3 and column == 3:
        board[8] = 'x'


def player_input2(board):
    row = int(input('Print row: '))
    column = int(input('Print column: '))
    if row == 1 and column == 1:
        board[0] = 'o'
    if row == 1 and column == 2:
        board[1] = 'o'
    if row == 1 and column == 3:
        board[2] = 'o'
    if row == 2 and column == 1:
        board[3] = 'o'
    if row == 2 and column == 2:
        board[4] = 'o'
    if row == 2 and column == 3:
        board[5] = 'o'
    if row == 3 and column == 1:
        board[6] = 'o'
    if row == 3 and column == 2:
        board[7] = 'o'
    if row == 3 and column == 3:
        board[8] = 'o'


def check_win(board):
    if board[0] == board[1] == board[2]:
        print('you won')
        sys.exit()
    if board[3] == board[4] == board[5]:
        print('you won')
        sys.exit()
    if board[6] == board[7] == board[8]:
        print('you won')
        sys.exit()
    if board[0] == board[3] == board[6]:
        print('you won')
        sys.exit()
    if board[1] == board[4] == board[7]:
        print('you won')
        sys.exit()
    if board[2] == board[5] == board[8]:
        sys.exit()
    if board[0] == board[4] == board[8]:
        sys.exit()
    if board[2] == board[4] == board[6]:
        sys.exit()


draw_board(board)
player_input(board)
draw_board(board)
check_win(board)
player_input2(board)
draw_board(board)
check_win(board)
player_input(board)
draw_board(board)
check_win(board)
player_input2(board)
draw_board(board)
check_win(board)
player_input(board)
draw_board(board)
check_win(board)
player_input2(board)
draw_board(board)
check_win(board)
player_input(board)
draw_board(board)
check_win(board)
player_input2(board)
draw_board(board)
check_win(board)
player_input(board)
draw_board(board)
check_win(board)
player_input2(board)
draw_board(board)
check_win(board)
player_input(board)
draw_board(board)
check_win(board)
player_input2(board)
draw_board(board)
check_win(board)
