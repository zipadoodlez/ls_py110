from random import randint
import os

WINNING_LINES = [
        [[0, 0], [0, 1], [0, 2]],
        [[1, 0], [1, 1], [1, 2]],
        [[2, 0], [2, 1], [2, 2]],
        [[0, 0], [1, 0], [2, 0]],
        [[0, 1], [1, 1], [2, 1]],
        [[0, 2], [1, 2], [2, 2]],
        [[0, 0], [1, 1], [2, 2]],
        [[2, 0], [1, 1], [0, 2]]]


def display_board(board, p, c):
    os.system('clear')
    print()
    print(f' {board[0][0]} | {board[0][1]} | {board[0][2]}')
    print(f'---|---|---    player wins: {p}')
    print(f' {board[1][0]} | {board[1][1]} | {board[1][2]}')
    print(f'---|---|---    computer wins: {c}')
    print(f' {board[2][0]} | {board[2][1]} | {board[2][2]}')
    print()


def valid_move(row, column, valid_moves):
    if row > 2 or row < 0 or column > 2 or row < 0:
        return False
    elif not valid_moves[row][column]:
        return False
    else:
        return True


def player_moves(board, valid_moves):
    move = detect_winning_move(board, valid_moves)
    if move:
        print(move)
    print("Please pick your move (row column): ", end='')
    while True:
        p_move = [int(i) - 1 for i in input().split()]
        if valid_move(*p_move, valid_moves):
            break
        else:
            print("That's not a valid move")
    board[p_move[0]][p_move[1]] = 'x'
    valid_moves[p_move[0]][p_move[1]] = 0


def computer_moves(board, valid_moves):
    move = detect_winning_move(board, valid_moves)
    if move:
        c_move = move
        print(move)
    else:
        while True:
            c_move = [randint(0, 2), randint(0, 2)]
            if valid_move(*c_move, valid_moves):
                break
    board[c_move[0]][c_move[1]] = 'o'
    valid_moves[c_move[0]][c_move[1]] = 0


def board_full(valid_moves):
    return not any([any(lst) for lst in valid_moves])


def game_count_prompt():
    while True:
        game_count = input("How many games would you like to play up to?")
        if game_count.isdigit():
            game_count = int(game_count)
            if game_count >= 1 and game_count <= 10:
                break
        print("Please input a number between 1 and 10")
    return game_count


def detect_winning_move(board, valid_moves):
    for i in range(len(WINNING_LINES)):
        a = WINNING_LINES[i][0]
        b = WINNING_LINES[i][1]
        c = WINNING_LINES[i][2]
        answer_list = [a, b, c]
        line = [board[a[0]][a[1]],
                board[b[0]][b[1]],
                board[c[0]][c[1]]]
        if line.count('o') == 2:
            for i in range(len(line)):
                if line[i] == ' ':
                    print(answer_list[i])
                    return answer_list[i]
        elif line.count('x') == 2:
            for i in range(len(line)):
                if line[i] == ' ':
                    print(answer_list[i])
                    return answer_list[i]

    return None


def game_winner(board, valid_moves):
    for line in WINNING_LINES:
        sq1 = board[line[0][0]][line[0][1]]
        sq2 = board[line[1][0]][line[1][1]]
        sq3 = board[line[2][0]][line[2][1]]
        if (sq1 == 'x' and sq2 == 'x' and sq3 == 'x'):
            return 'player'
        elif (sq1 == 'o' and sq2 == 'o' and sq3 == 'o'):
            return 'pc'

    return None


def initialize():
    board = [[' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' '],]

    valid_moves = [[1, 1, 1],
                   [1, 1, 1],
                   [1, 1, 1],]
    goes_first = bool(randint(0, 1))
    return board, valid_moves, goes_first


def new_match():
    print("Would you like to play again? (y/n): ")
    while True:
        play_again = input().lower()
        if play_again[0] == 'n':
            print("Thanks for playing!")
            quit()
        elif play_again[0] == 'y':
            play_ttt()
            break
        print("Sorry! That's not a valid choice!")


def play_game(p, c):
    board, valid_moves, goes_first = initialize()
    if goes_first:
        while True:
            display_board(board, p, c)
            player_moves(board, valid_moves)
            if board_full(valid_moves) or game_winner(board, valid_moves):
                break
            computer_moves(board, valid_moves)
            if board_full(valid_moves) or game_winner(board, valid_moves):
                break
    else:
        while True:
            computer_moves(board, valid_moves)
            display_board(board, p, c)
            if board_full(valid_moves) or game_winner(board, valid_moves):
                break
            player_moves(board, valid_moves)
            if board_full(valid_moves) or game_winner(board, valid_moves):
                break
    match game_winner(board, valid_moves):
        case 'pc':
            display_board(board, p, (c + 1))
            input("The computer won the game! Press enter to continue")
            return 'pc'
        case  'player':
            display_board(board, (p + 1), c)
            input("You won the game! Press enter to continue")
            return 'player'
        case None:
            input("It's a tie! Press enter to continue")
            return 'tie'


def play_ttt():
    game_count = game_count_prompt()
    p_wins, c_wins = 0, 0
    while True:
        winner = play_game(p_wins, c_wins)
        if winner == 'player':
            p_wins += 1
        elif winner == 'pc':
            c_wins += 1
        if p_wins == game_count:
            print("You won the match! Nice work!")
            new_match()
        elif c_wins == game_count:
            print("The computer won the match!")
            new_match()


print("Welcome to Tic Tac Toe!")
play_ttt()
