import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissors:
    def __init__(self, root):
        self.root = root
        self.root.title("CodSoft - Rock Paper Scissors")
        self.root.geometry("480x580")
        self.root.configure(bg="#1a1a2e")
        self.root.resizable(False, False)

        self.user_score = 0
        self.computer_score = 0
        self.rounds = 0
        self.choices = ["Rock", "Paper", "Scissors"]
        self.emojis = {"Rock": "🪨", "Paper": "📄", "Scissors": "✂️"}
        self.build_ui()

    def build_ui(self):
        tk.Label(self.root, text="Rock · Paper · Scissors",
                 font=("Helvetica", 18, "bold"), bg="#1a1a2e", fg="#e94560").pack(pady=15)

        # Score board
        score_frame = tk.Frame(self.root, bg="#16213e", pady=10)
        score_frame.pack(fill="x", padx=20)

        for col, (label, color) in enumerate([("You", "#4ade80"), ("Rounds", "#fbbf24"), ("Computer", "#f87171")]):
            tk.Label(score_frame, text=label, font=("Helvetica", 10),
                     bg="#16213e", fg="#94a3b8").grid(row=0, column=col, padx=30)

        self.user_score_var = tk.StringVar(value="0")
        self.rounds_var = tk.StringVar(value="0")
        self.comp_score_var = tk.StringVar(value="0")

        tk.Label(score_frame, textvariable=self.user_score_var,
                 font=("Helvetica", 28, "bold"), bg="#16213e", fg="#4ade80").grid(row=1, column=0, padx=30)
        tk.Label(score_frame, textvariable=self.rounds_var,
                 font=("Helvetica", 28, "bold"), bg="#16213e", fg="#fbbf24").grid(row=1, column=1, padx=30)
        tk.Label(score_frame, textvariable=self.comp_score_var,
                 font=("Helvetica", 28, "bold"), bg="#16213e", fg="#f87171").grid(row=1, column=2, padx=30)

        score_frame.columnconfigure(0, weight=1)
        score_frame.columnconfigure(1, weight=1)
        score_frame.columnconfigure(2, weight=1)

        # Battle display
        battle_frame = tk.Frame(self.root, bg="#1a1a2e", pady=10)
        battle_frame.pack()

        self.user_emoji_var = tk.StringVar(value="❓")
        self.comp_emoji_var = tk.StringVar(value="❓")

        tk.Label(battle_frame, textvariable=self.user_emoji_var,
                 font=("Helvetica", 60), bg="#1a1a2e").grid(row=0, column=0, padx=30)
        tk.Label(battle_frame, text="VS", font=("Helvetica", 20, "bold"),
                 bg="#1a1a2e", fg="#e94560").grid(row=0, column=1)
        tk.Label(battle_frame, textvariable=self.comp_emoji_var,
                 font=("Helvetica", 60), bg="#1a1a2e").grid(row=0, column=2, padx=30)

        tk.Label(battle_frame, text="You", font=("Helvetica", 10),
                 bg="#1a1a2e", fg="#94a3b8").grid(row=1, column=0)
        tk.Label(battle_frame, text="Computer", font=("Helvetica", 10),
                 bg="#1a1a2e", fg="#94a3b8").grid(row=1, column=2)

        # Result label
        self.result_var = tk.StringVar(value="Choose your move!")
        self.result_label = tk.Label(self.root, textvariable=self.result_var,
                                      font=("Helvetica", 16, "bold"),
                                      bg="#1a1a2e", fg="white")
        self.result_label.pack(pady=10)

        # Choice buttons
        tk.Label(self.root, text="Your Move:", font=("Helvetica", 12),
                 bg="#1a1a2e", fg="#94a3b8").pack()

        btn_frame = tk.Frame(self.root, bg="#1a1a2e")
        btn_frame.pack(pady=10)

        colors = {"Rock": "#6366f1", "Paper": "#06b6d4", "Scissors": "#f59e0b"}
        for choice in self.choices:
            tk.Button(btn_frame, text=f"{self.emojis[choice]}\n{choice}",
                      font=("Helvetica", 13, "bold"), bg=colors[choice], fg="white",
                      relief="flat", width=7, pady=10, cursor="hand2",
                      command=lambda c=choice: self.play(c)).pack(side="left", padx=10)

        # Reset button
        tk.Button(self.root, text="🔄 Reset Game", font=("Helvetica", 11),
                  bg="#e94560", fg="white", relief="flat", padx=15, pady=6,
                  cursor="hand2", command=self.reset).pack(pady=10)

    def play(self, user_choice):
        comp_choice = random.choice(self.choices)
        self.rounds += 1
        self.rounds_var.set(str(self.rounds))
        self.user_emoji_var.set(self.emojis[user_choice])
        self.comp_emoji_var.set(self.emojis[comp_choice])

        if user_choice == comp_choice:
            result = "🤝 It's a Tie!"
            color = "#fbbf24"
        elif (user_choice == "Rock" and comp_choice == "Scissors") or \
             (user_choice == "Scissors" and comp_choice == "Paper") or \
             (user_choice == "Paper" and comp_choice == "Rock"):
            result = "🎉 You Win!"
            color = "#4ade80"
            self.user_score += 1
            self.user_score_var.set(str(self.user_score))
        else:
            result = "💻 Computer Wins!"
            color = "#f87171"
            self.computer_score += 1
            self.comp_score_var.set(str(self.computer_score))

        self.result_var.set(result)
        self.result_label.config(fg=color)

    def reset(self):
        self.user_score = 0
        self.computer_score = 0
        self.rounds = 0
        self.user_score_var.set("0")
        self.comp_score_var.set("0")
        self.rounds_var.set("0")
        self.user_emoji_var.set("❓")
        self.comp_emoji_var.set("❓")
        self.result_var.set("Choose your move!")
        self.result_label.config(fg="white")

if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissors(root)
    root.mainloop()
