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

        # Labels
        routes_label = gui_elements.create_label(master, "imgs/routes_label.png")
        routes_label.place(relx=0.5, rely=0, anchor=tk.N)

        locations_label = gui_elements.create_label(master, "imgs/locations_label.png")
        locations_label.place(relx=0.5, rely=0.25, anchor=tk.N)

        stationary_label = gui_elements.create_label(master, "imgs/stationary_label.png")
        stationary_label.place(relx=0.5, rely=0.5, anchor=tk.N)

        # Frames
        routes_button_frame1 = gui_elements.create_frame(master, "TFrame")
        routes_button_frame1.place(relx=0.5, rely=0.075, anchor=tk.N)

        routes_button_frame2 = gui_elements.create_frame(master, "TFrame")
        routes_button_frame2.place(relx=0.5, rely=0.16, anchor=tk.N)

        locations_button_frame1 = gui_elements.create_frame(master, "TFrame")
        locations_button_frame1.place(relx=0.5, rely=0.325, anchor=tk.N)

        locations_button_frame2 = gui_elements.create_frame(master, "TFrame")
        locations_button_frame2.place(relx=0.5, rely=0.41, anchor=tk.N)

        stationary_button_frame1 = gui_elements.create_frame(master, "TFrame")
        stationary_button_frame1.place(relx=0.5, rely=0.575, anchor=tk.N)

        stationary_button_frame2 = gui_elements.create_frame(master, "TFrame")
        stationary_button_frame2.place(relx=0.5, rely=0.67, anchor=tk.N)

        stop_button_frame = gui_elements.create_frame(master, "TFrame")
        stop_button_frame.place(relx=0.5, rely=0.8, anchor=tk.N)

        shiny_check_frame = gui_elements.create_frame(master, "TFrame")
        shiny_check_frame.place(relx=0.5, rely=0.9, anchor=tk.N)

        # Route buttons
        self.start_route1_button = gui_elements.create_button(routes_button_frame1, "Route 1",
                                                              lambda: self.start_auto_loop('route1'))
        self.start_route22_button = gui_elements.create_button(routes_button_frame1, "Route 22",
                                                               lambda: self.start_auto_loop('route22'))
        self.start_route8_button = gui_elements.create_button(routes_button_frame2, "Route 8",
                                                              lambda: self.start_auto_loop('route8'))
        # Location buttons
        self.start_viridian_forest_button = gui_elements.create_button(locations_button_frame1, "Viridian Forest",
                                                                       lambda: self.start_auto_loop('viridian_forest'))
        # Stationary buttons
        self.start_eevee_button = gui_elements.create_button(stationary_button_frame1, "Start Eevee",
                                                             lambda: self.start_auto_loop('eevee'))
        self.start_aero_button = gui_elements.create_button(stationary_button_frame1, "Start Fossil",
                                                            lambda: self.start_auto_loop('aero'))
        self.start_starter_button = gui_elements.create_button(stationary_button_frame1, "Start Starter",
                                                               lambda: self.start_auto_loop('starter'))
        self.start_snorlax_button = gui_elements.create_button(stationary_button_frame2, "Start Snorlax",
                                                               lambda: self.start_auto_loop('snorlax'))
        self.start_legends_button = gui_elements.create_button(stationary_button_frame2, "Start Legends",
                                                               lambda: self.start_auto_loop('legends'))

        # Stop button
        self.stop_button = gui_elements.create_button(stop_button_frame, "Stop Loop", self.stop_auto_loop)
        self.stop_button.config(state=tk.DISABLED)

        # Shiny testing buttons
        self.shiny_check_button = gui_elements.create_button(shiny_check_frame, "Shiny Check",
                                                             lambda: shiny_detector.shiny_frame_detection(self))
        self.shiny_test_button = gui_elements.create_button(shiny_check_frame, "Shiny Test",
                                                            lambda: self.start_auto_loop('test'))

    def start_auto_loop(self, loop):
        try:
            if not self.running:
                self.running = True
                self.start_eevee_button.config(state=tk.DISABLED)
                self.start_aero_button.config(state=tk.DISABLED)
                self.start_starter_button.config(state=tk.DISABLED)
                self.start_snorlax_button.config(state=tk.DISABLED)
                self.start_legends_button.config(state=tk.DISABLED)
                self.start_route1_button.config(state=tk.DISABLED)
                self.start_route22_button.config(state=tk.DISABLED)
                self.start_route8_button.config(state=tk.DISABLED)
                self.start_viridian_forest_button.config(state=tk.DISABLED)
                self.stop_button.config(state=tk.NORMAL)
                self.shiny_check_button.config(state=tk.DISABLED)
                self.shiny_test_button.config(state=tk.DISABLED)

                if loop == 'route1':
                    self.loop_thread = Thread(target=custom_loops.route1_loop, args=(self, self.target_window))
                elif loop == 'route22':
                    self.loop_thread = Thread(target=custom_loops.route22_loop, args=(self, self.target_window))
                elif loop == 'route8':
                    self.loop_thread = Thread(target=custom_loops.route8_loop, args=(self, self.target_window))
                elif loop == 'viridian_forest':
                    self.loop_thread = Thread(target=custom_loops.viridian_forest_loop, args=(self, self.target_window))
                elif loop == 'eevee':
                    self.loop_thread = Thread(target=custom_loops.eevee_loop, args=(self, self.target_window))
                elif loop == 'aero':
                    self.loop_thread = Thread(target=custom_loops.aero_loop, args=(self, self.target_window))
                elif loop == 'starter':
                    self.loop_thread = Thread(target=custom_loops.starter_loop, args=(self, self.target_window))
                elif loop == 'snorlax':
                    self.loop_thread = Thread(target=custom_loops.snorlax_loop, args=(self, self.target_window))
                elif loop == 'legends':
                    self.loop_thread = Thread(target=custom_loops.legends_loop, args=(self, self.target_window))
                elif loop == 'test':
                    self.loop_thread = Thread(target=custom_loops.shiny_test, args=(self, self.target_window))

                self.loop_thread.start()

        except Exception as e:
            print(f"An error occurred: {e}")

    def stop_auto_loop(self):
        try:
            if self.running:
                self.running = False
                self.start_route1_button.config(state=tk.NORMAL)
                self.start_route22_button.config(state=tk.NORMAL)
                self.start_route8_button.config(state=tk.NORMAL)
                self.start_viridian_forest_button.config(state=tk.NORMAL)
                self.start_eevee_button.config(state=tk.NORMAL)
                self.start_aero_button.config(state=tk.NORMAL)
                self.start_starter_button.config(state=tk.NORMAL)
                self.start_snorlax_button.config(state=tk.NORMAL)
                self.start_legends_button.config(state=tk.NORMAL)
                self.stop_button.config(state=tk.DISABLED)
                self.shiny_check_button.config(state=tk.NORMAL)
                self.shiny_test_button.config(state=tk.NORMAL)

        except Exception as e:
            print(f"An error occurred: {e}")

    def on_close(self):
        self.stop_auto_loop()
        if self.loop_thread:
            self.loop_thread.join()
        self.master.destroy()


def main():
    gui.create_window(ShinyLoops)


if __name__ == "__main__":
    main()