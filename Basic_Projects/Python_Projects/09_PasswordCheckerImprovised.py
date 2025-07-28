# In this we want to check if the password is common or noot from common passwords text file
import string

def check_password(password: str) -> str:

    password = password.strip()

    with open('C:\\Users\\arora\\OneDrive - John Holland Group\\Github Repos\\Python Projects\\Basic_Projects\\commonpasswords.txt', 'r') as file:
        common_passwords = [line.strip() for line in file if line.strip()] #Here we read the common passwords from the file, list comprehension is used to remove any empty line, so the if condition runs first and strips any extra spaces leading or trailing and after striping if the line is not empty then it is added to the list. and we have used for line in file to iterate through each line in the file. because if we for line in file.read() then it will read the whole file as a single string and we will not be able to iterate through each line. or it will iterate through each character in the file. 
        
        
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
