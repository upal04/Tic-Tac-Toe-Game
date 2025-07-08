import tkinter as tk  # Importing the tkinter module for GUI
from tkinter import messagebox  # Importing messagebox to show pop-up messages

# Function to check if there's a winner
def check_winner():
    # List of all winning combinations (rows, columns, diagonals)
    for combo in [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]:
        # Check if the same player occupies all 3 cells and they're not empty
        if buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == buttons[combo[2]]["text"] != "":
            # Highlight winning buttons in green
            buttons[combo[0]].config(bg="green")
            buttons[combo[1]].config(bg="green")
            buttons[combo[2]].config(bg="green")
            # Show message that the player has won
            messagebox.showinfo("Tic-Tac-Toe", f"Player {buttons[combo[0]]['text']} wins!")
            root.quit()  # Close the application (corrected from `.quite()` to `.quit()`)

def check_tie():
    # Check if all buttons are clicked and no winner
    if "" not in [buttons[i]["text"] for i in range(9)] and not winner:
        # Show message that it's a tie
        messagebox.showinfo("Tic-Tac-Toe", "It's a tie!")
        root.quit()

# Function to handle a button click
def button_click(index):
    # Check if button is not already clicked and game hasn't ended
    if buttons[index]["text"] == "" and not winner:
        # Set the button text to current player's symbol
        buttons[index]["text"] = current_player
        check_winner()  # Check if this move wins the game
        check_tie()  # Check if the game is a tie
        toggle_player()  # Switch to the next player

# Function to switch turns between players
def toggle_player():
    global current_player  # Use the global current_player variable
    # Switch between "X" and "O"
    current_player = "X" if current_player == "O" else "O"
    # Update the label to show whose turn it is
    label.config(text=f"Player {current_player}'s turn")

# Create the main application window
root = tk.Tk()
root.title("Tic-Tac-Toe")  # Set the window title

# Create 9 buttons for the game grid and store them in a list
buttons = [tk.Button(root, text="", font=("normal", 25), width=6, height=2,
                      command=lambda i=i: button_click(i)) for i in range(9)] #buttons = [  # Create a list named 'buttons' to store all 9 button widgets
   # tk.Button(  # Create a new Button widget using tkinter
    #    root,  # Parent widget where the button will be placed (main window)
     #   text="",  # Initial text on the button is empty ("" means blank button)
      #  font=("normal", 25),  # Set font style and size of text on button
       # width=6,  # Set width of button (in character units)
        #height=2,  # Set height of button (in character units)
        #command=lambda i=i: button_click(i)  # Define what happens when the button is clicked using lambda
        # lambda i=i ensures the current index 'i' is passed to button_click(i) correctly)
    #for i in range(9)  # Loop to create 9 buttons (indexes 0 to 8) and store them in the list]


# Place the buttons in a 3x3 grid layout
for i, button in enumerate(buttons):
    button.grid(row=i // 3, column=i % 3)

# Initialize the first player as "X"
current_player = "X"

# A flag to indicate if someone has already won (not yet used effectively)
winner = False

# Label to show which player's turn it is
label = tk.Label(root, text=f"Player {current_player}'s turn", font=("normal", 16))
label.grid(row=3, column=0, columnspan=3)  # Position the label below the grid

# Start the GUI event loop
root.mainloop()
