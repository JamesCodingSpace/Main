import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Überprüfe Reihen, Spalten und Diagonalen
    return any(all(cell == player for cell in row) for row in board) or \
           any(all(board[i][j] == player for i in range(3)) for j in range(3)) or \
           all(board[i][i] == player for i in range(3)) or \
           all(board[i][2 - i] == player for i in range(3))

def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)

def get_empty_cells(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']

def player_move(board):
    while True:
        try:
            row = int(input("Enter the row (0, 1, or 2): "))
            col = int(input("Enter the column (0, 1, or 2): "))
            if board[row][col] == ' ':
                return row, col
            else:
                print("Cell already taken. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Try again.")

def minimax(board, depth, is_maximizing):
    if check_winner(board, 'O'):
        return 1
    elif check_winner(board, 'X'):
        return -1
    elif is_board_full(board):
        return 0

    if is_maximizing:
        max_eval = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    eval = minimax(board, depth + 1, False)
                    board[i][j] = ' '
                    max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    eval = minimax(board, depth + 1, True)
                    board[i][j] = ' '
                    min_eval = min(min_eval, eval)
        return min_eval

def get_computer_move(board, difficulty):
    empty_cells = get_empty_cells(board)

    if difficulty == 'easy':
        return random.choice(empty_cells)
    elif difficulty == 'medium':
        # Prioritize winning moves if available, else block the player
        for row, col in empty_cells:
            board[row][col] = 'O'
            if check_winner(board, 'O'):
                return row, col
            board[row][col] = ' '

        for row, col in empty_cells:
            board[row][col] = 'X'
            if check_winner(board, 'X'):
                return row, col
            board[row][col] = ' '

        return random.choice(empty_cells)
    elif difficulty == 'hard':
        # Implement Minimax algorithm for hard difficulty
        best_val = float('-inf')
        best_move = None
        for row, col in empty_cells:
            board[row][col] = 'O'
            move_val = minimax(board, 0, False)
            board[row][col] = ' '
            if move_val > best_val:
                best_move = (row, col)
                best_val = move_val
        return best_move

def play_tictactoe():
    while True:
        board = [[' ' for _ in range(3)] for _ in range(3)]
        player_turn = True  # True if it's player's turn, False if it's computer's turn

        difficulty = input("Choose difficulty (easy/medium/hard): ").lower()

        while True:
            print_board(board)

            if player_turn:
                row, col = player_move(board)
                symbol = 'X'
            else:
                print("Computer's turn:")
                row, col = get_computer_move(board, difficulty)
                symbol = 'O'

            board[row][col] = symbol

            if check_winner(board, symbol):
                print_board(board)
                print(f"{symbol} wins!")
                break

            if is_board_full(board):
                print_board(board)
                print("It's a tie!")
                break

            player_turn = not player_turn

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    play_tictactoe()