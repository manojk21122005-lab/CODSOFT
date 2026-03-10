import tkinter as tk

root = tk.Tk()
root.title("Calculator")
root.geometry("340x480")
root.configure(bg="#1e1e2e")
root.resizable(False, False)

expr = tk.StringVar(value="")

display = tk.Entry(root, textvariable=expr, font=("Helvetica", 24, "bold"),
                   justify="right", bg="#313244", fg="white", relief="flat",
                   state="readonly", readonlybackground="#313244")
display.pack(fill="x", padx=10, pady=10, ipady=15)

def click(val):
    if val == "C":
        expr.set("")
    elif val == "⌫":
        expr.set(expr.get()[:-1])
    elif val == "=":
        try:
            expr.set(eval(expr.get().replace("×","*").replace("÷","/").replace("−","-")))
        except:
            expr.set("Error")
    else:
        expr.set(expr.get() + str(val))

buttons = [
    ["C", "⌫", "%", "÷"],
    ["7", "8", "9", "×"],
    ["4", "5", "6", "−"],
    ["1", "2", "3", "+"],
    ["0", ".", "", "="],
]

for row in buttons:
    f = tk.Frame(root, bg="#1e1e2e")
    f.pack(fill="x", padx=10, pady=3)
    for b in row:
        color = "#f38ba8" if b in ("=", "÷", "×", "−", "+") else "#45475a"
        tk.Button(f, text=b, font=("Helvetica", 16, "bold"), bg=color, fg="white",
                  relief="flat", width=5, height=2, cursor="hand2",
                  command=lambda v=b: click(v)).pack(side="left", expand=True, fill="x", padx=3)

root.mainloop()
