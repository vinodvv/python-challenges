"""
Day 6: User Name Generator

Write a function called user_name that generates a username from the user’s email.
The code should ask the user to input an email and the code should return everything before the @ sign
as their username.

For example, if someone enters ben@gmail.com, the code should return ben as their username.
"""


def user_name():
    email_address = input("Enter email address: ")
    username = email_address.split('@')[0]
    return f"The username is '{username}'."


if __name__ == "__main__":
    print(user_name())
