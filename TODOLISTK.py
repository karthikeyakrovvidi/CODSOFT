import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        self.root.geometry("400x400")
        self.root.configure(bg="#d1f7ff")

        self.tasks = []

        self.title_label = tk.Label(root, text="To-Do List", font=("Helvetica", 18), bg="#d1f7ff")
        self.title_label.pack(pady=10)

        self.task_frame = tk.Frame(root, bg="#d1f7ff")
        self.task_frame.pack()

        self.task_entry = tk.Entry(root, width=30)
        self.task_entry.pack(pady=5)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task, bg="#00aaff", fg="white")
        self.add_button.pack(pady=5)

        self.task_listbox = tk.Listbox(root, width=50, height=10, bg="#ffffff", fg="black", selectbackground="#00aaff")
        self.task_listbox.pack(pady=10)

        self.update_button = tk.Button(root, text="Update Task", command=self.update_task, bg="#00aaff", fg="white")
        self.update_button.pack(pady=5)

        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task, bg="#ff4040", fg="white")
        self.delete_button.pack(pady=5)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_task_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def update_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            new_task = self.task_entry.get()
            if new_task:
                self.tasks[selected_task_index[0]] = new_task
                self.update_task_listbox()
                self.task_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Warning", "You must enter a task.")
        else:
            messagebox.showwarning("Warning", "You must select a task to update.")

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            del self.tasks[selected_task_index[0]]
            self.update_task_listbox()
        else:
            messagebox.showwarning("Warning", "You must select a task to delete.")

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
