import pyautogui
from PIL import Image


class ToArrays:
    pyautogui.PAUSE = 0
    fp = "/Users/cc/Desktop/pd_python_game/pythonProject/minesweeper_screenshot.png"
    block_in_row, block_in_list, block_size, length, height = 0, 0, 0, 0, 0
    x1, y1 = 0, 0
    all_cord, all_mine_rgb, all_mine = [], [], []
    img = None
    sleep_time = 0
    game_over = False

    def __init__(self, game_mode, x1, y1, img):
        # open image, set row and list number for each difficulty
        # get length and height of mine
        self.img = img
        self.length, self.height = self.img.size
        self.x1 = x1
        self.y1 = y1
        self.all_cord, self.all_mine_rgb, self.all_mine = [], [], []

        # easy is 9 * 9, hard is 16 * 16, Expert is ???
        if game_mode.lower() == "easy":
            self.block_in_row, self.block_in_list = 9, 9
            self.sleep_time = .1
        elif game_mode.lower() == "hard":
            self.block_in_row, self.block_in_list = 16, 16
            self.sleep_time = .17
        elif game_mode.lower() == "expert":
            self.block_in_row, self.block_in_list = 30, 16
            self.sleep_time = .5
        else:
            print("No such mode")

        self.block_size = self.length / self.block_in_row
        """for i in range(81):
            self.num_array.append(i + 1)"""

    def cord_array(self):
        # create two-dimensional array with coordinates
        cord_in_row = []
        for j in range(self.block_in_list):
            for k in range(self.block_in_row):
                cord_in_row.append([self.block_size * (.5 + k), self.block_size * (.5 + j)])
                if len(cord_in_row) == self.block_in_row:
                    self.all_cord.append(cord_in_row)
                    cord_in_row = []

        # printing out the array
        """for i in range(len(self.all_cord)):
            print(self.all_cord[i])"""
        return self.all_cord

    def mine_array(self, img):
        # find the coordination of each mine on the screen
        mine_in_row = []
        self.all_mine = []
        for row in range(self.block_in_list):
            for list_ in range(self.block_in_row):
                # print("This is all cord: ", self.all_cord)
                # print(cord)
                image = img
                rgb = image.getpixel((self.all_cord[row][list_][0], self.all_cord[row][list_][1] - 5))
                r = rgb[0]
                g = rgb[1]
                b = rgb[2]
                self.all_mine_rgb.append([r, g, b])
                if 195 <= r <= 204:
                    # _ for unchecked
                    mine_in_row.append("_")
                elif 181 <= r <= 188:
                    # F for flag
                    mine_in_row.append("F")
                    # S for safe
                elif 195 <= r <= 204:
                    mine_in_row.append("S")
                elif r <= 4 and b >= 240:
                    mine_in_row.append("1")
                elif 72 <= r <= 80:
                    mine_in_row.append("2")
                elif 222 <= r <= 230:
                    mine_in_row.append("3")
                elif 17 <= r <= 25 and 128 <= b <= 136:
                    mine_in_row.append("4")
                elif 148 <= r <= 156:
                    mine_in_row.append("5")
                elif 40 <= r <= 48:
                    mine_in_row.append("6")
                elif r <= 5:
                    mine_in_row.append("B")
                    self.game_over = True
                else:
                    mine_in_row.append("?")
                    """print((self.all_cord[row][list_][0], self.all_cord[row][list_][1] - 12))
                    print(r)"""

                if len(mine_in_row) == self.block_in_row:
                    self.all_mine.append(mine_in_row)
                    mine_in_row = []

        # printing out rbg and number
        index_list = []
        for i in range(len(self.all_mine)):
            index_list.append(str(i))
        print(" ", index_list)
        for i in range(len(self.all_mine)):
            print(i, self.all_mine[i])
        print(" " * 40)
        print("*" * 40)
        print(" " * 40)

        return self.all_mine

    def create_array(self, img):
        array_of_cords = self.cord_array()
        array_of_mines = self.mine_array(img)

        return array_of_cords, array_of_mines

