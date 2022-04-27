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

def compute(qty, section):
    """
    This module computes the total price and returns the total
    """

    q = qty         # Sent from UI
    s = section     # Sent from UI, can only be F, M, or B
    tax = 0.0725    # Tax rate at 7.25% 
    fee = 5.0       # $5 Masking fee

    # Establish which ticket price to use
    if s == 'F':        # Front
        price = 80.0
    elif s ==  'M':     # Middle
        price = 50.0
    else:               # Back
        price = 25.0

    # Compute total
    subTotal = q * s
    totalTax = subTotal * tax
    finalTotal = subTotal + totalTax + fee

    return finalTotal

    



