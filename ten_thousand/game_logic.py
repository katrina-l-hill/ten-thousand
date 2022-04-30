from sysconfig import get_makefile_filename
import random
from random import randint, sample
from collections import Counter


class GameLogic:
    def __init__(self):
        pass

    @staticmethod
    def validate_keepers(roll, user_input):

        for char in user_input:
            input_count = user_input.count(char)
            roll_count = roll.count(char)
            if input_count > roll_count:
                print("Cheater!!! Or possibly made a typo...")
                return False
            else:
                return True

    @staticmethod
    def roll_dice(num_dice):
        return tuple(randint(1, 6) for _ in range(0, num_dice))

    @staticmethod
    def calculate_score(tuple_input):
        score = 0
        nums_rolled = Counter(tuple_input[:6])
        straight = sorted(tuple_input)

        if nums_rolled[5] == 1 or nums_rolled[5] == 2:
            score += 50 * nums_rolled[5]
        if nums_rolled[1] == 1 or nums_rolled[1] == 2:
            score += 100 * nums_rolled[1]

        if straight == [1, 2, 3, 4, 5, 6]:
            score = 1500
            return score

        if nums_rolled[2] == 2 and nums_rolled[3] == 2 and nums_rolled[6] == 2:
            score = 1500
            return score

        for i in range(1, 7):
            if i == 1 and nums_rolled[1] == 3:
                score += 1000
            elif i != 1 and nums_rolled[i] == 3:
                score += i * 100

        for i in range(1, 7):
            if i == 1 and nums_rolled[1] == 4:
                score += 2000
            elif i != 1 and nums_rolled[i] == 4:
                score += i * 200

        for i in range(1, 7):
            if i == 1 and nums_rolled[1] == 5:
                score += 3000
            elif i != 1 and nums_rolled[i] == 5:
                score += i * 300

        for i in range(1, 7):
            if i == 1 and nums_rolled[1] == 6:
                score += 4000
            elif i != 1 and nums_rolled[i] == 6:
                score += i * 400

        return score

    @staticmethod
    def get_scorers(dice):
        scoring_dice = GameLogic.calculate_score(dice)
        if scoring_dice == 0:
            return tuple()
        scorers = []
        for i, val in enumerate(dice):
            sub_roll = dice[:i] + dice[i + 1:]
            sub_score = GameLogic.calculate_score(sub_roll)
            if sub_score != scoring_dice:
                scorers.append(val)
        return tuple(scorers)



