import tkinter as tk

# Function to evaluate the expression
def evaluate():
    try:
        result = str(eval(entry.get()))  # Evaluate the expression
        entry.delete(0, tk.END)  # Clear the entry field
        entry.insert(tk.END, result)  # Insert the result
    except Exception:
        entry.delete(0, tk.END)  # Clear the entry field
        entry.insert(tk.END, "Error")  # Display error in case of invalid input

# Function to append value to the entry field
def button_click(value):
    current_text = entry.get()  # Get current text
    entry.delete(0, tk.END)  # Clear the entry field
    entry.insert(tk.END, current_text + str(value))  # Append the value

# Function to clear the entry field
def clear():
    entry.delete(0, tk.END)  # Clear the entry field

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Entry widget to display the expression and result
entry = tk.Entry(root, font=("Arial", 20), bd=10, relief="sunken", justify="right")
entry.grid(row=0, column=0, columnspan=4)

# Buttons for numbers and operations
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2),
    ('0', 4, 1), ('+', 1, 3), ('-', 2, 3),
    ('*', 3, 3), ('/', 4, 3), ('=', 4, 2),
    ('C', 4, 0), ('.', 3, 1)
]

# Create buttons dynamically based on the list
for (text, row, col) in buttons:
    if text == '=':
        button = tk.Button(root, text=text, font=("Arial", 20), bd=5, command=evaluate)
    elif text == 'C':
        button = tk.Button(root, text=text, font=("Arial", 20), bd=5, command=clear)
    else:
        button = tk.Button(root, text=text, font=("Arial", 20), bd=5, command=lambda value=text: button_click(value))
    
    button.grid(row=row, column=col, sticky="nsew")

# Run the main loop
root.mainloop()
