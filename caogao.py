import pyautogui
import cv2 as cv
import numpy as np
from time import time

loop_time = time()
while(True):
    screenshot = pyautogui.screenshot()
    screenshot = np.array(screenshot)
    screenshot = cv.cvtColor(screenshot, cv.COLOR_RGB2BGR)

    cv.imshow("Computer Vision", screenshot)

    print(f"FPS {time() - loop_time}")
    loop_time = time()


    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break