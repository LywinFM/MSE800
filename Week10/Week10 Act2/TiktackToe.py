# -----------------------------
# TIC TAC TOE — In Decomposition format
# -----------------------------

# 1. Create the board
def create_board():
    return [" "] * 9


# 2. Display the board
def display_board(board):
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")


# 3. Check if a move is valid
def is_valid_move(board, position):
    return board[position] == " "


# 4. Place a move
def make_move(board, position, player):
    board[position] = player


# 5. Check for a win
def check_winner(board, player):
    win_patterns = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]

    for pattern in win_patterns:
        if all(board[i] == player for i in pattern):
            return True
    return False


# 6. Check for a draw
def is_draw(board):
    return " " not in board


# 7. Switch player
def switch_player(player):
    return "O" if player == "X" else "X"


# 8. Main game loop
def play_game():
    board = create_board()
    current_player = "X"
    game_running = True

    while game_running:
        display_board(board)
        print(f"Player {current_player}'s turn.")

        try:
            position = int(input("Choose a position (1-9): ")) - 1
        except ValueError:
            print("Invalid input. Enter a number 1–9.")
            continue

        if position not in range(9):
            print("Position must be between 1 and 9.")
            continue

        if not is_valid_move(board, position):
            print("That spot is already taken.")
            continue

        make_move(board, position, current_player)

        if check_winner(board, current_player):
            display_board(board)
            print(f"🎉 Player {current_player} wins!")
            game_running = False
        elif is_draw(board):
            display_board(board)
            print("It's a draw!")
            game_running = False
        else:
            current_player = switch_player(current_player)


# 9. Start the game
play_game()
