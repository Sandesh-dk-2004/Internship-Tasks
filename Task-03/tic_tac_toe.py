import math

# Display the Tic-Tac-Toe board
def print_board(board):
    for row in board:
        print("|".join(row))
    print()

# Check if a player has won
def check_winner(board, player):
    # Check rows, columns, and diagonals
    for row in board:
        if all([cell == player for cell in row]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

# Check if the board is full
def is_full(board):
    return all(cell != " " for row in board for cell in row)

# Minimax Algorithm
def minimax(board, depth, is_maximizing):
    if check_winner(board, "O"):
        return 1
    if check_winner(board, "X"):
        return -1
    if is_full(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    score = minimax(board, depth + 1, False)
                    board[i][j] = " "
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    score = minimax(board, depth + 1, True)
                    board[i][j] = " "
                    best_score = min(score, best_score)
        return best_score

# Best move for AI
def best_move(board):
    best_score = -math.inf
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                score = minimax(board, 0, False)
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

# Main game loop
def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to AI Tic-Tac-Toe!")
    print_board(board)

    while True:
        # User move
        row = int(input("Enter row (0-2): "))
        col = int(input("Enter col (0-2): "))
        if board[row][col] == " ":
            board[row][col] = "X"
        else:
            print("Invalid move! Try again.")
            continue

        # Check for user win/draw
        if check_winner(board, "X"):
            print_board(board)
            print("You win!")
            break
        if is_full(board):
            print_board(board)
            print("It's a draw!")
            break

        # AI move
        ai_move = best_move(board)
        if ai_move:
            board[ai_move[0]][ai_move[1]] = "O"

        # Check for AI win/draw
        if check_winner(board, "O"):
            print_board(board)
            print("AI wins!")
            break
        if is_full(board):
            print_board(board)
            print("It's a draw!")
            break

        print_board(board)

# Start the game
play_game()
