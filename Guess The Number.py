import random

def guess_number():
    number_to_guess = random.randint(1, 100)
    guess_count = 0
    while guess_count < 10:
        guess = int(input("Guess a number between 1 and 100: "))
        guess_count += 1
        if guess == number_to_guess:
            print("Congratulations! You guessed the number correctly.")
            break
        elif guess < number_to_guess:
            print("Too low, try again.")
        else:
            print("Too high, try again.")
    if guess_count == 10:
        print("Sorry, you didn't guess the number. The number was", number_to_guess)

guess_number()