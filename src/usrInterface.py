# userInterface.py
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
                 This is the main module that runs throughout the app.
"""

def start():
    """
    This function prints a banner to welcome the user, calls for login, and runs the app passing the userName
    """
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
    search by name, display all purchases or quit
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
        print("[S] Search by name")
        print("[D] Display all purchases")
        print("[Q] Quit")
        print("\n========================================\n")
        
        # Collect userOption, covert to upper, and take firstChar
        userOption = input("Please enter a command: ")
        upperOption = userOption.upper()
        firstChar = upperOption[0:1]

        # Proceed to menu choices

        # [V]
        if firstChar == 'V':
            # Call seating.displaySeatingChart(), prints current seating
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
            # Call seating.seatSearch() for the requested qty of seats in that section 
            # and store seats
            seats = seating.seatSearch(int(qtyOfTix), selectedSection)
            
            # Store the User's name for purchase data and search by name
            name = input("Please enter your name for confirmation: ")
            # Convert to title (capitalizes 1st letter of each word)
            name = name.title()

            #If no seats available break out
            if seats[1] == 99:
               # Inform user there aren't enough seats to fill request
               print("\nThere aren't any seats left in that section for qty requested\n")
            # Seats were found
            else:
               # Call tickets.compute() passing qty and section, store double
               total = tickets.compute(qtyOfTix, selectedSection)
               # Call seating.updateSeatingChart() passing assigned seats to update JSON file
               seating.updateSeatingChart(seats)
               # Call purchases.addTransaction() passing all purchase info to update JSON file
               purchases.addTransaction(user, name, qtyOfTix, selectedSection, total)

        # [S]
        elif firstChar == 'S':
            # Call purchases.searchByName() to initiate search
            purchases.searchByName()

        # [D]
        elif firstChar == 'D':
            # Call purchases.printAllTransactions() to print all transactions and total $
            purchases.printAllTransactions()

        # [Q]
        elif firstChar == 'Q':
            # Print thank you and exit the loop, ends program
            print("\nThank you for using the FrankFest App\n")
            userQuit = True

        # Invalid
        else:
            # Let the user know they're option no worky
            print("Invlid selection, please try again")
