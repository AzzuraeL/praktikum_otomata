import tkinter as tk
from tkinter import messagebox

def check_palindrome():
    raw_text = entry_input.get()
    
    cleaned_text = ''.join(char.lower() for char in raw_text if char.isalnum())
    
    if not cleaned_text:
        messagebox.showwarning("Peringatan", "Input tidak valid. Masukkan minimal satu huruf atau angka.")
        return

    if cleaned_text == cleaned_text[::-1]:
        result_label.config(text=f'"{raw_text}" adalah Palindrome! ', fg="green")
    else:
        result_label.config(text=f'"{raw_text}" bukan Palindrome!', fg="red")

root = tk.Tk()
root.title("Pengenal String Palindrome")
root.geometry("450x250")
root.configure(padx=20, pady=20)

title_label = tk.Label(root, text="Program Pengenal Palindrome", font=("Arial", 16, "bold"))
title_label.pack(pady=(0, 10))

instruction_label = tk.Label(root, text="Masukkan string (hanya huruf & angka yang dihitung):", font=("Arial", 10))
instruction_label.pack()

entry_input = tk.Entry(root, width=40, font=("Arial", 12), justify="center")
entry_input.pack(pady=10)

check_button = tk.Button(
    root, 
    text="Cek String", 
    command=check_palindrome, 
    bg="#003CFF", 
    fg="white", 
    font=("Arial", 10, "bold"),
    cursor="hand2"
)
check_button.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
result_label.pack(pady=10)

root.mainloop()