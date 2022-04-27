import sys

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

        print(f"Starting round {round_num}")
        print(f"Rolling {die} dice...")
        roll_input = ' '.join(map(str, (roller(die))))
        print(f"*** {roll_input} ***")
        print("Enter dice to keep, or (q)uit:")
        response = input("> ")

        if response == "q":
            print(f"Thanks for playing. You earned {total} points")
            sys.exit()

        else:
            dice_to_keep = [int(x) for x in str(response)]
            die = die - len(dice_to_keep)
            local_total += GameLogic.calculate_score(tuple(dice_to_keep))
            print(f"You have {local_total} unbanked points and {die} dice remaining")
            print("(r)oll again, (b)ank your points or (q)uit:")
            response = input('> ')

            if response == "r":
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

    def play(self, roller=GameLogic.roll_dice):

        round_num = 0
        total = 0
        die = 6
        local_total = 0

        print('Welcome to Ten Thousand')
        print('(y)es to play or (n)o to decline')
        response = input('> ')

        if response == "n":
            print("OK. Maybe another time")

        if response == "y":
            self.rounds(total, local_total, round_num, die, roller)


if __name__ == "__main__":
    game = Game()
    game.play()
