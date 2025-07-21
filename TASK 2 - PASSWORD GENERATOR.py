import random
import string

print("Welcome to the Password Generator!\n")

try:
    length = int(input("Enter the desired password length: "))

    if length <= 0:
        print("Password length must be greater than zero.")
    else:
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        print("\nYour generated password is:")
        print(password)

except ValueError:
    print("Invalid input. Please enter a valid number.")
