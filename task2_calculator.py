import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("CodSoft - Calculator")
        self.root.geometry("360x560")
        self.root.configure(bg="#1e1e2e")
        self.root.resizable(False, False)

        self.expression = ""
        self.build_ui()

    def build_ui(self):
        # Header
        tk.Label(self.root, text="CodSoft Calculator", font=("Helvetica", 13, "bold"),
                 bg="#1e1e2e", fg="#cdd6f4").pack(pady=(10, 0))

        # Display
        display_frame = tk.Frame(self.root, bg="#1e1e2e", pady=10)
        display_frame.pack(fill="x", padx=15)

        self.display_var = tk.StringVar(value="0")
        self.display = tk.Entry(display_frame, textvariable=self.display_var,
                                font=("Helvetica", 28, "bold"), justify="right",
                                bg="#313244", fg="#cdd6f4", relief="flat",
                                bd=0, insertwidth=0, state="readonly",
                                readonlybackground="#313244")
        self.display.pack(fill="x", ipady=18, ipadx=10)

        # Buttons
        buttons = [
            ["C", "±", "%", "÷"],
            ["7", "8", "9", "×"],
            ["4", "5", "6", "−"],
            ["1", "2", "3", "+"],
            ["0", ".", "⌫", "="],
        ]

        btn_frame = tk.Frame(self.root, bg="#1e1e2e")
        btn_frame.pack(fill="both", expand=True, padx=15, pady=10)

        for row_idx, row in enumerate(buttons):
            for col_idx, btn_text in enumerate(row):
                self.make_button(btn_frame, btn_text, row_idx, col_idx)

    def make_button(self, parent, text, row, col):
        if text in ("÷", "×", "−", "+", "="):
            bg, fg = "#f38ba8", "white"
        elif text in ("C", "±", "%"):
            bg, fg = "#585b70", "#cdd6f4"
        elif text == "0":
            bg, fg = "#45475a", "#cdd6f4"
        else:
            bg, fg = "#45475a", "#cdd6f4"

        btn = tk.Button(parent, text=text, font=("Helvetica", 16, "bold"),
                        bg=bg, fg=fg, relief="flat", cursor="hand2",
                        activebackground="#89b4fa", activeforeground="white",
                        command=lambda t=text: self.on_click(t))

        col_span = 2 if text == "0" else 1
        btn.grid(row=row, column=col, columnspan=col_span,
                 sticky="nsew", padx=4, pady=4, ipady=14)

        for i in range(4):
            parent.columnconfigure(i, weight=1)
        for i in range(5):
            parent.rowconfigure(i, weight=1)

    def on_click(self, text):
        if text == "C":
            self.expression = ""
            self.display_var.set("0")
        elif text == "⌫":
            self.expression = self.expression[:-1]
            self.display_var.set(self.expression if self.expression else "0")
        elif text == "=":
            try:
                expr = self.expression.replace("÷", "/").replace("×", "*").replace("−", "-")
                result = eval(expr)
                result = int(result) if isinstance(result, float) and result.is_integer() else round(result, 8)
                self.display_var.set(result)
                self.expression = str(result)
            except:
                self.display_var.set("Error")
                self.expression = ""
        elif text == "±":
            if self.expression and self.expression != "0":
                if self.expression.startswith("-"):
                    self.expression = self.expression[1:]
                else:
                    self.expression = "-" + self.expression
                self.display_var.set(self.expression)
        elif text == "%":
            try:
                result = float(eval(self.expression)) / 100
                result = int(result) if isinstance(result, float) and result.is_integer() else round(result, 8)
                self.expression = str(result)
                self.display_var.set(self.expression)
            except:
                self.display_var.set("Error")
                self.expression = ""
        else:
            if self.expression == "0" and text.isdigit():
                self.expression = text
            else:
                self.expression += text
            self.display_var.set(self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()
