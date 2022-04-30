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



if __name__ == "__main__":
    game = Game()
    game.play()
