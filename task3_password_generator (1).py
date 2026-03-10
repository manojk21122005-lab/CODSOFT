import tkinter as tk
import tkinter.messagebox
import random, string

root = tk.Tk()
root.title("Password Generator")
root.geometry("420x480")
root.configure(bg="#0f172a")
root.resizable(False, False)

tk.Label(root, text="🔐 Password Generator", font=("Helvetica", 16, "bold"),
         bg="#0f172a", fg="#38bdf8").pack(pady=12)

# Length slider
tk.Label(root, text="Password Length:", font=("Helvetica", 11),
         bg="#0f172a", fg="white").pack()

length_var = tk.IntVar(value=12)
length_label = tk.Label(root, text="12", font=("Helvetica", 11, "bold"),
                         bg="#0f172a", fg="#38bdf8")
length_label.pack()

def update_label(v):
    length_label.config(text=str(v))

tk.Scale(root, from_=4, to=32, orient="horizontal", variable=length_var,
         bg="#0f172a", fg="white", troughcolor="#1e293b",
         highlightthickness=0, command=update_label).pack(fill="x", padx=40)

# Character type checkboxes
tk.Label(root, text="Include Character Types:", font=("Helvetica", 11),
         bg="#0f172a", fg="#94a3b8").pack(pady=(10, 2))

use_upper  = tk.BooleanVar(value=True)
use_lower  = tk.BooleanVar(value=True)
use_digits = tk.BooleanVar(value=True)
use_special = tk.BooleanVar(value=False)

options_frame = tk.Frame(root, bg="#0f172a")
options_frame.pack()

for text, var, color in [
    ("🔠 Uppercase (A-Z)", use_upper,  "#a78bfa"),
    ("🔡 Lowercase (a-z)", use_lower,  "#34d399"),
    ("🔢 Numbers (0-9)",   use_digits, "#fbbf24"),
    ("🔣 Special (!@#$)",  use_special,"#f87171"),
]:
    tk.Checkbutton(options_frame, text=text, variable=var,
                   font=("Helvetica", 11), bg="#0f172a", fg=color,
                   activebackground="#0f172a", selectcolor="#1e293b",
                   activeforeground=color).pack(anchor="w", padx=40)

# Suggestion label
suggest_var = tk.StringVar(value="")
tk.Label(root, textvariable=suggest_var, font=("Helvetica", 9),
         bg="#0f172a", fg="#f87171", wraplength=380).pack(pady=4)

# Password display
result_var = tk.StringVar(value="Click Generate!")
tk.Entry(root, textvariable=result_var, font=("Courier", 13), justify="center",
         bg="#1e293b", fg="#4ade80", relief="flat", state="readonly",
         readonlybackground="#1e293b").pack(fill="x", padx=30, pady=8, ipady=8)

# Strength bar
strength_var = tk.StringVar(value="")
strength_label = tk.Label(root, textvariable=strength_var,
                           font=("Helvetica", 10, "bold"), bg="#0f172a")
strength_label.pack()

def check_suggestions():
    tips = []
    if not use_upper.get():  tips.append("Add Uppercase for stronger password")
    if not use_lower.get():  tips.append("Add Lowercase for better readability")
    if not use_digits.get(): tips.append("Add Numbers to increase complexity")
    if not use_special.get():tips.append("Add Special characters for maximum strength")
    suggest_var.set("💡 Tip: " + " | ".join(tips) if tips else "✅ Great combination selected!")

def get_strength(pwd):
    score = sum([
        any(c.isupper() for c in pwd),
        any(c.islower() for c in pwd),
        any(c.isdigit() for c in pwd),
        any(c in string.punctuation for c in pwd),
        len(pwd) >= 16
    ])
    levels = {
        5: ("💪 Very Strong", "#4ade80"),
        4: ("✅ Strong",      "#a3e635"),
        3: ("⚠️ Medium",     "#fbbf24"),
        2: ("❌ Weak",        "#f87171"),
        1: ("🚨 Very Weak",   "#ef4444"),
    }
    return levels.get(score, ("🚨 Very Weak", "#ef4444"))

def generate():
    check_suggestions()
    chars = ""
    if use_upper.get():   chars += string.ascii_uppercase
    if use_lower.get():   chars += string.ascii_lowercase
    if use_digits.get():  chars += string.digits
    if use_special.get(): chars += string.punctuation

    if not chars:
        tkinter.messagebox.showwarning("No Selection", "Please select at least one character type!")
        return

    pwd = ''.join(random.choices(chars, k=length_var.get()))
    result_var.set(pwd)

    text, color = get_strength(pwd)
    strength_var.set(f"Strength: {text}")
    strength_label.config(fg=color)

def copy():
    pwd = result_var.get()
    if pwd != "Click Generate!":
        root.clipboard_clear()
        root.clipboard_append(pwd)
        tkinter.messagebox.showinfo("Copied!", "Password copied to clipboard!")

btn_frame = tk.Frame(root, bg="#0f172a")
btn_frame.pack(pady=8)
tk.Button(btn_frame, text="⚡ Generate", font=("Helvetica", 12, "bold"),
          bg="#38bdf8", fg="#0f172a", relief="flat", padx=15, pady=6,
          cursor="hand2", command=generate).pack(side="left", padx=10)
tk.Button(btn_frame, text="📋 Copy", font=("Helvetica", 12),
          bg="#1e293b", fg="white", relief="flat", padx=15, pady=6,
          cursor="hand2", command=copy).pack(side="left")

root.mainloop()
