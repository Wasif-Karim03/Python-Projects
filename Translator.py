import tkinter as tk
from tkinter import ttk, messagebox
from googletrans import Translator, LANGUAGES

# Function to translate text
def translate_text():
    input_text = input_textbox.get("1.0", tk.END).strip()
    target_language = lang_combobox.get()

    if not input_text:
        messagebox.showerror("Input Error", "Please enter text to translate.")
        return

    if not target_language:
        messagebox.showerror("Language Error", "Please select a target language.")
        return

    translator = Translator()
    try:
        translated = translator.translate(input_text, dest=target_language)
        output_textbox.delete("1.0", tk.END)
        output_textbox.insert(tk.END, translated.text)
    except Exception as e:
        messagebox.showerror("Translation Error", str(e))

# Create the main window
root = tk.Tk()
root.title("Text Translator")

# Create input text frame
input_frame = ttk.LabelFrame(root, text="Enter Text in English")
input_frame.pack(padx=10, pady=10, fill="both", expand=True)

input_textbox = tk.Text(input_frame, height=10)
input_textbox.pack(padx=10, pady=10, fill="both", expand=True)

# Create language selection frame
lang_frame = ttk.LabelFrame(root, text="Select Target Language")
lang_frame.pack(padx=10, pady=10, fill="both", expand=True)

lang_combobox = ttk.Combobox(lang_frame, values=list(LANGUAGES.values()), state="readonly")
lang_combobox.pack(padx=10, pady=10, fill="both", expand=True)

# Create translate button
translate_button = ttk.Button(root, text="Translate", command=translate_text)
translate_button.pack(pady=10)

# Create output text frame
output_frame = ttk.LabelFrame(root, text="Translated Text")
output_frame.pack(padx=10, pady=10, fill="both", expand=True)

output_textbox = tk.Text(output_frame, height=10)
output_textbox.pack(padx=10, pady=10, fill="both", expand=True)

# Run the application
root.mainloop()