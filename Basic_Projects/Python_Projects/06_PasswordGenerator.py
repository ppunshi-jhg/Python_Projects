import secrets
import string

def contains_uppercase(password: str) -> bool:
    for char in password:
        if char.isupper():
            return True
    return False

def contains_symbol(password:str) -> bool:
    for char in password:
        if char in string.punctuation:
            return True
    return False

def generate_password(length, symbols:bool, uppercase:bool):
    combination = string.ascii_lowercase + string.digits
    
    if symbols:
        combination+= string.punctuation
    if uppercase:
        combination+= string.ascii_uppercase
        
    password = ''
    combination_length = len(combination)
    
    for _ in range(length):
        password += combination[secrets.randbelow(combination_length)]
        
    return password

if __name__ == "__main__":
    for i in range(5):
        new_password = generate_password(12,True,True)
        specs = f"Uppercase: {contains_uppercase(new_password)}, Symbol: {contains_symbol(new_password)}"
        print(f" {i}: {new_password} | {specs}")