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

    @staticmethod
    def check_for_zilch(keepers):
        if GameLogic.calculate_score(tuple(keepers)) == 0:
            return True

        else:
            return False

    def rounds(self, total, local_total, round_num, die, roller):
        round_num += 1
        input_is_valid = True  # flag
        zilch = False

        print(f"Starting round {round_num}")
        print(f"Rolling {die} dice...")
        # store tuple of roll for later use

        while input_is_valid is True:
            roll = list(roller(die))
            roll_input = " ".join(map(str, roll))  # removing everything except for the numbers, using them on line 27
            print(f"*** {roll_input} ***")
            zilch = self.check_for_zilch(roll)
            if zilch:
                self.zilch_is_yes(round_num, self.bank.balance)

            else:
                print("Enter dice to keep, or (q)uit:")
                response = input("> ")

                if response == "q":
                    print(f"Thanks for playing. You earned {self.bank.balance} points")
                    sys.exit()
                else:
                    dice_to_keep = [int(x) for x in str(response)]
                    input_is_valid = GameLogic.validate_keepers(roll, dice_to_keep)
                    if input_is_valid is False:
                        print(f"*** {roll_input} ***")
                        print("Enter dice to keep, or (q)uit:")
                        response = input("> ")

                        if response == "q":
                            print(f"Thanks for playing. You earned {self.bank.balance} points")
                            sys.exit()
                        else:
                            die = die - len(dice_to_keep)
                            local_total += GameLogic.calculate_score(tuple(dice_to_keep))
                            print(f"You have {local_total} unbanked points and {die} dice remaining")
                            print("(r)oll again, (b)ank your points or (q)uit:")
                            response = input("> ")

                            if response == "r":
                                roll = list(roller(die))
                                roll_input = " ".join(
                                    map(str, roll))  # removing everything except for the numbers, using them on line 27
                                print(f"*** {roll_input} ***")
                                zilch = self.check_for_zilch(roll)
                                if zilch:
                                    self.zilch_is_yes(round_num, self.bank.balance)
                                else:
                                    dice_to_keep = [int(x) for x in str(response)]
                                    input_is_valid = GameLogic.validate_keepers(roll, dice_to_keep)
                                    if input_is_valid is False:
                                        print(f"*** {roll_input} ***")
                                        print("Enter dice to keep, or (q)uit:")
                                        response = input("> ")
                                        if die = 0:
                                        ## need to say game over if dice is 0


                            elif response == "b":
                                self.bank.shelf(local_total)
                                local_total = self.bank.bank()
                                print(f"You banked {local_total} points in round {round_num}")
                                print(f"Total score is {self.bank.balance} points")
                                local_total = 0
                                die = 6
                                self.play()

                            elif response == "q":
                                print(f"Thanks for playing. You earned {self.bank.balance} points")
                                sys.exit()

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
            while True:
                round_num += 1
                self.rounds(total, local_total, round_num, die, roller)

    @staticmethod
    def zilch_is_yes(round_num, total):
        print(
            """
    ****************************************
    **        Zilch!!! Round over         **
    ****************************************
    """
        )

        print(f"You banked 0 points in round {round_num}")
        print(f"Total score is {total} points")
        return

    @staticmethod
    def game_over():

if __name__ == "__main__":
    game = Game()
    game.play()
