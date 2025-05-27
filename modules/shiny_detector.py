import time
from PIL import ImageGrab
from config import config


def shiny_frame_detection(self):
    # Screenshots the top left side of the screen
    time.sleep(0.5)
    screenshot = ImageGrab.grab()

    left, top = config.SQUARE_POSITION
    right, bottom = left + config.SQUARE_SIZE[0], top + config.SQUARE_SIZE[1]
    square = screenshot.crop((left, top, right, bottom))

    # Return True if frame is shiny
    if any(pixel == config.SHINY_FRAME_COLOR for pixel in square.getdata()):
        print("WOOHOO! It's a shiny!")
        self.stop_auto_loop()
    else:
        print("No shiny detected")


def wild_detection():
    # Screenshots the top left side of the screen
    screenshot = ImageGrab.grab()

    left, top = config.SQUARE_POSITION
    right, bottom = left + config.SQUARE_SIZE[0], top + config.SQUARE_SIZE[1]
    square = screenshot.crop((left, top, right, bottom))

    # Return True if frame is shiny
    return any(pixel == config.HP_BAR for pixel in square.getdata())


def wild_shiny_detection(self, encounters):
    # Screenshots the top left side of the screen
    screenshot = ImageGrab.grab()

    left, top = config.SQUARE_POSITION
    right, bottom = left + config.SQUARE_SIZE[0], top + config.SQUARE_SIZE[1]
    square = screenshot.crop((left, top, right, bottom))

    # Return True if frame is shiny
    for encounter in encounters:
        if any(pixel == encounter for pixel in square.getdata()):
            print("It's a shiny!")
            self.stop_auto_loop()