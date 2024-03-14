import tkinter as tk
from modules import *

from threading import Thread


class ShinyLoops:
    def __init__(self, master):
        self.loop_thread = None
        self.master = master
        master.title("Shiny Loops")

        self.target_window = get_target_window.detect_window()
        self.running = False

        gui_elements.custom_style()
        hunt_button_frame = gui_elements.create_frame(master, "TFrame")
        hunt_button_frame.place(relx=0.5, rely=0.1, anchor=tk.N)

        self.start_eevee_button = gui_elements.create_button(hunt_button_frame, "Start Eevee",
                                                             lambda: self.start_auto_loop('eevee'))
        self.start_aero_button = gui_elements.create_button(hunt_button_frame, "Start Aerodactyl",
                                                            lambda: self.start_auto_loop('aero'))
        self.start_starter_button = gui_elements.create_button(hunt_button_frame, "Start Starter",
                                                               lambda: self.start_auto_loop('starter'))
        self.start_route1_button = gui_elements.create_button(hunt_button_frame, "Wild",
                                                              lambda: self.start_auto_loop('route1'))

        stop_button_frame = gui_elements.create_frame(master, "TFrame")
        stop_button_frame.place(relx=0.5, rely=0.35, anchor=tk.N)

        self.stop_button = gui_elements.create_button(stop_button_frame, "Stop Loop", self.stop_auto_loop)
        self.stop_button.config(state=tk.DISABLED)

        shiny_check_frame = gui_elements.create_frame(master, "TFrame")
        shiny_check_frame.place(relx=0.5, rely=0.8, anchor=tk.N)

        self.shiny_check_button = gui_elements.create_button(shiny_check_frame, "Shiny Check",
                                                             lambda: shiny_detector.shiny_check(self))
        self.shiny_test_button = gui_elements.create_button(shiny_check_frame, "Shiny Test",
                                                            lambda: self.start_auto_loop('test'))

    def start_auto_loop(self, loop):
        if not self.running:
            self.running = True
            self.start_eevee_button.config(state=tk.DISABLED)
            self.start_aero_button.config(state=tk.DISABLED)
            self.start_starter_button.config(state=tk.DISABLED)
            self.start_route1_button.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.NORMAL)
            self.shiny_check_button.config(state=tk.DISABLED)
            self.shiny_test_button.config(state=tk.DISABLED)

            if loop == 'eevee':
                self.loop_thread = Thread(target=custom_loops.eevee_loop, args=(self, self.target_window))
            elif loop == 'aero':
                self.loop_thread = Thread(target=custom_loops.aero_loop, args=(self, self.target_window))
            elif loop == 'starter':
                self.loop_thread = Thread(target=custom_loops.starter_loop, args=(self, self.target_window))
            elif loop == 'route1':
                self.loop_thread = Thread(target=custom_loops.route1_loop, args=(self, self.target_window))
            elif loop == 'test':
                self.loop_thread = Thread(target=custom_loops.shiny_test, args=(self, self.target_window))

            self.loop_thread.start()

    def stop_auto_loop(self):
        if self.running:
            self.running = False
            self.start_eevee_button.config(state=tk.NORMAL)
            self.start_aero_button.config(state=tk.NORMAL)
            self.start_starter_button.config(state=tk.NORMAL)
            self.start_route1_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.DISABLED)
            self.shiny_check_button.config(state=tk.NORMAL)
            self.shiny_test_button.config(state=tk.NORMAL)

    def on_close(self):
        self.stop_auto_loop()
        if self.loop_thread:
            self.loop_thread.join()
        self.master.destroy()


def main():
    gui.create_window(ShinyLoops)


if __name__ == "__main__":
    main()