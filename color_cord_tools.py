import pyautogui
from pynput import mouse
from PIL import ImageGrab, Image
import time
import pygetwindow

fp = "/Users/cc/Desktop/pd_python_game/pythonProject/minesweeper_screenshot.png"


def find_color():
    time.sleep(3)
    x, y = pyautogui.position()
    x *= 2
    y *= 2
    rgb = ImageGrab.grab().getpixel((x, y))
    r = rgb[0]
    g = rgb[1]
    b = rgb[2]
    print(r, g, b)


def on_click(x, y, button, pressed):
    print('{0} at {1}'.format(
        'Pressed' if pressed else 'Released',
        (x, y)))
    if not pressed:
        # Stop listener
        return False


def find_cor():
    listener = mouse.Listener(on_click=on_click)
    listener.start()
    listener.join()


def check_pixel_color(x, y):
    img = Image.open(fp)
    print(img.getpixel((x, y)))

# code of adding two numeric tuples:
# actual_cord = tuple(map(lambda i, j: i + j, (x1, y1), cord))


def check_screen_pixel_color(x, y):
    rgb = ImageGrab.grab().getpixel((x, y))
    pyautogui.moveTo(x, y)
    r = rgb[0]
    g = rgb[1]
    b = rgb[2]
    print(r, g, b)


def check_mine_color(row, list_):
    row -= 1
    list_ -= 1
    x1, y1, width, height = pygetwindow.getWindowGeometry("Minesweeper Minesweeper")
    x = x1 + 15 + 15 + list_ * 30
    y = y1 + 144 + 9 + row * 30
    pyautogui.moveTo(x, y)
    pyautogui.click()

    print(pyautogui.pixel(x * 2, y * 2))


#find_color()
#find_cor()
"""pyautogui.moveTo(401, 383)
pyautogui.leftClick()
pyautogui.leftClick()"""
#check_pixel_color(480, 150)
check_screen_pixel_color(480, 185)
#check_mine_color(1, 2)

