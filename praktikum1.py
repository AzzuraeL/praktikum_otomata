import tkinter as tk
from tkinter import messagebox
import re

class LexicalAnalyzerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lexical Analyzer - C Language Tokenizer")
        self.root.geometry("750x650")
        self.root.configure(padx=15, pady=15)

        tk.Label(root, text="TUGAS PRAKTIKUM #1: Masukkan Program C:",
                 font=("Arial", 12, "bold")).pack(anchor="w")

        self.text_input = tk.Text(root, height=12, font=("Consolas", 11), bg="#ffffff")
        self.text_input.pack(fill="both", expand=True, pady=(5, 10))

        frame_btn = tk.Frame(root)
        frame_btn.pack(fill="x", pady=5)

        self.btn_analyze = tk.Button(frame_btn, text="Analisis Token",
                                     font=("Arial", 10, "bold"), bg="#003CFF", fg="white",
                                     command=self.analyze_code, cursor="hand2")
        self.btn_analyze.pack(side="left", padx=(0, 10))

        self.btn_clear = tk.Button(frame_btn, text="Bersihkan",
                                   font=("Arial", 10), command=self.clear_all, cursor="hand2")
        self.btn_clear.pack(side="left")

        tk.Label(root, text="Hasil Pengelompokan Token:",
                 font=("Arial", 12, "bold")).pack(anchor="w", pady=(10, 5))

        self.text_output = tk.Text(root, height=15, font=("Consolas", 11),
                                   state="disabled", bg="#f4f4f4")
        self.text_output.pack(fill="both", expand=True)

    def clear_all(self):
        self.text_input.delete(1.0, tk.END)
        self.text_output.config(state="normal")
        self.text_output.delete(1.0, tk.END)
        self.text_output.config(state="disabled")

    def analyze_code(self):
        code = self.text_input.get(1.0, tk.END).strip()
        if not code:
            messagebox.showwarning("Input Kosong", "Silakan masukkan kode program C terlebih dahulu!")
            return

        tokens = self.tokenize_c(code)
        self.display_results(tokens)

    def tokenize_c(self, code):
        keywords = {
            'auto', 'break', 'case', 'char', 'const', 'continue', 'default', 'do',
            'double', 'else', 'enum', 'extern', 'float', 'for', 'goto', 'if',
            'int', 'long', 'register', 'return', 'short', 'signed', 'sizeof', 'static',
            'struct', 'switch', 'typedef', 'union', 'unsigned', 'void', 'volatile', 'while' , 'printf'
        }

        token_specification = [
            ('COMMENT',  r'//[^\n]*|/\*.*?\*/'),
            ('FUNGSI',   r'\b[a-zA-Z_]\w*(?=\s*\()'),
            ('NUMBER',   r'\b\d+(\.\d*)?\b'),
            ('WORD',     r'\b[a-zA-Z_]\w*\b'),
            ('OPERATOR', r'==|!=|<=|>=|&&|\|\||\+\+|\-\-|[+\-*/=<>!&|]'),
            ('SYMBOL',   r'[{}()\[\],;#]'),
            ('STRING',   r'".*?"|\'.*?\''),
            ('SKIP',     r'[ \t\n]+'),
            ('MISMATCH', r'.'),
        ]

        tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)

        results = {
            "a. Reserve words": set(),
            "b. Simbol dan tanda baca": set(),
            "c. Variabel": set(),
            "d. Kalimat matematika (persamaan, fungsi, dsb)": set()
        }

        for mo in re.finditer(tok_regex, code, re.DOTALL):
            kind = mo.lastgroup
            value = mo.group()

            if kind in ['SKIP', 'STRING', 'MISMATCH', 'COMMENT']:
                continue

            if kind == 'FUNGSI':
                if value in keywords:
                    results["a. Reserve words"].add(value)
                else:
                    results["d. Kalimat matematika (persamaan, fungsi, dsb)"].add(value + "()")
            elif kind == 'WORD':
                if value in keywords:
                    results["a. Reserve words"].add(value)
                else:
                    results["c. Variabel"].add(value)
            elif kind == 'SYMBOL':
                results["b. Simbol dan tanda baca"].add(value)
            elif kind == 'NUMBER' or kind == 'OPERATOR':
                results["d. Kalimat matematika (persamaan, fungsi, dsb)"].add(value)

        return {k: sorted(list(v)) for k, v in results.items()}

    def display_results(self, tokens):
        self.text_output.config(state="normal")
        self.text_output.delete(1.0, tk.END)

        for category, items in tokens.items():
            self.text_output.insert(tk.END, f"{category}\n", "bold")
            if items:
                self.text_output.insert(tk.END, " -> " + ", ".join(items) + "\n\n")
            else:
                self.text_output.insert(tk.END, " -> (Tidak ada)\n\n")

        self.text_output.config(state="disabled")

if __name__ == "__main__":
    root = tk.Tk()
    app = LexicalAnalyzerApp(root)
    root.mainloop()