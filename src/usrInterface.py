import io
import login
import re



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
    
    # Prime loop
    userQuit = False

    # Start menu loop
    while not userQuit:

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
        
        # Collect userOption, covert to lower, and take firstChar
        userOption = input("Please enter a command: ")
        upperOption = userOption.upper()
        firstChar = upperOption[0:1]

        # Proceed to menu choices

        # [V]
        if firstChar == 'V':
            print("View seating selected")

        # [B]
        elif firstChar == 'B':
            # Prime loop
            number = False
            positive = False
            while not number and not positive:
                try:
                    qtyOfTix = input("Please enter how many tickets you would like to purchase: ")
                    number = isNumeric(qtyOfTix)
                    if int(qtyOfTix) > 0:
                        positive = True
                    elif int(qtyOfTix) == 0:
                        print("Zero tickets selected, returning to main menu")
                        print()
                        break
                    else:
                        print("Number of tickets must be positive number")
                        print()

                except ValueError:
                    print("Please enter numbers only")
                    print()
            
            # Return to main menu if zero tickets purchased
            if int(qtyOfTix) == 0:
                continue
                
            print()
            print("Please select a section")
            print("[F] Front  $80")
            print("[M] Middle $50")
            print("[B] Back   $25")
            
            userSection = input("Enter a selection: ")

        # [S]
        elif firstChar == 'S':
            print("Search selected")

        # [D]
        elif firstChar == 'D':
            print("Display purchases selected")

        # [Q]
        elif firstChar == 'Q':
            print("Thank you for using the FrankFest App")
            userQuit = True

        # Invalid
        else:
            print("Invlid selection, please try again")

def isNumeric(qty):
    numeric = re.compile(r'([0-9])+')

    if re.fullmatch(numeric, qty):
        return True
    else:
        return False



   