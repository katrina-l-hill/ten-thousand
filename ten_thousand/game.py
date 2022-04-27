from ten_thousand.game_logic import GameLogic
from ten_thousand.banker import Banker


class Game:
    def __init__(self):
        self.bank = Banker()

    def this_project_succs(self):
        round_num += 1
        print(f"Starting round {round_num}")
        print(f"Rolling {die} dice...")
        roll_input = ' '.join(map(str, (roller(die))))
        print(f"*** {roll_input} ***")
        print("Enter dice to keep, or (q)uit:")
        response = input("> ")

    def play(self, roller=GameLogic.roll_dice):

        def split(word):
            return [char for char in word]

        score = 0
        round_num = 0
        die = 6
        print('Welcome to Ten Thousand')
        print('(y)es to play or (n)o to decline')
        response = input('> ')

        if response == "n":
            print("OK. Maybe another time")
        else:
            round_num += 1
            print(f"Starting round {round_num}")
            print(f"Rolling {die} dice...")
            roll_input = ' '.join(map(str, (roller(die))))
            print(f"*** {roll_input} ***")
            print("Enter dice to keep, or (q)uit:")
            response = input("> ")

            if response == "q":
                print("Thanks for playing. You earned 0 points")

            else:
                dice_to_keep = [int(x) for x in str(response)]
                die = die - len(dice_to_keep)
                score = GameLogic.calculate_score(tuple(dice_to_keep))
                self.bank.shelf(score)
                print(f"You have {score} unbanked points and {die} dice remaining")
                print("(r)oll again, (b)ank your points or (q)uit:)")
                response = input('> ')

                if response == 'b':
                    score = self.bank.bank()
                    print(f"You have {score} banked points in round {round_num}")
                    print(f"Total score is {score} points")
                    round_num += 1
                    print(f"Starting round {round_num}")
                    roll_input = ' '.join(map(str, (roller(die))))
                    print(f"*** {roll_input} ***")
                    print("Enter dice to keep, or (q)uit:")
                    response = input("> ")

                    if response == "q":
                        print(f"Thanks for playing. You earned {score} points")

            # # turn the string 3335 into a list [3,3,3,5]
            # else:
            #     tuple_input = tuple(map(int, response.split(', ')))


if __name__ == "__main__":
    game = Game()
    game.play()
