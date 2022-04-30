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
        """Entry point for playing the game"""
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
        """print the start of the round"""
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

   

if __name__ == "__main__":
    game = Game()
    game.play()
