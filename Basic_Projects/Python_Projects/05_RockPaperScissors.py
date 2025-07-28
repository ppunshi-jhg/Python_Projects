import random
import sys

def run_game():
    valid_choices = ["rock", "paper", "scissors", "exit"]
    
    while True:
        user_turn = input(f"Enter your choice: rock, paper, or scissors or type exit to quit: ").lower()
        if user_turn not in valid_choices:
            print(f"Please enter the valid choices: {', '.join(valid_choices)}")
            continue
        if user_turn == "exit":
            print(f"Exiting the game. Goodbye!")
            sys.exit()
        ai_turn = random.choice(["rock", "paper", "scissors"])
        print(f"AI Chose: {ai_turn}")
        
        if user_turn == ai_turn:
            print(f"It's a tie! Both chose {user_turn}.")
        elif (user_turn == "rock" and ai_turn == "scissors") or \
            (user_turn == "paper" and ai_turn == "rock") or \
            (user_turn == "scissors" and ai_turn == "paper"):
                print(f"You win! {user_turn} beats {ai_turn}. ")
               
        else:
            print(f"You lose! {ai_turn} beats {user_turn}.")
            
        
run_game()
        
    
    
    