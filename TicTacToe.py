import tkinter as tk  # Importing tkinter module
from tkinter import messagebox  # Allows us to display message boxes

window = tk.Tk()  # Creating a window object
window.title("Tic Tac Toe")  # Setting the title of the window

# Creating a 3x3 grid of buttons
buttons = [[None, None, None],
           [None, None, None],
           [None, None, None]]

current_player = "X"  # Setting the current player to "X"


def button_click(row, col):
    global current_player

    if buttons[row][col]["text"] == "":  # Checks if button is empty
        buttons[row][col]["text"] = current_player

        # If there is a winner, it displays a message and calls for a reset
        if check_winner():
            messagebox.showinfo("Game Over!", f"player {current_player} wins!")
            reset_game()


        # If all buttons are filled with no winner, displays a draw message and resets
        elif all(buttons[r][c]["text"] != "" for r in range(3) for c in range(3)):
            messagebox.showinfo("Game Over!", "It's a draw")
            reset_game()

        else:
            current_player = "O" if current_player == "X" else "X"


# Function checks for winner by running through all options to win the game
def check_winner():
    for row in range(3):
        # Checks if all three buttons are taken in rows [0],[1], and [2]
        if buttons[row][0]["text"] == buttons[row][1]["text"] == buttons[row][2]["text"] != "":
            return True

        # Checks if all three buttons are taken in columns [0],[1], and [2]
    for col in range(3):
        if buttons[0][col]["text"] == buttons[1][col]["text"] == buttons[2][col]["text"] != "":
            return True

        # Checks diagonals for possible win
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        return True
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        return True

    return False


# Function resets the game
def reset_game():
    global current_player
    current_player = "X"
    for row in range(3):  # Clears all buttons
        for col in range(3):
            buttons[row][col]["text"] = ""


for row in range(3):  # Creates the buttons
    for col in range(3):
        buttons[row][col] = tk.Button(window, text="", font=('normal', 40), width=5, height=2,
                                      command=(lambda r=row, c=col: button_click(r, c)))
        buttons[row][col].grid(row=row, column=col)

window.mainloop()  # Runs the window
