# Tic Tac Toe Game in Python

def print_board(board):
    # Print the current state of the board
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Check if the player has won horizontally, vertically, or diagonally
    for i in range(3):
        if all([board[i][j] == player for j in range(3)]):  # Check rows
            return True
        if all([board[j][i] == player for j in range(3)]):  # Check columns
            return True
    if all([board[i][i] == player for i in range(3)]):  # Check diagonal (top-left to bottom-right)
        return True
    if all([board[i][2-i] == player for i in range(3)]):  # Check diagonal (top-right to bottom-left)
        return True
    return False

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ['X', 'O']
    turn = 0

    while True:
        current_player = players[turn % 2]

        print(f"Player {current_player}'s turn.")
        print_board(board)

        # Get player's move
        while True:
            try:
                row = int(input("Enter row (0-2): "))
                col = int(input("Enter column (0-2): "))
                if board[row][col] == " ":
                    break
                else:
                    print("That spot is already taken! Try again.")
            except ValueError:
                print("Invalid input! Please enter a number.")
            except IndexError:
                print("Invalid input! Please enter a number between 0 and 2.")

        # Place the player's move on the board
        board[row][col] = current_player

        # Check if the current player wins
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        # Check if the board is full (tie game)
        if all([cell != " " for row in board for cell in row]):
            print_board(board)
            print("It's a tie!")
            break

        turn += 1

if __name__ == "__main__":
    tic_tac_toe()
