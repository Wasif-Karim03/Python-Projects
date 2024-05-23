import tkinter as tk
from tkinter import messagebox

def encrypt_message(message, shift):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            shift_amount = 65 if char.isupper() else 97
            encrypted_message += chr((ord(char) - shift_amount + shift) % 26 + shift_amount)
        else:
            encrypted_message += char
    return encrypted_message

def decrypt_message(encrypted_message, shift):
    return encrypt_message(encrypted_message, -shift)

def encrypt():
    message = entry_message.get()
    shift = int(entry_shift.get())
    encrypted_message = encrypt_message(message, shift)
    entry_result.delete(0, tk.END)
    entry_result.insert(0, encrypted_message)

def decrypt():
    encrypted_message = entry_message.get()
    shift = int(entry_shift.get())
    decrypted_message = decrypt_message(encrypted_message, shift)
    entry_result.delete(0, tk.END)
    entry_result.insert(0, decrypted_message)

# Create the main window
root = tk.Tk()
root.title("Secret Message Encryption and Decryption Tool")

# Create and place labels and entry widgets
label_message = tk.Label(root, text="Message:")
label_message.grid(row=0, column=0, padx=10, pady=10)

entry_message = tk.Entry(root, width=50)
entry_message.grid(row=0, column=1, padx=10, pady=10)

label_shift = tk.Label(root, text="Shift:")
label_shift.grid(row=1, column=0, padx=10, pady=10)

entry_shift = tk.Entry(root, width=5)
entry_shift.grid(row=1, column=1, padx=10, pady=10, sticky='w')

label_result = tk.Label(root, text="Result:")
label_result.grid(row=2, column=0, padx=10, pady=10)

entry_result = tk.Entry(root, width=50)
entry_result.grid(row=2, column=1, padx=10, pady=10)

# Create and place buttons
button_encrypt = tk.Button(root, text="Encrypt", command=encrypt)
button_encrypt.grid(row=3, column=0, padx=10, pady=10)

button_decrypt = tk.Button(root, text="Decrypt", command=decrypt)
button_decrypt.grid(row=3, column=1, padx=10, pady=10)

# Start the GUI event loop
root.mainloop()