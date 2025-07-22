import string
import itertools

def common_words(word: str) -> str | None:
    word = word.strip()
    with open(r"C:\Users\arora\OneDrive - John Holland Group\Github Repos\Python Projects\Basic_Projects\commonwords.txt", encoding="utf-8", mode = "r") as file:
        common_words = [line.strip() for line in file if line.strip()]
    
    for idx, common in enumerate(common_words):
        if word == common:
            return f"Word is too common: {word}. Please choose a different word. {idx}"
    return "Not found in common words list."
    

def main():
    print(common_words("hello"))
    
if __name__ == "__main__":
    main()
