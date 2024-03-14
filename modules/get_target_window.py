import pygetwindow as gw

TARGET_APP_TITLE = 'Playback'


def detect_window():
    target_window = gw.getWindowsWithTitle(TARGET_APP_TITLE)

    if not target_window:
        print(f"Error: Window with title '{TARGET_APP_TITLE}' not found.")
        exit()

    return target_window[0]