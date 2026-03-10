import tkinter as tk
from tkinter import messagebox
import random
import string

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("CodSoft - Password Generator")
        self.root.geometry("460x500")
        self.root.configure(bg="#0f172a")
        self.root.resizable(False, False)
        self.build_ui()

    def build_ui(self):
        # Header
        tk.Label(self.root, text="🔐 Password Generator", font=("Helvetica", 20, "bold"),
                 bg="#0f172a", fg="#38bdf8").pack(pady=20)

        # Length slider
        length_frame = tk.Frame(self.root, bg="#0f172a")
        length_frame.pack(fill="x", padx=30)

        tk.Label(length_frame, text="Password Length:", font=("Helvetica", 12),
                 bg="#0f172a", fg="#94a3b8").pack(anchor="w")

        slider_row = tk.Frame(length_frame, bg="#0f172a")
        slider_row.pack(fill="x")

        self.length_var = tk.IntVar(value=16)
        self.length_label = tk.Label(slider_row, text="16", font=("Helvetica", 14, "bold"),
                                     bg="#0f172a", fg="#38bdf8", width=3)
        self.length_label.pack(side="right")

        slider = tk.Scale(slider_row, from_=4, to=64, orient="horizontal",
                          variable=self.length_var, bg="#0f172a", fg="#94a3b8",
                          troughcolor="#1e293b", activebackground="#38bdf8",
                          highlightthickness=0, showvalue=False,
                          command=lambda v: self.length_label.config(text=v))
        slider.pack(fill="x", expand=True)

        # Options
        options_frame = tk.LabelFrame(self.root, text=" Character Types ",
                                       font=("Helvetica", 11), bg="#0f172a",
                                       fg="#94a3b8", bd=1, relief="groove",
                                       labelanchor="n")
        options_frame.pack(fill="x", padx=30, pady=15)

        self.use_upper = tk.BooleanVar(value=True)
        self.use_lower = tk.BooleanVar(value=True)
        self.use_digits = tk.BooleanVar(value=True)
        self.use_special = tk.BooleanVar(value=True)

        options = [
            ("Uppercase (A-Z)", self.use_upper),
            ("Lowercase (a-z)", self.use_lower),
            ("Digits (0-9)", self.use_digits),
            ("Special (!@#$...)", self.use_special),
        ]

        for i, (label, var) in enumerate(options):
            row = i // 2
            col = i % 2
            tk.Checkbutton(options_frame, text=label, variable=var,
                           font=("Helvetica", 11), bg="#0f172a", fg="#cbd5e1",
                           activebackground="#0f172a", activeforeground="#38bdf8",
                           selectcolor="#1e293b").grid(row=row, column=col,
                                                       sticky="w", padx=15, pady=6)

        # Generate button
        tk.Button(self.root, text="⚡ Generate Password", font=("Helvetica", 13, "bold"),
                  bg="#38bdf8", fg="#0f172a", relief="flat", padx=20, pady=10,
                  cursor="hand2", command=self.generate).pack(pady=10)

        # Password display
        display_frame = tk.Frame(self.root, bg="#1e293b", pady=10, padx=10)
        display_frame.pack(fill="x", padx=30)

        self.password_var = tk.StringVar(value="Click Generate to create a password")
        password_entry = tk.Entry(display_frame, textvariable=self.password_var,
                                   font=("Courier", 13), justify="center",
                                   bg="#1e293b", fg="#4ade80", relief="flat",
                                   state="readonly", readonlybackground="#1e293b",
                                   selectbackground="#38bdf8")
        password_entry.pack(fill="x", ipady=8)

        # Strength indicator
        self.strength_var = tk.StringVar(value="")
        tk.Label(self.root, textvariable=self.strength_var, font=("Helvetica", 11, "bold"),
                 bg="#0f172a").pack(pady=2)

        # Copy button
        tk.Button(self.root, text="📋 Copy to Clipboard", font=("Helvetica", 11),
                  bg="#1e293b", fg="#94a3b8", relief="flat", padx=15, pady=6,
                  cursor="hand2", command=self.copy_password).pack()

    def generate(self):
        charset = ""
        if self.use_upper.get(): charset += string.ascii_uppercase
        if self.use_lower.get(): charset += string.ascii_lowercase
        if self.use_digits.get(): charset += string.digits
        if self.use_special.get(): charset += string.punctuation

        if not charset:
            messagebox.showwarning("No Characters", "Please select at least one character type!")
            return

        length = self.length_var.get()
        password = ''.join(random.choices(charset, k=length))
        self.password_var.set(password)
        self.update_strength(password)

    def update_strength(self, pwd):
        score = 0
        if any(c.isupper() for c in pwd): score += 1
        if any(c.islower() for c in pwd): score += 1
        if any(c.isdigit() for c in pwd): score += 1
        if any(c in string.punctuation for c in pwd): score += 1
        if len(pwd) >= 16: score += 1

        levels = {5: ("💪 Very Strong", "#4ade80"),
                  4: ("✅ Strong", "#a3e635"),
                  3: ("⚠️ Medium", "#fbbf24"),
                  2: ("❌ Weak", "#f87171"),
                  1: ("🚨 Very Weak", "#ef4444")}
        text, color = levels.get(score, ("🚨 Very Weak", "#ef4444"))
        self.strength_var.set(f"Strength: {text}")
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Label) and widget.cget("textvariable") == str(self.strength_var):
                widget.config(fg=color)

    def copy_password(self):
        pwd = self.password_var.get()
        if pwd and pwd != "Click Generate to create a password":
            self.root.clipboard_clear()
            self.root.clipboard_append(pwd)
            messagebox.showinfo("Copied!", "Password copied to clipboard!")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGenerator(root)
    root.mainloop()
