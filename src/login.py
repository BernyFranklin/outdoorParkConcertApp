import io
import getpass
import re

"""
    Module: login
    Description: This module lets the user login using a valid email address,
                 verified using regex and submitting a password
"""


def login():
    """
    This function prompts for a valid email adress, passes user input to isValid(),
    returns bool, if true, prompts for password. Function returns emailAddress
    """
    # Prime loop
    emailValid = False
    # Start loop for email validation
    while (emailValid == False):
        # Prompt user for emailAddress
        emailAddress = input("Email: ")
        # Pass input to isValid()
        emailValid = isValid(emailAddress)
    # Uses getpass() to hide password input on cosole
    password = getpass.getpass("Password: ")
    # Returns emailAddress
    return emailAddress

def isValid(email):
    """
    This function verifies a valid email using regex. Returns bool.
    """
    # Create regex for valid email
    regex = re.compile(r'([A-Za-z0-9\._-]+)@([A-Za-z0-9\._-])+(\.[A-Za-z]{2,})+')

    # Check for validity
    # Yes it is valid
    if re.fullmatch(regex, email):
        return True
    # No it is not valid
    else:
        print("Invalid Email, please try again")
        return False
