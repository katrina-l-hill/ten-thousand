from distutils.sysconfig import get_makefile_filename
import random
from random import randint, sample
from collections import Counter


class GameLogic:
    def __init__(self):
        pass

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

        # elif nums_rolled[1] == 1 and nums_rolled[5] == 1:
        #     score += 150
        #     return score
        #
        #
        #
        # for num in nums_rolled:
        #
        #     if nums_rolled[num] == 6:
        #         score += num * 400
        #
        #     elif nums_rolled[num] == 5:
        #         score += num * 300
        #
        #     elif nums_rolled[num] == 4:
        #         score += num * 200
        #
        #     elif nums_rolled[num] == 3:
        #         triples.append(num)
        #         score += num * 100
        #
        # if nums_rolled[1] == 3 and nums_rolled[5] == 1:
        #     score += 1050
        #
        # elif nums_rolled[1] == 3:
        #     score += 1000
        #
        #     # if nums_rolled[1] == 3:
        #     #     score += 1000
        #
        # return score

        # count1 = 0
        # count2 = 0
        # count3 = 0
        # count4 = 0
        # count5 = 0
        # count6 = 0
        #
        # for i in len(roll):
        #     if i == 1:
        #         count1 += 1
        #     elif i == 2:
        #         count2 += 1
        #     elif i == 3:
        #         count3 += 1
        #     elif i == 4:
        #         count4 += 1
        #     elif i == 5:
        #         count5 += 1
        #     elif i == 6:
        #         count6 += 1
