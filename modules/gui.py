import tkinter as tk
from config import config


def create_window(application):
    root = tk.Tk()
    app = application(root)

    root.protocol("WM_DELETE_WINDOW", app.on_close)
    root.iconbitmap(default=config.ICON_PATH)
    root.configure(bg="#333333")
    root.geometry(config.APP_SIZE)
    root.resizable(False, False)

    root.mainloop()