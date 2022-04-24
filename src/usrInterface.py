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

    # Call login() to get userName
    userName = login.login()

    # Call runApp with userName as param
    runApp(userName)

def runApp(userName):
    """
    This function welcomes the user by email, gives options to view seating, purchase tickets,
    search by email, display all purchases or quit
    """

    # Store userName for purchase info
    user = userName

    print("========================================")
    print("Welcome " + user)
    print()
    print("Please select from the following options")
    print("[V] View Seating")
    print("[B] Buy tickets")
    print("[S] Search by email")
    print("[D] Display all purchases")
    print("[Q] Quit")
    print("========================================")
    
    userOption = input("Please enter a command: ")
    lowerOption = userOption.lower()
    firstChar = lowerOption[0:1]



   