import tkinter as tk
from tkinter import ttk


def create_button(frame, text, command):
    button = ttk.Button(frame, text=text, command=command, cursor="hand2")
    button.pack(side=tk.LEFT)
    return button


def create_frame(master, style):
    frame = ttk.Frame(master, style=style)
    return frame


def create_label(parent, image_path):
    frame = ttk.Frame(parent, width=500, height=30)
    frame.pack_propagate(False)

    image = tk.PhotoImage(file=image_path)
    frame.image = image

    image_label = tk.Label(frame, image=image)
    image_label.place(x=0, y=0, relwidth=1, relheight=1)

    return frame


def custom_style():
    style = ttk.Style()
    style.configure("TButton", padding=10, background="#333333", borderwidth=0, highlightthickness=0)

    style.map("TButton", foreground=[('active', '#FFFFFF'), ('pressed', '#FFFFFF')],
              background=[('active', '#555555'), ('pressed', '#888888')])
    style.map("TButton", foreground=[('disabled', '#AAAAAA')], background=[('disabled', '#333333')])
