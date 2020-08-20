"""
CP1404/CP5632 - Practical - Christian Torrisi
Written practice - Password to Asterisk
"""

MIN_LENGTH = 8

password = input("Enter your password: ")

while len(password) < MIN_LENGTH:
    password = input("Error! Enter your password of 5 or more characters: ")

# print an asterisk for each character in the password
for character in password:
    print("*", end="")