#Janhavi Beley 
#Tic Tac Toe Game #Introduction to Computer Science

# Tic Tac Toe board
board = [["*" for _ in range(3)] for _ in range(3)]

def prettyPrintGrid(grid):
    for row in grid:
        for col in row:
            print(col, end=' ')
        print()

def isFull(board):
    for row in board:
        if "*" in row:
            return False
    return True

def isWinner(board):
    for r in range(3):
        if (board[r][0] != '*') and (board[r][0] == board[r][1] == board[r][2]):
            return True

    for c in range(3):
        if (board[0][c] != '*') and (board[0][c] == board[1][c] == board[2][c]):
            return True

    if board[1][1] != '*':
        if (board[0][0] == board[1][1] == board[2][2]):
            return True
        elif (board[0][2] == board[1][1] == board[2][0]):
            return True

    return False

# Main game loop
current_player = "X"

print("Welcome to Tic Tac Toe!")

while True:
    prettyPrintGrid(board)

    row = int(input(f"Player {current_player}, enter the row (0, 1, or 2): "))
    col = int(input(f"Player {current_player}, enter the column (0, 1, or 2): "))

    if board[row][col] == "*":
        board[row][col] = current_player
    else:
        print("Invalid move. That spot is already taken.")
        continue

    if isWinner(board):
        prettyPrintGrid(board)
        print(f"Player {current_player} wins!")
        break
    elif isFull(board):
        prettyPrintGrid(board)
        print("It's a draw!")
        break

    current_player = "X" if current_player == "O" else "O"