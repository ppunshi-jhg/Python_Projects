import random
import sys

class RockPaperScissors:
    def __init__(self):
        self.valid_choices = ["rock", "paper", "scissors", "exit"]
        
    def user_choice(self):
        while True:
            user_input = input(f"Enter your choice: rock, paper, or scissors or type exit to quit: ").lower()
            if user_input not in self.valid_choices:
                print(f"Please enter the valid choices: {', '.join(self.valid_choices)}")
                continue
            if user_input == "exit":
                print(f"Exiting the game. Goodbye!")
                sys.exit()
            return user_input
    
    def ai_choice(self):
        return random.choice(self.valid_choices[:-1])
    
    def determine_winner(self, user_turn, ai_turn):
        if user_turn == ai_turn:
            print(f"Its a tie! Both chose {user_turn}.")
        elif (user_turn == "rock" and ai_turn == "scissors") or \
             (user_turn == "paper" and ai_turn == "rock") or \
             (user_turn == "scissors" and ai_turn == "paper"):
                 print(f"You win! {user_turn} beats {ai_turn}. ")
        elif user_turn == "exit":
            print(f"Exiting the game.Goodbye!")
        else:
            print(f"You lose! {ai_turn} beats {user_turn}. ")
            
    def run_game(self):
        print(f"Welcome to the game of Rock, Paper, Scissors!")
        while True:
           user_turn = self.user_choice()
           ai_turn = self.ai_choice()
           self.determine_winner(user_turn, ai_turn)

if __name__ == "__main__":
    game = RockPaperScissors()
    game.run_game()
