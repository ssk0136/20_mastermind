import random
from logic import feedback


class Mastermind:
    def __init__(self):
        self.history = []
        self.game_over = False
        self.won = False
        self.code = []
        self.code_length = 4
        self.symbol_limit = 6
        self.max_turns = 10

    def choose_difficulty(self):
        print("Choose difficulty:")
        print("1. Easy")
        print("2. Medium")
        print("3. Hard")

        while True:
            choice = input("Enter 1, 2, or 3: ")

            if choice == "1":
                self.code_length = 4
                self.symbol_limit = 4
                self.max_turns = 12
                break

            if choice == "2":
                self.code_length = 4
                self.symbol_limit = 6
                self.max_turns = 10
                break

            if choice == "3":
                self.code_length = 5
                self.symbol_limit = 8
                self.max_turns = 8
                break

            print("Invalid choice.")

    def run(self):
        self.choose_difficulty()

        self.code = [
            str(random.randint(1, self.symbol_limit))
            for _ in range(self.code_length)
        ]

        print(
            f"Mastermind — enter {self.code_length} digits "
            f"from 1 to {self.symbol_limit}."
        )

        while len(self.history) < self.max_turns and not self.game_over:
            turns_left = self.max_turns - len(self.history)
            guess = input(f"{turns_left} turns left > ")

            if guess.lower() == "q":
                print("Game ended.")
                self.game_over = True
                break

            valid_symbols = "12345678"[:self.symbol_limit]

            if (
                len(guess) != self.code_length
                or any(ch not in valid_symbols for ch in guess)
            ):
                print(
                    f"Invalid guess. Enter exactly {self.code_length} digits "
                    f"from 1 to {self.symbol_limit}."
                )
                continue

            exact, partial = feedback(self.code, guess)

            self.history.append((guess, exact, partial))

            print(f"Exact: {exact} Partial: {partial}")

            if exact == self.code_length:
                self.won = True
                self.game_over = True
                print("You won!")
                break

        if not self.won and not self.game_over:
            self.game_over = True
            print(f"You lost! The code was {''.join(self.code)}.")