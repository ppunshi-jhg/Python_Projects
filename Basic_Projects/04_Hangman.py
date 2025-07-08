from random import choice

def run_game():
    word = choice(["python", "java", "hangman", "programming"])
    username = input(f"Enter your name: ")
    print(f"Welcome {username}! Let's play Hangman.")
    
    tries = 3
    guessed_letters = ""
    while tries > 0:
        guess = input(f"Enter a Letter to guess: ")
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetic character.")
            continue
        if guess in guessed_letters:
            print("You have already guessed that letter. Try again.")
            continue
        if guess not in word:
            print(f"Sorry, the word does not contain '{guess}'.")
            tries -= 1
            print(f"You have {tries} tries left.")
            continue
        if guess in word:
            guessed_letters += guess
            print(f"Good guess! The word contains '{guess}'.")
            word_length = len(word)
            print("_"*len(word))
            print(f"You have {tries} tries left.")
            if all(letter in guessed_letters for letter in word):
                print(f"Congratulations {username}! You guessed the word '{word}' correctly.")
                exit()
            continue
    print(f"Sorry {username}, you have run out of tries. The word was '{word}'.") 
    
run_game()  
            
            
     