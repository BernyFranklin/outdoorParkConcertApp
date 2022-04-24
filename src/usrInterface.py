import io
import login


"""
    Module: userInterface
    Description: This module presents a welcome prompt, 
                 login prompt to store user data purchase, 
                and interface to navigate purchases.
"""

def start():
    print()
    print("========================================")
    print("  Welcome to FrankFest Music Festival   ")
    print("========================================")
    print()
    print("Please login with valid email to continue")
    userName = login.login()

    #Run the app after successful login