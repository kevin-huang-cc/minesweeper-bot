import pyautogui
import window_screenshot
import time
import random


class RulesToClick:
    """set of rules to
    1: finding out a bomb
    2: click a safe spot
    3: if cannot do 1 and 2 , click randomly"""
    pyautogui.PAUSE = 0
    cord_array, num_array, mine_array = None, None, None
    block_in_row, block_in_list = 0, 0
    rules_applied = False

    def __init__(self, game_mode, x1, y1):
        """initiate coordinate array and number array"""
        self.x1 = x1
        self.y1 = y1
        if game_mode.lower() == "easy":
            self.block_in_row = self.block_in_list = 9
        elif game_mode.lower() == "hard":
            self.block_in_row = self.block_in_list = 16
        elif game_mode.lower() == "expert":
            self.block_in_row = 30
            self.block_in_list = 16
        else:
            print("No such mode")

    def flag_n_unchecked(self, row_range, list_range, mine_array):
        """determine how many flags and unchecked blocks there are in a certain tile"""
        flag_in_tile = 0
        unchecked_in_tile = 0
        for row_3x3 in row_range:
            for list_3x3 in list_range:
                if mine_array[row_3x3][list_3x3] == "F":
                    flag_in_tile += 1
                elif mine_array[row_3x3][list_3x3] == "_":
                    unchecked_in_tile += 1
        return flag_in_tile, unchecked_in_tile

    def random_click(self, cord_array, mine_array):
        """store coordinates of unchecked boxes and
        click a unchecked box randomly if rule1 and 2 does not apply"""
        unchecked_array = []
        for row in range(len(mine_array)):
            for list_ in range(len(mine_array[row])):
                if mine_array[row][list_] == "_":
                    unchecked_array.append(cord_array[row][list_])
        random_index = random.randint(0, len(unchecked_array)-1)
        random_cor = unchecked_array[random_index]
        pyautogui.moveTo(self.x1 + random_cor[0]/2, self.y1 + random_cor[1]/2)
        pyautogui.leftClick()

    def rule_1n2(self, cord_array, mine_array):
        """clicking flags and safe spots using two rules"""
        self.rules_applied = False
        row_range, list_range = 0, 0

        # already checked dictionary stores location and checked status to
        # avoid double click
        already_checked = {}
        for j in range(self.block_in_list):
            for k in range(self.block_in_row):
                already_checked[(j, k)] = False

        # locating a tile around each block
        for row in range(self.block_in_list):
            for list_ in range(self.block_in_row):
                current_num = mine_array[row][list_]

                # only finding 2x3 for blocks on the sides and 2x2 in the corner
                if row == 0 or row == self.block_in_list-1 or list_ == 0 or list_ == self.block_in_row-1:
                    # top or bottom row
                    if row in [0, self.block_in_list-1]:
                        if row == 0:
                            row_range = [0, 1]
                        else:
                            row_range = range(self.block_in_list - 2, self.block_in_list)
                        if list_ == 0:
                            list_range = [0, 1]
                        elif list_ == self.block_in_row - 1:
                            list_range = range(self.block_in_row - 2, self.block_in_row)
                        else:
                            list_range = range(list_ - 1, list_ + 2)
                    # left or right list
                    if list_ in [0, self.block_in_row-1]:
                        if list_ == 0:
                            list_range = [0, 1]
                        else:
                            list_range = range(self.block_in_row - 2, self.block_in_row)
                        if row == 0:
                            row_range = [0, 1]
                        elif row == self.block_in_list - 1:
                            row_range = range(self.block_in_list - 2, self.block_in_list)
                        else:
                            row_range = range(row - 1, row + 2)

                else:
                    row_range = range(row - 1, row + 2)
                    list_range = range(list_ - 1, list_ + 2)

                flag_in_tile, unchecked_in_tile = self.flag_n_unchecked(row_range, list_range, mine_array)

                # Rule 1: if there are same amounts of
                # unchecked mines around a number, it is a mine
                # eg. 2_1
                #     123
                #     S1F
                if current_num.isnumeric() \
                        and (unchecked_in_tile == int(current_num) - flag_in_tile):
                    for row_3x3 in row_range:
                        for list_3x3 in list_range:
                            if mine_array[row_3x3][list_3x3] == "_" and \
                                        already_checked[(row_3x3, list_3x3)] is False:
                                pyautogui.moveTo(self.x1 + cord_array[row_3x3][list_3x3][0]/2,
                                                 self.y1 + cord_array[row_3x3][list_3x3][1]/2)
                                pyautogui.rightClick()

                                # printing out for debugging
                                """print(f"Current Number is: {current_num} located at row {row} and list{list_}")
                                print(f"current row range is: {row_range}, current list rage is: {list_range}")
                                print(
                                    f"I am right-clicking the block {mine_array[row_3x3][list_3x3]} located at row {row_3x3} and list {list_3x3}")
                                print(f"flag_in_tile is: {flag_in_tile}")
                                print(f"unchecked_in_tile is: {unchecked_in_tile}")"""
                                already_checked[(row_3x3, list_3x3)] = True
                                self.rules_applied = True
                                break

                # Rule 2: if there are same amounts of flags as current number,
                # everything around it is not a mine
                # eg. 2_1
                #     F23
                #     S1F
                elif current_num.isnumeric() and (int(current_num) == flag_in_tile):
                    """pyautogui.doubleClick(self.x1 + cord_array[row][list_][0]/2,
                                self.y1 + cord_array[row][list_][1]/2, interval=.5)"""
                    for row_3x3 in row_range:
                        for list_3x3 in list_range:
                            if mine_array[row_3x3][list_3x3] == "_" and \
                                        already_checked[(row_3x3, list_3x3)] is False:
                                pyautogui.moveTo(self.x1 + cord_array[row_3x3][list_3x3][0]/2,
                                                 self.y1 + cord_array[row_3x3][list_3x3][1]/2)
                                pyautogui.leftClick()
                                already_checked[(row_3x3, list_3x3)] = True
                                self.rules_applied = True
                                # printing out for debugging
                                """print(f"Current Number is: {current_num} located at row {row} and list{list_}")
                                print(f"current row range is: {row_range}, current list rage is: {list_range}")
                                print(f"I am left-clicking the block {mine_array[row_3x3][list_3x3]} located at row {row_3x3} and list {list_3x3}")
                                print(f"flag_in_tile is: {flag_in_tile}")"""
                                break

                else:
                    pass
                    # already_checked[(row, list_)] = True
                    """else:
                    for row_3x3 in row_range:
                        for list_3x3 in list_range:
                            if mine_array[row_3x3][list_3x3] == "_":
                                pyautogui.moveTo(self.x1 + cord_array[row_3x3][list_3x3][0] / 2,
                                                 self.y1 + cord_array[row_3x3][list_3x3][1] / 2)
                                pyautogui.leftClick()"""

    def start_clicking(self, cord_array, mine_array):
        """clicking using rule 1 and 2, if none apply then click randomly"""
        self.rule_1n2(cord_array, mine_array)
        if not self.rules_applied:
            self.random_click(cord_array, mine_array)
            self.rules_applied = False

