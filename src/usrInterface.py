import io
import login
import tickets
import seating
import purchases



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

        print("\n========================================")
        print("                Main Menu               ")
        print("========================================")
        print("Welcome " + user)
        print("\nPlease select from the following options\n")
        print("[V] View Seating")
        print("[B] Buy tickets")
        print("[S] Search by email")
        print("[D] Display all purchases")
        print("[Q] Quit")
        print("\n========================================\n")
        
        # Collect userOption, covert to lower, and take firstChar
        userOption = input("Please enter a command: ")
        upperOption = userOption.upper()
        firstChar = upperOption[0:1]

        # Proceed to menu choices

        # [V]
        if firstChar == 'V':
           seating.displaySeatingChart() 

        # [B]
        elif firstChar == 'B':
            # Print menu selection
            print("========================================")
            print("              Buy Tickets               ")
            print("========================================")
            #initialize seats
            seats = []
            # Call tickets.quantity for numeric verification
            qtyOfTix = tickets.quantity()
            
            # Return to main menu if zero tickets purchased
            if int(qtyOfTix) == 0:
                continue
            
            # Call tickets.section for char selection
            selectedSection = tickets.section()
            # Search for seats in that section, store seats
            seats = seating.seatSearch(int(qtyOfTix), selectedSection)
            
            # Store the User's name for purchase data and search by name
            name = input("Please enter your name for confirmation: ")

            #If no seats available break out
            if seats[1] == 99:
               print("\nThere aren't any seats left in that section for qty requested\n")
            else:
               total = tickets.compute(qtyOfTix, selectedSection)
               seating.updateSeatingChart(seats)
               purchases.addTransaction(user, name, qtyOfTix, selectedSection, total)

        # [S]
        elif firstChar == 'S':
            print("Search selected")

        # [D]
        elif firstChar == 'D':
            purchases.printAllTransactions()

        # [Q]
        elif firstChar == 'Q':
            print("\nThank you for using the FrankFest App\n")
            userQuit = True

        # Invalid
        else:
            print("Invlid selection, please try again")




   