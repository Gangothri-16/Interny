def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 10)

def check_winner(board,player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all (board[row][col]==player for row in range(3)):
            return True
    if all (board[i][i]==player for i in range(3)):
        return True
    if all (board[i][2-i]==player for i in range(3)):
        return True
    return False

def is_draw(board):
    for row in board:
        for cell in row:
            if cell == ' ':
                return False
    return True
def main():
    board = [[' 'for _ in range(3)] for _ in range(3)]
    players = ['X','O']
    turn = 0
    print("Welcome to tic-tac-toe!")
    while True:
        current_player = players[turn % 2]
        print_board(board)
        print(f"player{current_player}'s turn")
        row = int(input("Enter row(0,1,2):"))
        col = int(input("Enter column(0,1,2):"))
        if board[row][col]!= ' ':
            print("cell already occupied.Try again.")
            continue
        board[row][col] = current_player
        if check_winner(board,current_player):
            print_board(board)
            print(f"player{current_player} wins!")
            break
        elif is_draw(board):
            print_board(board)
            print("It's a draw!")
            break
        turn += 1
if __name__ == "__main__":
    main()
