import tkinter as tk
from tkinter import messagebox

class PDA:
    def __init__(self):
        self.stack = []
    
    def process_string(self, input_string):
        self.stack = []
        state = 'q0'

        for char in input_string:
            if state == 'q0':
                if char == 'a':
                    self.stack.append('A')
                elif char == 'b':
                    if not self.stack:
                        return False
                    self.stack.pop()
                    state = 'q1'
                else:
                    return False
                    
            elif state == 'q1':
                if char == 'b':
                    if not self.stack:
                        return False
                    self.stack.pop()
                else:
                    return False
        
        return len(self.stack) == 0

class PDAApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simulator Mesin PDA")
        self.root.geometry("400x250")
        self.root.configure(padx=20, pady=20)
        
        self.pda_machine = PDA()
        
        self.create_widgets()

    def create_widgets(self):
        title_label = tk.Label(self.root, text="PDA: L = {aⁿ bⁿ | n ≥ 0}", font=("Helvetica", 16, "bold"))
        title_label.pack(pady=(0, 10))
        
        instruction_label = tk.Label(self.root, text="Masukkan string (hanya karakter 'a' dan 'b'):")
        instruction_label.pack()
        
        self.entry_string = tk.Entry(self.root, font=("Helvetica", 14), width=20, justify="center")
        self.entry_string.pack(pady=10)
        
        check_button = tk.Button(self.root, text="Cek String", font=("Helvetica", 12), bg="#003CFF", fg="white", command=self.check_pda)
        check_button.pack(pady=10)
        
        self.result_label = tk.Label(self.root, text="", font=("Helvetica", 14, "bold"))
        self.result_label.pack(pady=10)

    def check_pda(self):
        input_str = self.entry_string.get()
        
        is_accepted = self.pda_machine.process_string(input_str)
        
        if is_accepted:
            self.result_label.config(text="Status: ACCEPTED", fg="green")
        else:
            self.result_label.config(text="Status: REJECTED", fg="red")

if __name__ == "__main__":
    root = tk.Tk()
    app = PDAApp(root)
    root.mainloop()