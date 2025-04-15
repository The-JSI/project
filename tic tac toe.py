# Create an empty board
def create_board():
    return {
        'a1': ' ', 'b1': ' ', 'c1': ' ',
        'a2': ' ', 'b2': ' ', 'c2': ' ',
        'a3': ' ', 'b3': ' ', 'c3': ' ',
    }

# Print the board
def print_board(board):
    print("    a   b   c")
    print(f"1   {board['a1']} | {board['b1']} | {board['c1']}")
    print("   -----------")
    print(f"2   {board['a2']} | {board['b2']} | {board['c2']}")
    print("   -----------")
    print(f"3   {board['a3']} | {board['b3']} | {board['c3']}")

# Handle player move
def player_input(board, player_mark):
    while True:
        move = input(f"Player {player_mark}, enter your move (e.g. a1): ").lower()
        if move in board and board[move] == ' ':
            board[move] = player_mark
            break
        else:
            print("Invalid move. Try again.")

# Check for winning combinations
def check_win(board, player_mark):
    win_combos = [
        ['a1', 'b1', 'c1'],  # Row 1
        ['a2', 'b2', 'c2'],  # Row 2
        ['a3', 'b3', 'c3'],  # Row 3
        ['a1', 'a2', 'a3'],  # Column A
        ['b1', 'b2', 'b3'],  # Column B
        ['c1', 'c2', 'c3'],  # Column C
        ['a1', 'b2', 'c3'],  # Diagonal \
        ['c1', 'b2', 'a3'],  # Diagonal /
    ]
    for combo in win_combos:
        if all(board[cell] == player_mark for cell in combo):
            return True
    return False

# Main game logic
def play_game():
    board = create_board()
    current_player = 'X'
    
    for turn in range(9):  # Max 9 turns
        print_board(board)
        player_input(board, current_player)
        
        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            return
        
        # Switch player
        current_player = 'O' if current_player == 'X' else 'X'
    
    print_board(board)
    print("It's a tie!")

# Start the game
play_game()