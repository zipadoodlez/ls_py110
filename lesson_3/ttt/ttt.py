def prompt(message):
    print(f'==> {message}')


def display_board(board):
    print()
    print(f' {board[0][0]} | {board[0][1]} | {board[0][2]}')
    print('---|---|---')
    print(f' {board[1][0]} | {board[1][1]} | {board[1][2]}')
    print('---|---|---')
    print(f' {board[2][0]} | {board[2][1]} | {board[2][2]}')
    print()


def player_moves(board):
    prompt("""Please pick your move (row column).
    Example: '1 1' places an X in the top left corner.""")
    p_move = [int(i) - 1 for i in input().split()]
    if not valid_moves[p_move[0]][p_move[1]]:
        prompt("That's not a valid move")
        p_move = [int(i) - 1 for i in input().split()]
    board[p_move[0]][p_move[1]] = 'x'
    valid_moves[p_move[0]][p_move[1]] = 0


board = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' '],
]

valid_moves = [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1],
]

played_moves = []

display_board(board)
player_moves(board)
display_board(board)
player_moves(board)
