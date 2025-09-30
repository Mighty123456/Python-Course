import tkinter as tk

# Functions
def click(btn):
    if btn == "=":
        try:
            expression = entry.get()
            result = str(eval(expression))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif btn == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, btn)

# Main window
root = tk.Tk()
root.title("Calculator")

# Entry box
entry = tk.Entry(root, width=20, font=("Arial", 20), justify="right")
entry.grid(row=0, column=0, columnspan=4, pady=10)

# Button layout
buttons = [
    ["7", "8", "9", "+"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "*"],
    ["C", "0", "=", "/"]
]

# Create buttons
for r, row in enumerate(buttons, 1):
    for c, btn in enumerate(row):
        tk.Button(root, text=btn, width=5, height=2, font=("Arial", 18),
                  command=lambda b=btn: click(b)).grid(row=r, column=c, padx=3, pady=3)

root.mainloop()
