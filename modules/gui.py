import tkinter as tk

ICON_PATH = "imgs/icon.ico"


def create_window(application):
    root = tk.Tk()
    app = application(root)

    root.protocol("WM_DELETE_WINDOW", app.on_close)
    root.iconbitmap(default=ICON_PATH)
    root.configure(bg="#333333")
    root.geometry("500x300")
    root.minsize(500, 200)

    root.mainloop()