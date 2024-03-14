import time
from PIL import ImageGrab

SHINY_FRAME_COLOR = (107, 227, 231)
HP_BAR = (255, 251, 222)
SQUARE_POSITION = (0, 0)
SQUARE_SIZE = (500, 500)


def shiny_frame_detection(self):
    # Screenshots the top left side of the screen
    time.sleep(0.5)
    screenshot = ImageGrab.grab()

    left, top = SQUARE_POSITION
    right, bottom = left + SQUARE_SIZE[0], top + SQUARE_SIZE[1]
    square = screenshot.crop((left, top, right, bottom))

    # Return True if frame is shiny
    if any(pixel == SHINY_FRAME_COLOR for pixel in square.getdata()):
        print("WOOHOO! It's a shiny!")
        self.stop_auto_loop()


def shiny_check(self):
    if shiny_frame_detection(self):
        print("Shiny detected!")
    else:
        print("No shiny detected")


def wild_detection():
    # Screenshots the top left side of the screen
    time.sleep(0.1)
    screenshot = ImageGrab.grab()

    left, top = SQUARE_POSITION
    right, bottom = left + SQUARE_SIZE[0], top + SQUARE_SIZE[1]
    square = screenshot.crop((left, top, right, bottom))

    # Return True if frame is shiny
    return any(pixel == HP_BAR for pixel in square.getdata())


def wild_shiny_detection(self, encounters):
    # Screenshots the top left side of the screen
    time.sleep(0.5)
    screenshot = ImageGrab.grab()

    left, top = SQUARE_POSITION
    right, bottom = left + SQUARE_SIZE[0], top + SQUARE_SIZE[1]
    square = screenshot.crop((left, top, right, bottom))

    # Return True if frame is shiny
    for encounter in encounters:
        if any(pixel == encounter for pixel in square.getdata()):
            print("It's a shiny!")
            self.stop_auto_loop()