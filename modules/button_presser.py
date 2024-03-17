import time
import win32con
import win32gui
from modules import shiny_detector

WILD_ESCAPE_KEYS = ['z', 'z', 'z', 'right', 'down', 'x', 'z', 'z']
RESTART_KEYS = ['return', 'backspace', 'x', 'z']

virtual_key_code = {
    'return': win32con.VK_RETURN,
    'backspace': win32con.VK_BACK,
    'up': win32con.VK_UP,
    'down': win32con.VK_DOWN,
    'left': win32con.VK_LEFT,
    'right': win32con.VK_RIGHT,
    'x': ord('X'),
    'z': ord('Z'),
}


def restart_game(target_handle):
    for key in RESTART_KEYS:
        press_key_down(target_handle, key)
    time.sleep(0.1)
    for key in RESTART_KEYS:
        press_key_up(target_handle, key)


def skip_intro(self, target_handle):
    for i in range(8):
        if not self.running:
            break
        time.sleep(0.3)
        win32gui.PostMessage(target_handle, win32con.WM_KEYDOWN, ord('X'), 0)
        time.sleep(0.3)
        win32gui.PostMessage(target_handle, win32con.WM_KEYUP, ord('X'), 0)


def run_in_grass_side(self, target_handle):
    while True:
        if not self.running:
            break
        press_key(target_handle, "left", 0.03)
        press_key(target_handle, "right", 0.03)
        if shiny_detector.wild_detection():
            break


def run_in_grass_vert(self, target_handle):
    while True:
        if not self.running:
            break
        press_key(target_handle, "up", 0.03)
        press_key(target_handle, "down", 0.03)
        if shiny_detector.wild_detection():
            break


def escape_wild_battle(self, target_handle):
    for key in WILD_ESCAPE_KEYS:
        if not self.running:
            break
        press_key(target_handle, key, 0.4)


def press_loop_combination(self, target_handle, loop_keys):
    for key in loop_keys:
        if not self.running:
            break
        time.sleep(0.5)
        press_key_down(target_handle, key)
        time.sleep(0.5)
        press_key_up(target_handle, key)


def stationary_loop_combination(self, target_window, loop_keys):
    try:
        while self.running:
            target_handle = target_window._hWnd if target_window else None
            restart_game(target_handle)
            skip_intro(self, target_handle)
            press_loop_combination(self, target_handle, loop_keys)

            if shiny_detector.shiny_frame_detection(self):
                break

    except KeyboardInterrupt:
        print("Loop interrupted.")


def wild_loop_combination_side(self, target_window, encounters):
    try:
        while self.running:
            target_handle = target_window._hWnd if target_window else None
            run_in_grass_side(self, target_handle)
            if shiny_detector.wild_shiny_detection(self, encounters):
                break
            escape_wild_battle(self, target_handle)

    except KeyboardInterrupt:
        print("Loop interrupted.")


def wild_loop_combination_vert(self, target_window, encounters):
    try:
        while self.running:
            target_handle = target_window._hWnd if target_window else None
            run_in_grass_vert(self, target_handle)
            if shiny_detector.wild_shiny_detection(self, encounters):
                break
            escape_wild_battle(self, target_handle)

    except KeyboardInterrupt:
        print("Loop interrupted.")


# Functions for full key presses, only up press, and only down press
def press_key(target_handle, key, secs):
    if key in virtual_key_code:
        win32gui.PostMessage(target_handle, win32con.WM_KEYDOWN, virtual_key_code[key], 0)
        time.sleep(secs)
        win32gui.PostMessage(target_handle, win32con.WM_KEYUP, virtual_key_code[key], 0)
        time.sleep(secs)


def press_key_down(target_handle, key):
    if key in virtual_key_code:
        win32gui.PostMessage(target_handle, win32con.WM_KEYDOWN, virtual_key_code[key], 0)


def press_key_up(target_handle, key):
    if key in virtual_key_code:
        win32gui.PostMessage(target_handle, win32con.WM_KEYUP, virtual_key_code[key], 0)