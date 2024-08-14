import random

board = ["-","-","-",
         "-","-","-",
         "-","-","-"]

current_player = "X"

#printing game board
def print_board(board):
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("---+---+---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("---+---+---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])

#taking input from user
def player_input(board):
    global current_player
    inp=int(input("Enter your position between 1-9:"))
    if inp>=1 and inp<=9 and board[inp-1] == "-":
        board[inp-1]= current_player
        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"
    else:
        print("This position is not available!")

#to check win or tie
def check_win(board):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] != "-":
            return board[condition[0]]
    if "-" not in board:
        return "Tie"
    return False

def minimax(board, depth, is_maximizing):
    result = check_win(board)
    if result:
        if result == "Tie":
            return 0
        elif result == "X":
            return -1
        else:
            return 1
    if is_maximizing:
        best_score = -1000
        for i in range(9):
            if board[i] == "-":
                board[i] = "O"
                score = minimax(board, depth + 1, False)
                board[i] = "-"
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = 1000
        for i in range(9):
            if board[i] == "-":
                board[i] = "X"
                score = minimax(board, depth + 1, True)
                board[i] = "-"
                best_score = min(score, best_score)
        return best_score

def agent_move(board):
    global current_player
    best_score = -1000
    best_move = 0
    for i in range(9):
        if board[i] == "-":
            board[i] = "O"
            score = minimax(board, 0, False)
            board[i] = "-"
            if score > best_score:
                best_score = score
                best_move = i
    board[best_move] = "O"
    current_player = "X"

gameRunning = True
while gameRunning:
    print_board(board)
    player_input(board)
    result = check_win(board)
    if result:
        print_board(board)
        if result == "Tie":
            print("It's a tie!")
        else:
            print("Player " + result + " wins!")
        gameRunning = False
    else:
        agent_move(board)
        result = check_win(board)
        if result:
            print_board(board)
            if result == "Tie":
                print("It's a tie!")
            else:
                print("Player" + result + " wins!")
            gameRunning = False