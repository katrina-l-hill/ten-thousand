import sys
from ten_thousand.game_logic import GameLogic
from ten_thousand.banker import Banker


class Game:
    """main game class"""

    def __init__(self, total_rounds=20):
        self.bank = Banker()
        self.total_rounds = total_rounds
        self.round_num = 0

    def play(self, roller=GameLogic.roll_dice):
        """starts the game"""
        self.roller = roller

        self.welcome()
        self.play_rounds()
        self.game_over()

    def welcome(self):
        print("Welcome to Ten Thousand")
        print("(y)es to play or (n)o to decline")
        response = input("> ")

        if response == "n":
            print("OK. Maybe another time")
            sys.exit()


    def start_round(self):
        """starts the round"""
        print(f"Starting round {self.round_num}")

    def end_round(self):
        """bank and complete the round"""
        local_total = self.bank.bank()
        print(f"You banked {local_total} points in round {self.round_num}")
        print(f"Total score is {self.bank.balance} points")

    def play_rounds(self):
        """use the round limit set in game init"""
        while self.round_num < self.total_rounds:
            self.round_num += 1
            self.play_the_round()

    def play_the_round(self):
        self.start_round()
        self.play_turn()
        self.end_round()

    def play_turn(self):
        num_of_dice = 6

        while True:
            roll = self.dice_roll(num_of_dice)

            if self.check_zilch(roll):
                self.zilch_is_yes()
                return
            dice_to_keep = self.collect_keepers(roll)

            num_of_dice -= len(dice_to_keep)

            print(
                f"You have {self.bank.shelved} unbanked points and {num_of_dice} dice remaining"
            )
            if num_of_dice == 0:
                num_of_dice = 6

            print("(r)oll again, (b)ank your points or (q)uit:")
            response = input("> ")
            if response == "q":
                self.game_over()
            elif response == "b":
                return

    def game_over(self):
        """closes the game"""
        print(f"Thanks for playing. You earned {self.bank.balance} points")
        sys.exit()

    def dice_roll(self, num_of_dice):
        print(f"Rolling {num_of_dice} dice...")
        roll = self.roller(num_of_dice)
        formatted_roll = self.format_roll(roll)
        print(formatted_roll)
        return roll

    def format_roll(self, roll):
        roll_input = " ".join(map(str, roll))  # format the roll
        return f"*** {roll_input} ***"

    def check_zilch(self, roll):
        return GameLogic.calculate_score(roll) == 0

    def zilch_is_yes(self):
        """print zilch method and clear the score"""
        self.bank.clear_shelf()

        print("****************************************")
        print("**        Zilch!!! Round over         **")
        print("****************************************")

    def collect_keepers(self, roll):  # borrowed from JB Tellez
        """set the dice to keep"""
        keeper_values = self.validate_keepers(roll)
        points_for_current_roll = GameLogic.calculate_score(keeper_values)
        self.bank.shelf(points_for_current_roll)
        return keeper_values

    def validate_keepers(self, roll):  # borrowed from JB Tellez
        """validated the kept dice"""
        while True:
            print("Enter dice to keep, or (q)uit:")
            response = input("> ")
            if response == "q":
                self.game_over()

            keeper_values = []
            for char in response:
                if char.isnumeric():
                    keeper_values.append(int(char))

            if GameLogic.validate_keepers(roll, keeper_values):
                return keeper_values
            else:

                print(self.format_roll(roll))


if __name__ == "__main__":
    game = Game()
    game.play()
