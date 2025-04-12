# Initialize board
board = [" " for _ in range(9)]

# Function to print the board
def print_board():
    print("\n")
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print("\n")

# Function to check for a win
def check_win(player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],  # rows
        [0,3,6], [1,4,7], [2,5,8],  # cols
        [0,4,8], [2,4,6]            # diagonals
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

# Game loop
current_player = "X"
game_running = True

print("🎮 Welcome to Tic Tac Toe!")
print("Player 1: X | Player 2: O")
print("Enter position from 1 to 9 as shown below:")
print("1 | 2 | 3\n4 | 5 | 6\n7 | 8 | 9")
print_board()

while game_running:
    try:
        move = int(input(f"Player {current_player}, enter your move (1-9): ")) - 1
        if board[move] == " ":
            board[move] = current_player
            print_board()

            if check_win(current_player):
                print(f"🏆 Player {current_player} wins!")
                game_running = False
            elif " " not in board:
                print("🤝 It's a draw!")
                game_running = False
            else:
                current_player = "O" if current_player == "X" else "X"
        else:
            print("That position is already taken. Try again.")
    except (ValueError, IndexError):
        print("Invalid input. Please choose a number from 1 to 9.")

