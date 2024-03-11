import time
import pyautogui
import tkinter as tk

from tkinter import ttk
from PIL import ImageGrab
from threading import Thread


class AutoLoopApp:
    def __init__(self, master):
        self.loop_thread = None
        self.master = master
        master.title("Shiny Loops")

        self.running = False

        style = ttk.Style()
        style.configure("TButton", padding=10, background="#333333", borderwidth=0, highlightthickness=0)
        hunt_button_frame = ttk.Frame(master, style="TFrame")
        hunt_button_frame.place(relx=0.5, rely=0.1, anchor=tk.N)

        self.start_abra = ttk.Button(hunt_button_frame, text="Start Abra", command=lambda: self.start_auto_loop(self.auto_abra_loop))
        self.start_abra.pack(side=tk.LEFT)
        self.start_abra.bind("<Enter>", lambda event: on_enter(self.start_abra))
        self.start_abra.bind("<Leave>", lambda event: on_leave(self.start_abra))

        self.start_eevee = ttk.Button(hunt_button_frame, text="Start Eevee", command=lambda: self.start_auto_loop(self.auto_eevee_loop))
        self.start_eevee.pack(side=tk.LEFT)
        self.start_eevee.bind("<Enter>", lambda event: on_enter(self.start_eevee))
        self.start_eevee.bind("<Leave>", lambda event: on_leave(self.start_eevee))

        self.start_aero = ttk.Button(hunt_button_frame, text="Start Aerodactyl", command=lambda: self.start_auto_loop(self.auto_aero_loop))
        self.start_aero.pack(side=tk.LEFT)
        self.start_aero.bind("<Enter>", lambda event: on_enter(self.start_aero))
        self.start_aero.bind("<Leave>", lambda event: on_leave(self.start_aero))

        stop_button_frame = ttk.Frame(master, style="TFrame")
        stop_button_frame.place(relx=0.5, rely=0.35, anchor=tk.N)

        self.stop_button = ttk.Button(stop_button_frame, text="Stop Loop", command=self.stop_auto_loop, state=tk.DISABLED)
        self.stop_button.pack()
        self.stop_button.bind("<Enter>", lambda event: on_enter(self.stop_button))
        self.stop_button.bind("<Leave>", lambda event: on_leave(self.stop_button))

        shiny_check_frame = ttk.Frame(master, style="TFrame")
        shiny_check_frame.place(relx=0.5, rely=0.8, anchor=tk.N)

        self.shiny_check_button = ttk.Button(shiny_check_frame, text="Shiny Check", command=lambda: self.start_auto_loop(self.shiny_check))
        self.shiny_check_button.pack()
        self.shiny_check_button.bind("<Enter>", lambda event: on_enter(self.shiny_check_button))
        self.shiny_check_button.bind("<Leave>", lambda event: on_leave(self.shiny_check_button))

    def auto_abra_loop(self):
        try:
            while self.running:
                pyautogui.keyDown('x')
                time.sleep(0.01)
                pyautogui.keyUp('x')

        except KeyboardInterrupt:
            print("Loop interrupted.")

    def auto_eevee_loop(self):
        loop_keys = ['z', 'x', 'z', 'enter', 'down', 'x', 'down', 'x', 'x']
        restart_keys = ['x', 'z', 'return', 'backspace']

        try:
            while self.running:
                for i in range(5):
                    pyautogui.keyDown('x')
                    time.sleep(0.01)
                    pyautogui.keyUp('x')
                    time.sleep(1)

                for key in loop_keys:
                    if not self.running:
                        break
                    pyautogui.keyDown(key)
                    time.sleep(0.01)
                    pyautogui.keyUp(key)
                    time.sleep(1)

                screenshot = ImageGrab.grab()
                target_color = (107, 227, 231)
                square_position = (0, 0)
                square_size = (100, 500)

                left, top = square_position
                right, bottom = left + square_size[0], top + square_size[1]
                square = screenshot.crop((left, top, right, bottom))

                shiny_pixels = any(pixel == target_color for pixel in square.getdata())

                if shiny_pixels:
                    print("WOOHOOO! You got a shiny!")
                    break
                else:
                    for key in restart_keys:
                        pyautogui.keyDown(key)
                    time.sleep(0.01)
                    for key in restart_keys:
                        pyautogui.keyUp(key)

        except KeyboardInterrupt:
            print("Loop interrupted.")

    def auto_aero_loop(self):
        loop_keys = ['z', 'x', 'x', 'x', 'z', 'enter', 'down', 'x', 'down', 'x', 'x']
        restart_keys = ['x', 'z', 'return', 'backspace']

        try:
            while self.running:
                for i in range(5):
                    pyautogui.keyDown('x')
                    time.sleep(0.01)
                    pyautogui.keyUp('x')
                    time.sleep(1)

                for key in loop_keys:
                    if not self.running:
                        break
                    pyautogui.keyDown(key)
                    time.sleep(0.01)
                    pyautogui.keyUp(key)
                    time.sleep(1)

                screenshot = ImageGrab.grab()
                target_color = (107, 227, 231)
                square_position = (0, 0)
                square_size = (100, 500)

                left, top = square_position
                right, bottom = left + square_size[0], top + square_size[1]
                square = screenshot.crop((left, top, right, bottom))

                shiny_pixels = any(pixel == target_color for pixel in square.getdata())

                if shiny_pixels:
                    print("WOOHOOO! You got a shiny!")
                    break
                else:
                    for key in restart_keys:
                        pyautogui.keyDown(key)
                    time.sleep(0.01)
                    for key in restart_keys:
                        pyautogui.keyUp(key)

        except KeyboardInterrupt:
            print("Loop interrupted.")

    def shiny_check(self):
        loop_keys = ['z', 'enter', 'down', 'x', 'x', 'x']

        try:
            while self.running:
                for i in range(5):
                    pyautogui.keyDown('x')
                    time.sleep(0.01)
                    pyautogui.keyUp('x')
                    time.sleep(1)

                for key in loop_keys:
                    if not self.running:
                        break
                    pyautogui.keyDown(key)
                    time.sleep(0.01)
                    pyautogui.keyUp(key)
                    time.sleep(1)

                screenshot = ImageGrab.grab()
                target_color = (107, 227, 231)
                square_position = (0, 0)
                square_size = (100, 500)

                left, top = square_position
                right, bottom = left + square_size[0], top + square_size[1]
                square = screenshot.crop((left, top, right, bottom))

                shiny_pixels = any(pixel == target_color for pixel in square.getdata())

                if shiny_pixels:
                    print("WOOHOOO! You got a shiny!")
                    break
                else:
                    print("No shiny")
                    break

        except KeyboardInterrupt:
            print("Loop interrupted.")

    def start_auto_loop(self, loop):
        # Gives a little time to focus on the emulator
        time.sleep(5)

        if not self.running:
            self.running = True
            self.start_abra.config(state=tk.DISABLED)
            self.start_eevee.config(state=tk.DISABLED)
            self.start_aero.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.NORMAL)
            self.shiny_check_button.config(state=tk.DISABLED)

            self.loop_thread = Thread(target=loop)
            self.loop_thread.start()

    def stop_auto_loop(self):
        if self.running:
            self.running = False
            self.start_abra.config(state=tk.NORMAL)
            self.start_eevee.config(state=tk.NORMAL)
            self.start_aero.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.DISABLED)
            self.shiny_check_button.config(state=tk.NORMAL)

    def on_close(self):
        self.stop_auto_loop()
        if self.loop_thread:
            self.loop_thread.join()
        self.master.destroy()


def on_enter(widget):
    widget.configure(cursor="hand2")


def on_leave(widget):
    widget.configure(cursor="")


root = tk.Tk()
app = AutoLoopApp(root)
icon_path = "imgs/icon.ico"

root.protocol("WM_DELETE_WINDOW", app.on_close)
root.iconbitmap(default=icon_path)
root.configure(bg="#333333")
root.geometry("500x300")
root.minsize(250, 200)

root.mainloop()
