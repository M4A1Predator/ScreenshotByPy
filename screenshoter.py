import os

import datetime
from PIL import ImageGrab
import win32api
import win32gui
import time


def take_photo(name="test.png"):
    box = (0, 0, get_width(), get_height())
    im = ImageGrab.grab(box)
    im.save(name)


def get_width():
    return win32api.GetSystemMetrics(0)


def get_height():
    return win32api.GetSystemMetrics(1)


def get_window_size(hwnd, extra):
    program = win32gui.GetWindowText(hwnd)
    rect = win32gui.GetWindowRect(hwnd)
    if program != "":
        print("{} : {} x {}".format(program, rect[2]-rect[0], rect[3]-rect[1]))


def test():
    # print(win32gui.EnumWindows(get_size, None))
    pass

if __name__ == "__main__":
    test()
    print(int(time.time()))
