import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import ttk

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.root.geometry("450x500")
        self.root.config(bg="#000000")  # Black background color

        self.tasks = []

        style = ttk.Style()
        style.theme_use("clam")  # Use the 'clam' theme for ttk

        # Configure custom styles
        style.configure("TButton",
                        font=("Helvetica", 12),
                        padding=6,
                        background="#5dade2",
                        foreground="white",
                        borderwidth=0)
        style.map("TButton",
                  background=[('active', '#3498db'), ('pressed', '#2e86c1')])
        style.configure("TLabel", font=("Helvetica", 14), background="#000000", foreground="white")
        style.configure("TEntry", font=("Helvetica", 12))
        style.configure("TListbox", font=("Helvetica", 12))

        self.frame = tk.Frame(self.root, bg="#000000")
        self.frame.pack(pady=20)

        self.title = ttk.Label(self.frame, text="To-Do List", font=("Helvetica", 24, "bold"))
        self.title.pack(pady=10)

        self.task_entry = ttk.Entry(self.frame, width=40)
        self.task_entry.pack(pady=5)

        self.add_button = ttk.Button(self.frame, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)

        self.tasks_listbox = tk.Listbox(self.frame, width=50, height=10, font=("Helvetica", 12), selectmode=tk.SINGLE, bg="#333333", fg="white", bd=0, highlightthickness=0)
        self.tasks_listbox.pack(pady=5)

        self.button_frame = tk.Frame(self.frame, bg="#000000")
        self.button_frame.pack(pady=10)

        self.delete_button = ttk.Button(self.button_frame, text="Delete Task", command=self.delete_task)
        self.delete_button.grid(row=0, column=0, padx=5)

        self.edit_button = ttk.Button(self.button_frame, text="Edit Task", command=self.edit_task)
        self.edit_button.grid(row=0, column=1, padx=5)

        self.mark_done_button = ttk.Button(self.button_frame, text="Mark as Done", command=self.mark_as_done)
        self.mark_done_button.grid(row=0, column=2, padx=5)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append({"task": task, "done": False})
            self.update_tasks()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def update_tasks(self):
        self.tasks_listbox.delete(0, tk.END)
        for task_info in self.tasks:
            task = task_info["task"]
            if task_info["done"]:
                task = f"{task} ✔"
            self.tasks_listbox.insert(tk.END, task)

    def delete_task(self):
        try:
            selected_task_index = self.tasks_listbox.curselection()[0]
            self.tasks.pop(selected_task_index)
            self.update_tasks()
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to delete.")

    def edit_task(self):
        try:
            selected_task_index = self.tasks_listbox.curselection()[0]
            task_info = self.tasks[selected_task_index]
            old_task = task_info["task"]
            new_task = simpledialog.askstring("Edit Task", f"Edit task '{old_task}':")
            if new_task:
                self.tasks[selected_task_index]["task"] = new_task
                self.update_tasks()
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to edit.")

    def mark_as_done(self):
        try:
            selected_task_index = self.tasks_listbox.curselection()[0]
            self.tasks[selected_task_index]["done"] = True
            self.update_tasks()
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to mark as done.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()