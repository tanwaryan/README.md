import tkinter as tk
from tkinter import messagebox

def click(button_text):
    if button_text == "=":
        try:
            result = str(eval(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except ZeroDivisionError:
            messagebox.showerror("Error", "Cannot divide by zero!")
            entry.delete(0, tk.END)
        except Exception:
            messagebox.showerror("Error", "Invalid Input!")
            entry.delete(0, tk.END)
    elif button_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button_text)

root = tk.Tk()
root.title("Tkinter Calculator")
root.geometry("300x400")
root.resizable(False, False)

entry = tk.Entry(root, font=("Arial", 20), borderwidth=2, relief="solid")
entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
    ("C", 5, 0)
]

for (text, row, col) in buttons:
    btn = tk.Button(root, text=text, width=6, height=2, font=("Arial", 14),
                    command=lambda t=text: click(t))
    btn.grid(row=row, column=col, padx=5, pady=5)

root.mainloop()
