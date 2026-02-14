import math

# Creating the board
board = [" " for _ in range(9)]

# Printing the board
def print_board():
    print()
    for i in range(3):
        print(board[i*3] + " | " + board[i*3+1] + " | " + board[i*3+2])
        if i < 2:
            print("--+---+--")
    print()

# Checking winner
def check_winner(player):
    win_positions = [
        [0,1,2],[3,4,5],[6,7,8],  # Rows
        [0,3,6],[1,4,7],[2,5,8],  # Columns
        [0,4,8],[2,4,6]           # Diagonals
    ]
    for pos in win_positions:
        if board[pos[0]] == board[pos[1]] == board[pos[2]] == player:
            return True
    return False

# Checking if board full
def is_full():
    return " " not in board

# Minimax algorithm
def minimax(is_maximizing):
    if check_winner("O"):
        return 1
    if check_winner("X"):
        return -1
    if is_full():
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(False)
                board[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(True)
                board[i] = " "
                best_score = min(score, best_score)
        return best_score

# AI move
def ai_move():
    best_score = -math.inf
    move = 0
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    board[move] = "O"

# Main game loop
print("Tic-Tac-Toe Game!")
print("You are X, AI is O")
print("Positions are numbered 0 to 8")

while True:
    print_board()
    position = int(input("Enter your move in (0-8): "))

    if board[position] == " ":
        board[position] = "X"
    else:
        print("Invalid move!")
        continue

    if check_winner("X"):
        print_board()
        print("You Win!")
        break

    if is_full():
        print_board()
        print("Draw!")
        break

    ai_move()

    if check_winner("O"):
        print_board()
        print("AI Wins!")
        break

    if is_full():
        print_board()
        print("Draw!")
        break
