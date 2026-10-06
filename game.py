import random
from logic import feedback


class Mastermind:
    def __init__(self):
        self.code = [str(random.randint(1, 6)) for _ in range(4)]
        self.max_turns = 10
        self.history = []
        self.game_over = False
        self.won = False

    def run(self):
        print("Mastermind — enter four digits from 1 to 6.")

        while len(self.history) < self.max_turns and not self.game_over:
            turns_left = self.max_turns - len(self.history)
            guess = input(f"{turns_left} turns left > ")

            if guess.lower() == "q":
                print("Game ended.")
                self.game_over = True
                break

            if len(guess) != 4 or any(ch not in "123456" for ch in guess):
                print("Invalid guess. Enter exactly four digits from 1 to 6.")
                continue

            exact, partial = feedback(self.code, guess)

            self.history.append((guess, exact, partial))

            print(f"Exact: {exact} Partial: {partial}")

            if exact == 4:
                self.won = True
                self.game_over = True
                print("You won!")
                break

        if not self.won and not self.game_over:
            self.game_over = True
            print(f"You lost! The code was {''.join(self.code)}.")