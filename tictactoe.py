import math

HUMAN = "X"
AI = "O"

# Create board
def create_board():
    return [" " for _ in range(9)]

def display(board):
    print("\n")
    for i in range(3):
        print(" | ".join(board[i*3:(i+1)*3]))
        if i < 2:
            print("--+---+--")
    print("\n")

def available_moves(board):
    return [i for i, spot in enumerate(board) if spot == " "]

def is_winner(board, player):
    win_patterns = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]
    return any(board[a] == board[b] == board[c] == player for a,b,c in win_patterns)

def is_terminal(board):
    return is_winner(board, HUMAN) or is_winner(board, AI) or " " not in board

# Alpha-Beta Minimax
def minimax(board, depth, alpha, beta, maximizing):
    if is_winner(board, AI):
        return 10 - depth
    if is_winner(board, HUMAN):
        return depth - 10
    if " " not in board:
        return 0

    if maximizing:
        max_eval = -math.inf
        for move in available_moves(board):
            board[move] = AI
            eval = minimax(board, depth + 1, alpha, beta, False)
            board[move] = " "
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = math.inf
        for move in available_moves(board):
            board[move] = HUMAN
            eval = minimax(board, depth + 1, alpha, beta, True)
            board[move] = " "
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

def get_best_move(board):
    best_score = -math.inf
    best_move = None

    for move in available_moves(board):
        board[move] = AI
        score = minimax(board, 0, -math.inf, math.inf, False)
        board[move] = " "
        if score > best_score:
            best_score = score
            best_move = move

    return best_move

# Main game loop
def play():
    board = create_board()
    print("You are X, AI is O")
    display(board)

    while True:
        # Human move
        try:
            move = int(input("Enter your move (0-8): "))
        except:
            print("Invalid input")
            continue

        if move not in available_moves(board):
            print("Invalid move!")
            continue

        board[move] = HUMAN
        display(board)

        if is_winner(board, HUMAN):
            print("You win!")
            break
        if is_terminal(board):
            print("Draw!")
            break

        # AI move
        ai_move = get_best_move(board)
        board[ai_move] = AI
        print(f"AI plays at {ai_move}")
        display(board)

        if is_winner(board, AI):
            print("AI wins!")
            break
        if is_terminal(board):
            print("Draw!")
            break

if __name__ == "__main__":
    play()