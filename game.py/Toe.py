import tkinter as tk
from tkinter import messagebox

# Function to check if someone has won
def check_winner():
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            return buttons[row][0]['text']
    for col in range(3):
        if buttons[0][col]['text'] == buttons[1][col]['text'] == buttons[2][col]['text'] != "":
            return buttons[0][col]['text']
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        return buttons[0][0]['text']
    if buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        return buttons[0][2]['text']
    return None

# Function to handle button click events
def button_click(row, col):
    global player_turn, game_over
    if buttons[row][col]['text'] == "" and not game_over:
        buttons[row][col].config(text=player_turn)
        winner = check_winner()
        if winner:
            messagebox.showinfo("Game Over", f"Player {winner} wins!")
            game_over = True
        elif all(button['text'] != "" for row in buttons for button in row):
            messagebox.showinfo("Game Over", "It's a draw!")
            game_over = True
        else:
            switch_turn()

# Function to switch the player's turn
def switch_turn():
    global player_turn
    player_turn = 'O' if player_turn == 'X' else 'X'

# Reset the game
def reset_game():
    global game_over, player_turn
    player_turn = 'X'
    game_over = False
    for row in range(3):
        for col in range(3):
            buttons[row][col].config(text="")

# Initialize the main window
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Global variables
player_turn = 'X'
game_over = False

# Create buttons for the grid
buttons = [[tk.Button(root, text="", font=('normal', 40), width=5, height=2,
                      command=lambda row=row, col=col: button_click(row, col))
            for col in range(3)] for row in range(3)]

# Place the buttons on the grid
for row in range(3):
    for col in range(3):
        buttons[row][col].grid(row=row, column=col)

# Reset button (placed below the grid)
reset_button = tk.Button(root, text="Reset Game", font=('normal', 20), command=reset_game)
reset_button.grid(row=3, column=0, columnspan=3, pady=10)

# Run the main loop
root.mainloop()
