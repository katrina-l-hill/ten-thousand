import sys
from collections import Counter

from ten_thousand.game_logic import GameLogic
from ten_thousand.banker import Banker


class Game:
    def __init__(self):
        self.bank = Banker()

    score = 0
    round_num = 0
    die = 6

    def rounds(self, total, local_total, round_num, die, roller):
        round_num += 1
        input_is_valid = False  # flag

        print(f"Starting round {round_num}")
        print(f"Rolling {die} dice...")
        # store tuple of roll for later use
        roll = list(roller(die))
        roll_input = " ".join(
            map(str, (roll))
        )  # removing everything except for the numbers, using them on line 27

        while input_is_valid is False:
            print(f"*** {roll_input} ***")
            print("Enter dice to keep, or (q)uit:")
            response = input("> ")
            input_is_valid = GameLogic.validate_keepers(roll_input, response)

        if response == "q":
            print(f"Thanks for playing. You earned {total} points")
            sys.exit()

        else:
            dice_to_keep = [int(x) for x in str(response)]
            die = die - len(dice_to_keep)
            local_total += GameLogic.calculate_score(tuple(dice_to_keep))
            print(f"You have {local_total} unbanked points and {die} dice remaining")
            print("(r)oll again, (b)ank your points or (q)uit:")
            response = input("> ")

            # renamed from dice_to_keep because it's what they're requesting to keep, not what's being kept
            # dice_requested = [int(x) for x in str(response)]
            # # assigned empty tuple to variable for dice being kept
            # dice_to_keep = tuple()
            # for loop for dice requested to keep, remove from list of dice, and start another round
            # for dice in dice_requested:
            #     if dice in roll:
            #         dice_to_keep += dice
            #         roll.remove(dice)

            if input_is_valid is False:
                print("Cheater!!! Or possibly made a typo....")
                # need to show user the same roll numbers they rolled prior to being a cheater
                print(f"*** {roll_input} ***")
                print("Enter dice to keep, or (q)uit:")
                response = input("> ")
                is_cheater = GameLogic.validate_keepers(roll_input, response)

            # else:

            #     # calling function to start another round
            #     self.rounds(local_total, local_total, round_num, die, roller)
            # #     return
            # # die = die - len(dice_to_keep)
            # # local_total += GameLogic.calculate_score(tuple(dice_to_keep))
            # # print(f"You have {local_total} unbanked points and {die} dice remaining")
            # # print("(r)oll again, (b)ank your points or (q)uit:")
            # # response = input("> ")

            elif response == "r":
                self.rounds(local_total, local_total, round_num, die, roller)

            elif response == "b":
                self.bank.shelf(local_total)
                local_total = self.bank.bank()
                total += local_total
                print(f"You banked {local_total} points in round {round_num}")
                print(f"Total score is {total} points")
                local_total = 0
                die = 6
                self.rounds(total, local_total, round_num, die, roller)
            else:
                print(f"Thanks for playing Ten Thousand")
                sys.exit()

        # handle zilch to check
        zilch_points = [int(x) for x in str(roll)]
        check_for_zilch = GameLogic.calculate_score(tuple(zilch_points))
        if check_for_zilch == 0:
            self.bank.clear_shelf()
            # round is over
            print(
                """
            ****************************************
**        Zilch!!! Round over         **
****************************************
            """
            )
            # need to bypass the rounds while loop
            print(f"You banked {local_total} points in round {round_num}")
            print(f"Total score is {total} points")
            print("Thanks for playing. You earned {total} points")
        else:
            print("Enter dice to keep, or (q)uit:")
            response = input("> ")

    def play(self, roller=GameLogic.roll_dice):

        round_num = 0
        total = 0
        die = 6
        local_total = 0

        print("Welcome to Ten Thousand")
        print("(y)es to play or (n)o to decline")
        response = input("> ")

        if response == "n":
            print("OK. Maybe another time")

        if response == "y":
            self.rounds(total, local_total, round_num, die, roller)


if __name__ == "__main__":
    game = Game()
    game.play()
