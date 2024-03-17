import pygetwindow as gw
from config import config


def detect_window():
    target_window = gw.getWindowsWithTitle(config.TARGET_APP_TITLE)

    if not target_window:
        print(f"Error: Window with title '{config.TARGET_APP_TITLE}' not found.")
        exit()

    return target_window[0]