import tkinter as tk
import random

root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("400x400")
root.configure(bg="#1a1a2e")
root.resizable(False, False)

tk.Label(root, text="🪨 Paper ✂️ Scissors", font=("Helvetica", 16, "bold"),
         bg="#1a1a2e", fg="#e94560").pack(pady=15)

scores = {"You": 0, "Computer": 0}
score_var = tk.StringVar(value="You: 0  |  Computer: 0")
tk.Label(root, textvariable=score_var, font=("Helvetica", 13),
         bg="#1a1a2e", fg="#fbbf24").pack()

user_var = tk.StringVar(value="❓")
comp_var = tk.StringVar(value="❓")
result_var = tk.StringVar(value="Choose your move!")

vs_frame = tk.Frame(root, bg="#1a1a2e")
vs_frame.pack(pady=15)
tk.Label(vs_frame, textvariable=user_var, font=("Helvetica", 50),
         bg="#1a1a2e").pack(side="left", padx=20)
tk.Label(vs_frame, text="VS", font=("Helvetica", 18, "bold"),
         bg="#1a1a2e", fg="#e94560").pack(side="left")
tk.Label(vs_frame, textvariable=comp_var, font=("Helvetica", 50),
         bg="#1a1a2e").pack(side="left", padx=20)

tk.Label(root, textvariable=result_var, font=("Helvetica", 14, "bold"),
         bg="#1a1a2e", fg="white").pack(pady=5)

emojis = {"Rock": "🪨", "Paper": "📄", "Scissors": "✂️"}

def play(choice):
    comp = random.choice(["Rock", "Paper", "Scissors"])
    user_var.set(emojis[choice])
    comp_var.set(emojis[comp])
    if choice == comp:
        result_var.set("🤝 It's a Tie!")
    elif (choice=="Rock" and comp=="Scissors") or \
         (choice=="Scissors" and comp=="Paper") or \
         (choice=="Paper" and comp=="Rock"):
        result_var.set("🎉 You Win!")
        scores["You"] += 1
    else:
        result_var.set("💻 Computer Wins!")
        scores["Computer"] += 1
    score_var.set(f"You: {scores['You']}  |  Computer: {scores['Computer']}")

btn_frame = tk.Frame(root, bg="#1a1a2e")
btn_frame.pack(pady=10)
for choice, color in [("Rock","#6366f1"), ("Paper","#06b6d4"), ("Scissors","#f59e0b")]:
    tk.Button(btn_frame, text=f"{emojis[choice]}\n{choice}", font=("Helvetica", 12, "bold"),
              bg=color, fg="white", relief="flat", width=8, height=3,
              cursor="hand2", command=lambda c=choice: play(c)).pack(side="left", padx=8)

root.mainloop()
