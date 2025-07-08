f'''
This program simulates rolling dice.

It asks the user how many dice they want to roll.
If the user types "exit", the program ends.
If the user enters a valid number greater than 0, it rolls that many dice.
Each die gives a random number between 1 and 6.
It prints out the result of all the dice rolls.
Finally, it thanks the user for using the simulator.
'''

from random import randint

lower_number, higher_number = 1,6
Output_lst = []

while True:
    user_input = input("How many dices you want to roll? ")
    if user_input.strip().lower() == "exit":
        print("You have exited the simulator.")
        exit()
    try:
        number_of_dices = int(user_input)
        if number_of_dices > 0:
            break
        else:
            print("Enter the number greater than 0")    
    except:
        print("Please enter the integer value greater than 0")
        
#Now do the rolling of dices

for i in range(number_of_dices):
    dice_output = randint(lower_number, higher_number)
    Output_lst.append(dice_output)

print(f"The output of the dices is: ", *Output_lst)
print(f"Thanks for using the dice simulator!")
