# In this we want to check if the password is common or noot from common passwords text file
import string

def check_password(password: str) -> str:
    password = password.strip()
    
    with open('commonpasswords.txt', 'r') as file:
        common_passwords = file.read().splitlines()
        print(common_passwords)
        
check_password("password")