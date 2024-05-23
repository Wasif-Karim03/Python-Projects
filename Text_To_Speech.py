import tkinter as tk
from tkinter import filedialog
from gtts import gTTS
import os
import platform

# Function to convert text to speech
def text_to_speech():
    text = text_entry.get("1.0", tk.END)
    if text.strip():
        tts = gTTS(text=text, lang='en')
        tts.save("output.mp3")
        if platform.system() == 'Darwin':  # macOS
            os.system("afplay output.mp3")
        else:
            playsound("output.mp3")
    else:
        result_label.config(text="Please enter some text.")

# Function to load text from a file
def load_text():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, 'r') as file:
            text_entry.delete("1.0", tk.END)
            text_entry.insert(tk.END, file.read())

# Create the main window
root = tk.Tk()
root.title("Text to Speech Converter")
root.geometry("400x300")

# Create a text entry widget
text_entry = tk.Text(root, wrap=tk.WORD, height=10, width=40)
text_entry.pack(pady=10)

# Create a convert button
convert_button = tk.Button(root, text="Convert to Speech", command=text_to_speech)
convert_button.pack(pady=5)

# Create a load text button
load_button = tk.Button(root, text="Load Text from File", command=load_text)
load_button.pack(pady=5)

# Create a label to display results
result_label = tk.Label(root, text="", fg="red")
result_label.pack(pady=5)

# Run the application
root.mainloop()

# Cleanup: Remove the audio file after use
if os.path.exists("output.mp3"):
    os.remove("output.mp3")