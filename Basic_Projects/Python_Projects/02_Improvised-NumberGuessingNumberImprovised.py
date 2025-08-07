'''
This is a simple number guessing game.

The computer picks a random number between 1 and 10.
You have 3 chances to guess the number.
Each time you guess:
If your guess is higher than the number, it tells you "Your number is higher".
If your guess is lower, it tells you "Your number is lower".
If you guess correctly, it says "You have guessed the number" and the game ends.
After each wrong guess, it tells you how many guesses you have left.
If you use all your guesses and don’t get the number, it tells you the correct number at the end.
If you enter something that isn’t a number, it asks you to "Please enter a valid number".
The else after the for loop runs only if you never guessed the number correctly.
'''


from random import randint

lower_number, higher_number = 1,10
random_number = randint(lower_number, higher_number)

choices = 3

for i in range(choices):
    try:
        user_guess = int(input("Guess a number from 1 to 10: "))
        if user_guess > random_number:
            print("Your number is higher")
        elif user_guess < random_number:
            print("Your number is lower")
        else:
            print("You have guessed the number")
            break       
        print(f"You have {choices - i - 1} guesses left")
    except:
        print("Please enter a valid number")
        print(f"You have {choices - i - 1} guesses left")
        continue
else:
    print(f"You have run out of your guesses. The number was {random_number}.")
    
    
#Else can be used with the for loop as well and it runs when the loop is exhausted withoout a break statement, means we never guessed the number.

