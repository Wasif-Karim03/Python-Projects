import tkinter as tk
from tkinter import colorchooser

class DigitalWhiteBoard:
    def __init__(self, root):
        self.root = root
        self.root.title("Digital White Board")

        self.canvas = tk.Canvas(root, bg='white', width=800, height=600)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.pen_color = 'black'
        self.eraser_on = False

        self.canvas.bind('<B1-Motion>', self.paint)
        self.canvas.bind('<Button-1>', self.paint)

        color_button = tk.Button(root, text='Choose Color', command=self.choose_color)
        color_button.pack(side=tk.LEFT)

        eraser_button = tk.Button(root, text='Eraser', command=self.use_eraser)
        eraser_button.pack(side=tk.LEFT)

        pen_button = tk.Button(root, text='Pen', command=self.use_pen)
        pen_button.pack(side=tk.LEFT)

    def choose_color(self):
        self.pen_color = colorchooser.askcolor(color=self.pen_color)[1]
        self.eraser_on = False

    def use_eraser(self):
        self.eraser_on = True

    def use_pen(self):
        self.eraser_on = False

    def paint(self, event):
        paint_color = 'white' if self.eraser_on else self.pen_color
        x1, y1 = (event.x - 1), (event.y - 1)
        x2, y2 = (event.x + 1), (event.y + 1)
        self.canvas.create_oval(x1, y1, x2, y2, fill=paint_color, outline=paint_color)

if __name__ == "__main__":
    root = tk.Tk()
    board = DigitalWhiteBoard(root)
    root.mainloop()