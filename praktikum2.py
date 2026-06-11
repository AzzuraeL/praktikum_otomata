import tkinter as tk
from tkinter import messagebox

class FSM:
    def __init__(self):
        self.start_state = 'S'
        self.accept_states = {'B'}
        self.transitions = {
            'S': {'0': 'A', '1': 'B'},
            'A': {'0': 'C', '1': 'B'},
            'B': {'0': 'A', '1': 'B'},
            'C': {'0': 'C', '1': 'C'}
        }

    def evaluate(self, input_string):
        current_state = self.start_state

        for char in input_string:
            if char not in ['0', '1']:
                return False, f"Error: Invalid character '{char}'. Only '0' and '1' are allowed."
            current_state = self.transitions[current_state][char]
        is_accepted = current_state in self.accept_states
        
        if is_accepted:
            return True, f"Accepted (Ended in state {current_state})"
        else:
            if current_state == 'C':
                return False, "Rejected (Contains substring '00')"
            else:
                return False, f"Rejected (Did not end in '1', ended in state {current_state})"

class FSMApp:
    def __init__(self, root):
        self.root = root
        self.root.title("FSM Automata Validator")
        self.root.geometry("400x350")
        self.root.configure(padx=20, pady=20)
        
        self.fsm = FSM()
        self.create_widgets()

    def create_widgets(self):
        title_label = tk.Label(self.root, text="FSM String Validator", font=("Arial", 16, "bold"))
        title_label.pack(pady=(0, 10))

        rules_text = (
            "L = { x ∈ (0 + 1)+ | dengan karakter terakhir\n"
            "pada string x adalah 1 dan x tidak memiliki substring 00 }\n"
        )
        rules_label = tk.Label(self.root, text=rules_text, justify="left", fg="#555555", font=("Arial", 10))
        rules_label.pack(anchor="w", pady=(0, 15))

        input_frame = tk.Frame(self.root)
        input_frame.pack(fill="x", pady=5)

        tk.Label(input_frame, text="Enter string:", font=("Arial", 10)).pack(side="left")
        self.entry_var = tk.StringVar()
        self.entry = tk.Entry(input_frame, textvariable=self.entry_var, font=("Arial", 12))
        self.entry.pack(side="left", fill="x", expand=True, padx=5)
        
        self.root.bind('<Return>', lambda event: self.evaluate_string())

        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=15)

        eval_btn = tk.Button(btn_frame, text="Evaluate", command=self.evaluate_string, bg="#003CFF", fg="white", width=10, font=("Arial", 10, "bold"))
        eval_btn.pack(side="left", padx=5)

        clear_btn = tk.Button(btn_frame, text="Clear", command=self.clear_input, width=10, font=("Arial", 10))
        clear_btn.pack(side="left", padx=5)

        self.result_label = tk.Label(self.root, text="", font=("Arial", 14, "bold"))
        self.result_label.pack(pady=(10, 0))
        
        self.detail_label = tk.Label(self.root, text="", font=("Arial", 10))
        self.detail_label.pack()

    def evaluate_string(self):
        user_input = self.entry_var.get().strip()
        
        if not user_input:
            messagebox.showwarning("Empty Input", "Input cannot be empty. Please enter a string.")
            return

        is_valid, message = self.fsm.evaluate(user_input)
        
        if is_valid:
            self.result_label.config(text="[ VALID ]", fg="green")
        else:
            self.result_label.config(text="[ INVALID ]", fg="red")
            
        self.detail_label.config(text=message)

    def clear_input(self):
        self.entry_var.set("")
        self.result_label.config(text="")
        self.detail_label.config(text="")
        self.entry.focus()

if __name__ == "__main__":
    root = tk.Tk()
    app = FSMApp(root)
    root.mainloop()