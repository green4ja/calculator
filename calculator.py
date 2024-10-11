import tkinter as tk
import re

class calculator():
    # Constructor
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Calculator")

        self.display = tk.Entry(self.window, width=30, borderwidth=5)
        self.display.grid(row=0, column=0, columnspan=4)

        self.new_entry = False  # Initialize new_entry

        # Buttons
        self.buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]

        # Create buttons
        self.create_buttons()

    # Create buttons
    def create_buttons(self):
        # Create buttons using a loop
        r = 1
        c = 0
        for button in self.buttons:
            tk.Button(self.window, text=button, width=10, height=3, command=lambda x=button: self.click(x)).grid(row=r, column=c)
            c += 1
            if c > 3:
                c = 0
                r += 1

    # Button click function
    def click(self, value):
        if value == "=":
            try:
                expression = self.display.get()
                tokens = re.split(r'(\D)', expression) # Split the expression into operands and operators
                tokens = [token.lstrip('0') if token.isdigit() else token for token in tokens] # Remove leading zeros from each operand
                expression = ''.join(tokens) # Reconstruct the expression
                result = eval(expression)  # Evaluate the expression
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
                self.new_entry = True
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
                self.new_entry = True
        elif value == "C":
            self.display.delete(0, tk.END)
            self.new_entry = False
        else:
            if self.new_entry:
                self.display.delete(0, tk.END)
                self.new_entry = False
            self.display.insert(tk.END, value)

