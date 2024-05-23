import tkinter as tk
from tkinter import messagebox

# Initialize main window
root = tk.Tk()
root.title("Tic Tac Toe")

# Set up the board
board = [" " for _ in range(9)]
current_player = "X"  # Player starts first

# Function to check for a win
def check_win(player):
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]  # diagonals
    ]
    for combo in win_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False

# Function to check for a tie
def check_tie():
    return all(space != " " for space in board)

# Minimax algorithm to find the best move
def minimax(is_maximizing):
    if check_win("O"):
        return 1
    elif check_win("X"):
        return -1
    elif check_tie():
        return 0
    
    if is_maximizing:
        best_score = -float('inf')
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(False)
                board[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(True)
                board[i] = " "
                best_score = min(score, best_score)
        return best_score

# Function for computer's move
def computer_move():
    best_score = -float('inf')
    best_move = None
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False)
            board[i] = " "
            if score > best_score:
                best_score = score
                best_move = i
    board[best_move] = "O"
    buttons[best_move].config(text="O", state="disabled")
    if check_win("O"):
        messagebox.showinfo("Game Over", "Computer wins!")
        root.quit()
    elif check_tie():
        messagebox.showinfo("Game Over", "It's a tie!")
        root.quit()

# Function to handle player's move
def player_move(index):
    if board[index] == " ":
        board[index] = "X"
        buttons[index].config(text="X", state="disabled")
        if check_win("X"):
            messagebox.showinfo("Game Over", "You win!")
            root.quit()
        elif check_tie():
            messagebox.showinfo("Game Over", "It's a tie!")
            root.quit()
        else:
            computer_move()

# Create buttons
buttons = []
for i in range(9):
    button = tk.Button(root, text=" ", font=("Arial", 20), width=5, height=2,
                       command=lambda i=i: player_move(i))
    button.grid(row=i // 3, column=i % 3)
    buttons.append(button)

# Start the main loop
root.mainloop()