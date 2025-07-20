# In this we want to check if the password is common or noot from common passwords text file
import string

def check_password(password: str) -> str:
    password = password.strip()

    with open('C:\\Users\\arora\\OneDrive - John Holland Group\\Github Repos\\Python Projects\\Basic_Projects\\commonpasswords.txt', 'r') as file:
        common_passwords = [line.strip() for line in file if line.strip()]
        
        
    if password in common_passwords:
        return f"Password is too common: {password}. Please choose a different password."
    
def main() -> str:
    user_password = input(f"Enter your password to check if its common: ")
    result = check_password(user_password)
    if result:
        print(result)
    else:
        print("Password is not common. You can use it.")
        
if __name__ == "__main__":
    main()
