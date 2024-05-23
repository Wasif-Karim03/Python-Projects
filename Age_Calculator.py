import tkinter as tk
from datetime import datetime

def calculate_age():
    birthdate = entry.get()
    try:
        birthdate = datetime.strptime(birthdate, "%Y-%m-%d")
        today = datetime.today()
        
        # Calculate the difference
        delta = today - birthdate
        
        # Calculate years, months, and days
        years = today.year - birthdate.year
        if today.month < birthdate.month or (today.month == birthdate.month and today.day < birthdate.day):
            years -= 1
        
        months = (today.year - birthdate.year) * 12 + today.month - birthdate.month
        if today.day < birthdate.day:
            months -= 1
        
        days = delta.days
        hours = days * 24 + today.hour - birthdate.hour
        minutes = hours * 60 + today.minute - birthdate.minute
        seconds = minutes * 60 + today.second - birthdate.second
        
        result_text.set(
            f"You are {years} years old.\n\n"
            f"That's {months} months,\n"
            f"{days} days,\n"
            f"{hours} hours,\n"
            f"{minutes} minutes,\n"
            f"and {seconds} seconds old."
        )
    except ValueError:
        result_text.set("Please enter a valid date in YYYY-MM-DD format.")

# Create the main window
root = tk.Tk()
root.title("Age Calculator")
root.geometry("400x300")

# Create and place the widgets
frame = tk.Frame(root, padx=20, pady=20)
frame.pack(expand=True)

label = tk.Label(frame, text="Enter your birthdate (YYYY-MM-DD):")
label.grid(row=0, column=0, pady=10)

entry = tk.Entry(frame, width=20)
entry.grid(row=1, column=0, pady=5)

button = tk.Button(frame, text="Calculate Age", command=calculate_age, bg="blue", fg="black")
button.grid(row=2, column=0, pady=10)

result_text = tk.StringVar()
result_label = tk.Label(frame, textvariable=result_text, justify="left")
result_label.grid(row=3, column=0, pady=10)

# Start the main event loop
root.mainloop()