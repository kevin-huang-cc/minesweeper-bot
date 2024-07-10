import PIL.Image
import pyautogui
import pygetwindow
from PIL import Image, ImageGrab
import mss
import mss.tools

# where to store the screenshot
# fp = "/Users/cc/Desktop/pd_python_game/pythonProject/minesweeper_screenshot.png"


class MinesweeperScreenshot:
    x1, y1, x2, y2, width, height, xcor, ycor = 0, 0, 0, 0, 0, 0, 0, 0
    width_screenshot, height_screenshot = 0, 0

    def __init__(self, game_mode):
        """getting the region of the mind
        and adjusting to the macbook retina display"""
        if game_mode.lower() == "beginner":
            pass
        elif game_mode.lower() == "intermediate":
            self.x1, self.y1, self.width, self.height = 503, 327, 384, 384
        elif game_mode.lower() == "expert":
            pass
        else:
            print("Now only support Beginner, Intermediate and Expert")
        """self.x2 = self.x1 + self.width
        self.y2 = self.y1 + self.height
        # img.save(fp)

        self.x1 = self.x1 * 2 + 30
        self.y1 = self.y1 * 2 + 288
        self.x2 = self.x2 * 2 - 30
        self.y2 = self.y2 * 2 - 30
        self.xcor = self.x1 / 2
        self.ycor = self.y1 / 2
        self.width_screenshot = self.width * 2 - 60
        self.height_screenshot = self.height * 2 - 318"""

    def get_titles(self):
        """get all titles of windows"""
        titles = pygetwindow.getAllTitles()
        print(titles)

    def get_screenshot(self):
        """taking screenshots of the mine region"""
        """# name of window is "Minesweeper Minesweeper"
        x1, y1, width, height = pygetwindow.getWindowGeometry("Minesweeper Minesweeper")
        x2 = x1 + width
        y2 = y1 + height
        pyautogui.screenshot(path)
        img = Image.open(path)"""

        with mss.mss() as sct:
            """get the screen part to capture"""
            print(self.x1)
            region = {'top': self.y1, 'left': self.x1,
                      'width': self.width, 'height': self.height}

            # Grab the data
            img = sct.grab(region)
            img = Image.frombytes("RGB", img.size, img.bgra, "raw", "BGRX")
            img.show()

        return img


screenshot = MinesweeperScreenshot("intermediate")
screenshot.get_screenshot()
