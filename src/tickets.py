import io
import re

"""
    Module: Tickets
    Description: This module processes all aspects of purchasing tickets.
"""

def quantity():
    """
    This function validates quantity as a numeric value and returns a number >= 0
    """
    # Prime loop
    number = False
    positive = False
    # Start loop
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
    return qtyOfTix

def section():
    """
    This function Prompts user for desired section and returns a valid char
    """
     # Prompt for section selection  
    print()
    print("Please select a section")
    print("[F] Front  $80")
    print("[M] Middle $50")
    print("[B] Back   $25")

    # Prime loop
    charSection = ""
    # Loop for valid input
    while (charSection != 'F') or (charSection != 'M') or (charSection != 'B'):
        # Read input from keyboard
        userSection = input("Enter a selection: ")
        # Convert to upper
        upperSection = userSection.upper()
        # Pull first char
        charSection = upperSection[0:1]

        # Validate Entry
        if (charSection == 'F') or (charSection == 'M') or (charSection == 'B') :
            break
        else:
            print("Please select a valid section")

    return charSection

def isNumeric(qty):
    """
    This function verifies ticket quantity is numeric and returns a bool
    """

    numeric = re.compile(r'([0-9])+')

    if re.fullmatch(numeric, qty):
        return True
    else:
        return False