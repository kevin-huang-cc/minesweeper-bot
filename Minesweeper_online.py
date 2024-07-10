import window_screenshot_online
from screenshot_to_array import ToArrays
from rule1_rule2 import RulesToClick
import time
from PIL import Image
import pyautogui


# game_mode = input("What is the difficulty?: ")
game_mode = "hard"

# instantiate classes and getting image and arrays for first analysis
screenshot = window_screenshot_online.MinesweeperScreenshot(game_mode)
img = screenshot.get_screenshot()
array_creation = ToArrays(game_mode, screenshot.x1, screenshot.y1, img)
click_action = RulesToClick(game_mode, screenshot.xcor, screenshot.ycor)
cord_array, mine_array = array_creation.create_array(img)

# click to the minesweeper window
pyautogui.leftClick(screenshot.x1, screenshot.y1)
click_action.random_click(cord_array, mine_array)

# main function
while not array_creation.game_over:
    #time0 = time.time()
    img = screenshot.get_screenshot()
    #time1 = time.time()
    cord_array, mine_array = array_creation.create_array(img)
    #time2 = time.time()
    click_action.start_clicking(cord_array, mine_array)
    #time3 = time.time()
    time.sleep(array_creation.sleep_time)

"""print(f"screenshot time: {time1 - time0}")
print(f"array creation time: {time2 - time1}")
print(f"clicking_time: {time3 - time2}")"""



