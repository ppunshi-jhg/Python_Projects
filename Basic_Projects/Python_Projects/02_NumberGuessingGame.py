from random import randint

lower_number, higher_number = 1, 10
guess_number = randint(lower_number, higher_number)
print(guess_number)

while True:
    try:
        user_guess = int(input("Guess a number from 1 to 10: "))
        if user_guess > guess_number:
            print("Your number is higher")
        elif user_guess < guess_number:
             print("Your number is lower")
        else:
            print("Congratulations! You guessed the number!")
            break
    except:
        print("Please enter a valid number")
        continue

    