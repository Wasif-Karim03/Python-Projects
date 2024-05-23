import tkinter as tk
from tkinter import messagebox

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.geometry("400x600")
        self.configure(bg='lightgray')

        self.result_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Create display
        display_frame = tk.Frame(self, bg='white')
        display_frame.pack(expand=True, fill='both')
        
        display_entry = tk.Entry(display_frame, textvariable=self.result_var, font=('Arial', 24), justify='right', bd=0, bg='white', fg='black')
        display_entry.pack(expand=True, fill='both')

        # Create buttons
        buttons_frame = tk.Frame(self)
        buttons_frame.pack(expand=True, fill='both')

        buttons = [
            '7', '8', '9', '/', 
            '4', '5', '6', '*', 
            '1', '2', '3', '-', 
            '0', '.', '=', '+',
            '%', 'C'
        ]

        rows = 5
        cols = 4

        for i in range(rows):
            for j in range(cols):
                index = i * cols + j
                if index < len(buttons):
                    button = tk.Button(buttons_frame, text=buttons[index], font=('Arial', 18), fg='black', bg='lightblue', bd=1, command=lambda x=buttons[index]: self.on_button_click(x))
                    button.grid(row=i, column=j, sticky='nsew')

        for i in range(rows):
            buttons_frame.grid_rowconfigure(i, weight=1)
        for j in range(cols):
            buttons_frame.grid_columnconfigure(j, weight=1)

    def on_button_click(self, char):
        if char == 'C':
            self.result_var.set("")
        elif char == '=':
            try:
                result = eval(self.result_var.get())
                self.result_var.set(result)
            except Exception as e:
                messagebox.showerror("Error", "Invalid Expression")
                self.result_var.set("")
        else:
            current_text = self.result_var.get()
            new_text = current_text + str(char)
            self.result_var.set(new_text)

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()