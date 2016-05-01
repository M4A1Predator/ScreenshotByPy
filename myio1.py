import datetime
import time
import win32api
import win32con
import os

import screenshoter


def get_datetime():
    date = datetime.datetime.now()
    i = 1
    print(date.strftime('%I : %M : %S - %p '))
    i += 1


def get_filename():
    date = datetime.datetime.now()
    name = "pic-{}-{}.png".format(date.strftime('%m-%d-%y'), int(time.time()))
    return name


def get_key():
    if win32api.GetAsyncKeyState(win32con.VK_INSERT):
        print("Ins pressed")
        screenshoter.take_photo(get_filename())
    elif win32api.GetAsyncKeyState(win32con.VK_ESCAPE):
        exit()


def main():
    root = os.getcwd()
    save_path = root+"\\pics"
    os.chdir(save_path)
    while True:
        get_datetime()
        get_key()
        time.sleep(1)


if __name__ == '__main__':
    print("start")
    main()
