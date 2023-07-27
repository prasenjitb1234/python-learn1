# random password generator

import random
import string

def generate_random_password(length=12):
    # Define all the characters that can be used in the password
    valid_characters = string.ascii_letters + string.digits + string.punctuation

    # Initialize an empty string to store the generated password
    password = ""

    # Loop to create the password of the desired length
    for _ in range(length):
        # Choose a random character from the valid characters and add it to the password
        random_character = random.choice(valid_characters)
        password += random_character

    return password

if __name__ == "__main__":
    # Ask the user for the desired password length
    password_length = int(input("Enter the desired length of the password: "))

    # Generate the random password
    generated_password = generate_random_password(password_length)

    # Display the generated password
    print("Generated Password:", generated_password)
