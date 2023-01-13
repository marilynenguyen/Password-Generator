"""
This program allows the user to get a password with random characters .
He can choose the numbers of letters, numbers and symbols that he wants in the password 
"""

import random

# lists of letters, symbols and numbers

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
           'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
           'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

print("Welcome to the Password Generator! ")

# variable to check if the user wants to generate another password
would_continue = True

# while would_continue is true : we enter the loop until it becomes false
while would_continue:

    nr_letters = (input("How many letters would you like in your password? "))

    while nr_letters not in numbers:
        print("Error : You must enter a number. ")
        nr_letters = (input("How many letters would you like in your password? "))

    nr_letters = int(nr_letters)

    nr_symbols = (input("How many symbols would you like in your password? "))

    while nr_symbols not in numbers:
        print("Error : You must enter a number. ")
        nr_symbols = (input("How many symbols would you like in your password? "))

    nr_symbols = int(nr_symbols)

    nr_numbers = (input("How many numbers would you like in your password? "))

    while nr_numbers not in numbers:
        print("Error : You must enter a number. ")
        nr_numbers = (input("How many numbers would you like in your password? "))

    nr_numbers = int(nr_numbers)

    # initialization of password_list to empty
    password_list = []

    # loop 1 to nr_letters+1 of times to take random letters (the number of letters the user wants)
    for char in range(1, nr_letters + 1):
        # random.choice() it will pick any letter from the letter list (randomly)
        random_char = random.choice(letters)
        password_list += random_char

    for char in range(1, nr_symbols + 1):
        random_char = random.choice(symbols)
        password_list += random_char

    for char in range(1, nr_numbers + 1):
        random_char = random.choice(numbers)
        password_list += random_char

    # password_list : we shuffle all the characters in it

    random.shuffle(password_list)

    # we change the password_list into a string called password
    password = ""
    for char in password_list:
        password += char

    print(f"Here is your password: {password}")

    # answer of the user if he would like to generate an other password
    answer = input("Would you like to have another password ? Type 'yes' or 'no' : ").lower()
    # if the answer is no, we change the would_continue to False
    if answer == "no":
        would_continue = False
        print("Thank you for using the PassWord Generator")

    # if the answer is yes, the would_continue would stay at True

