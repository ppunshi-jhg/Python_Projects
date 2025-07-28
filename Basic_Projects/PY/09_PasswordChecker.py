import string
def check_password(password:str) -> str:
    password = password.strip()
    
    min_length = 8
    
    hasUpper = any(char.isupper() for char in password)
    hasLower = any(char.islower() for char in password)
    hasDigit = any(char.isdigit() for char in password)
    hasSpecial = any(char in string.punctuation for char in password)
    
    if len(password) < min_length: 
        return "Password must be at least 8 characters long."
    
    if not (hasUpper and hasLower and hasDigit and hasSpecial):
        return "Password must contain at least one uppercase letter, one lowercase letter, one digit, and one special character."
    
    return "Password is valid."

def main():
    while True:
        try:
            password = input("Enter your password: ")
            if password.lower() == 'exit':
                print("Exiting the password checker.")
                break
            result = check_password(password)
            print(result)
        except Exception as e:
            print(f"An error occurred: {e}")
    
if __name__ == "__main__":
    main()
        
        