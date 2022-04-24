import io
import getpass
import re

"""
    Module: login
    Description: This module lets the user login using a valid email address,
                 verified using regex and submitting a password
"""


def login():
    # Prime loop
    emailValid = False
    # Start loop for email validation
    while (emailValid == False):
        # Prompt user for emailAddress
        emailAddress = input("Email: ")
        emailValid = isValid(emailAddress)
    
    password = getpass.getpass("Password: ")


    return emailAddress

def isValid(email):
    # Create regex for valid email
    regex = re.compile(r'([A-Za-z0-9\._-]+)@([A-Za-z0-9\._-])+(\.[A-Za-z]{2,})+')

    # Check for validity
    if re.fullmatch(regex, email):
        return True
    else:
        print("Invalid Email, please try again")
        return False


