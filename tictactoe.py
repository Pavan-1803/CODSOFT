import random

# Create board
board = [" " for _ in range(9)]

# Print board
def print_board():
    print()
    for i in range(3):
        print(board[i*3], "|", board[i*3+1], "|", board[i*3+2])
        if i < 2:
            print("--+---+--")
    print()

# Check for winner
def check_winner(player):
    win = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    for combo in win:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

# Check for draw
def is_draw():
    return " " not in board

# Player move
def player_move():
    while True:
        try:
            move = int(input("Choose your move (1-9): ")) - 1
            if board[move] == " ":
                board[move] = "X"
                break
            else:
                print("Place already taken!")
        except:
            print("Invalid input. Try again.")

# Computer move
def computer_move():
    empty = [i for i, x in enumerate(board) if x == " "]
    move = random.choice(empty)
    board[move] = "O"

# Game loop
def play():
    print("Tic-Tac-Toe Game: You = X, Computer = O")
    print_board()

    while True:
        player_move()
        print_board()
        if check_winner("X"):
            print("You win!")
            break
        if is_draw():
            print("It's a draw!")
            break

        print("Computer's turn...")
        computer_move()
        print_board()
        if check_winner("O"):
            print("Computer wins!")
            break
        if is_draw():
            print("It's a draw!")
            break

play()
