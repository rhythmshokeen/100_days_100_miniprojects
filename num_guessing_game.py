import random
def number_guessing_game():
    print("=== Number Guessing Game ===")
    print("I am thinking of a number between 1 and 100.")

    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue

            if guess < secret_number:
                print("Too low!")
            elif guess > secret_number:
                print("Too high!")
            else:
                print(f"Correct! You guessed it in {attempts} attempts.")
                break

        except ValueError:
            print("Invalid input. Enter only numbers.")


if __name__ == "__main__":
    number_guessing_game()