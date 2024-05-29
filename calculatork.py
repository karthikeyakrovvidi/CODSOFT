import tkinter as tk
from tkinter import messagebox

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.root.geometry("300x400")
        self.root.configure(bg="#f0f8ff")

        self.create_widgets()

    def create_widgets(self):
        self.display_var = tk.StringVar()
        self.display_var.set("")

        self.display_label = tk.Label(self.root, textvariable=self.display_var, font=("Helvetica", 20), bg="#f0f8ff", anchor="e")
        self.display_label.pack(expand=True, fill="both")

        self.buttons_frame = tk.Frame(self.root, bg="#f0f8ff")
        self.buttons_frame.pack(expand=True, fill="both")

        buttons_data = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3)
        ]

        for text, row, col in buttons_data:
            button = tk.Button(self.buttons_frame, text=text, font=("Helvetica", 14), bg="#4caf50", fg="white", padx=10, pady=10, command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)
        
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_rowconfigure(2, weight=1)
        self.root.grid_rowconfigure(3, weight=1)
        self.root.grid_rowconfigure(4, weight=1)

        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_columnconfigure(2, weight=1)
        self.root.grid_columnconfigure(3, weight=1)

    def on_button_click(self, char):
        if char == "=":
            try:
                result = eval(self.display_var.get())
                self.display_var.set(str(result))
            except Exception as e:
                messagebox.showerror("Error", f"Invalid expression: {e}")
        elif char == "C":
            self.display_var.set("")
        else:
            self.display_var.set(self.display_var.get() + char)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
