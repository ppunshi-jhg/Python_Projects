from random import choice

def run_game():
    word = choice(["python", "java", "hangman", "programming"])
    username = input(f"Enter your name: ")
    print(f"Welcome {username}! Let's play the game of Hangman.")
    tries = 3
    guessed_letter = set()
    def make_display_word(word, guessed_letters):
        return ''.join(letter if letter in guessed_letters else '_' for letter in word)
    while tries > 0:
        guess = input(f"Enter a letter to guess: ")
        guess.lower()
        if len(guess)!= 1 or not guess.isalpha():
            print(f"Please enter a single alphabetic character.")
            continue
        if guess in guessed_letter:
            print(f"You have already guessed that letter. Try again.")
            continue
        if guess not in word:
            print(f"Sorry, the letter {guess} is not in word.")
            tries -= 1
            print(f"You have {tries} tries left.")
            continue
        guessed_letter.add(guess)
        print(f"Good guess! The word contains {guess}.")
        display = make_display_word(word, guessed_letter)
        print(f"Current word: {display}")
        if "_" not in display:
            print(f"Congratulations {username}! You guessed the word {word} correctly.")
            exit()
    print(f"Sorry {username}, you have run out of tries. The word was {word}.")
    
run_game()