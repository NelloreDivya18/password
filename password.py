import random
import string

def generate_password(length):
    # Define characters to be used in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate password using random.choice
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    try:
        length = int(input("Enter the desired length of the password: "))
        if length <= 0:
            print("Please enter a positive length.")
            return
        password = generate_password(length)
        print("Your generated password is:", password)
    except ValueError:
        print("Please enter a valid integer for the length.")

if __name__ == "__main__":
    main()
