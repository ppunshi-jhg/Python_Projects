import time
import string
import itertools #Helps provides a collection of fast, memory-efficient tools that are useful by themselves or in combination. It is used for creating iterators for efficient looping.

def common_words(word: str) -> str | None:
    word = word.strip()
    with open(r"C:\Users\arora\OneDrive - John Holland Group\Github Repos\Python Projects\Basic_Projects\commonwords.txt", encoding="utf-8", mode = "r") as file:
        common_words: list[str] = [line.strip() for line in file if line.strip()]
    
    for idx, common in enumerate(common_words):
        if word == common:
            return f"Word is too common: {word}. Please choose a different word. {idx}"
    return None
    
def brute_force(word: str, length: int, digits: bool = False, symbols:bool = False) -> str:
    chars : str = string.ascii_lowercase
    if digits:
        chars += string.digits
    if symbols:
        chars += string.punctuation
    
    attempts: int = 0
    for guess in itertools.product(chars, repeat = length):
        attempts += 1
        guess_word = ''.join(guess)
        
        if guess_word == word:
            return f"Password found: {guess_word} in {attempts} attempts."

def main():
    print("Searching..")
    password: str = "abc123"
    
    start_time: float = time.perf_counter()
    
    if common_match := common_words(password):
        print(common_match)
    else:
        if cracked := brute_force(password, len(password), digits=True, symbols=True):
            print(cracked)
        else:
            print("Password not found.")
            
    end_time: float = time.perf_counter()
    print(round(end_time - start_time, 2), "seconds elapsed.")
        
    
if __name__ == "__main__":
    main()
