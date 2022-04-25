from distutils.sysconfig import get_makefile_filename
import random


class GameLogic:
    def __init__(self):
        pass

    # Do this last
    @staticmethod
    def calculate_score(roll):
        count1 = 0
        count2 = 0
        count3 = 0
        count4 = 0
        count5 = 0
        count6 = 0

        for i in len(roll):
            if i == 1:
                count1 += 1
            elif i == 2:
                count2 += 1
            elif i == 3:
                count3 += 1
            elif i == 4:
                count4 += 1
            elif i == 5:
                count5 += 1
            elif i == 6:
                count6 += 1

        return

    @staticmethod
    def roll_dice(num_dice):
        roll = ()
        for i in range(num_dice):
            roll += (random.randint(1, 6),)
        return roll
