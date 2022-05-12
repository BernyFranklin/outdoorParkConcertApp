# tickets.py
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
    under15 = False
    qtyOfTix = 0
    # Start loop
    while not number or not positive or not under15:
        try:
            # Prompt for input
            qtyOfTix = input("\nPlease enter how many tickets you would like to purchase: ")
            # Pass input to isNumeric(), bool value
            number = isNumeric(qtyOfTix)
            # Test for positive input, bool value
            positive = (int(qtyOfTix) > 0)
            # Test for max number of tickets (15), bool value
            under15 = (int(qtyOfTix) <= 15)   
            # If negative
            if not positive:
                print("Quantity must be a positive number")
            # If too many tickets
            if not under15:
                print("Quantity may not exceed 15 tickets")
            # If zero selected
            if int(qtyOfTix) == 0:
                print("\nZero tickets selected, returning to main menu\n")
                break
        # Catch non number values
        except ValueError:
            print("\nPlease enter numbers only\n")

    # After validity check, return int qtyOfTix
    return qtyOfTix

def section():
    """
    This function Prompts user for desired section and returns a valid char
    """
     # Prompt for section selection
    print("\nPlease select a section")
    print("[F] Front  $80")
    print("[M] Middle $50")
    print("[B] Back   $25")

    # Prime loop
    charSection = ""
    valid = False

    # Loop for valid input
    while not valid:
        # Read input from keyboard
        userSection = input("\nEnter a selection: ")
        # Convert to upper
        upperSection = userSection.upper()
        # Pull first char
        charSection = upperSection[0:1]

        # Validate Entry
        if (charSection == 'F') or (charSection == 'M') or (charSection == 'B') :
            # Set true to break out of loop
            valid = True
        else:
            # Alert user invalid selection, loop continues
            print("Please select a valid section")
    # Returns valid section
    return charSection

def isNumeric(qty):
    """
    This function verifies ticket quantity is numeric using regex and returns a bool
    """
    # Sets regex criteria
    numeric = re.compile(r'([0-9])+')
    # If matches criteria, set true
    if re.fullmatch(numeric, qty):
        return True
    # If not set false
    else:
        return False

def compute(qty, section):
    """
    This module computes the total price for selected qty and section and returns the total
    """

    q = qty         # Sent from UI
    s = section     # Sent from UI, can only be F, M, or B
    tax = 0.0725    # Tax rate at 7.25% 
    fee = 5.0       # $5 Masking fee

    # Establish which ticket price to use
    if s == 'F':        # Front
        price = 80.0
        sString = "Front"
    elif s ==  'M':     # Middle
        price = 50.0
        sString = "Middle"
    else:               # Back
        price = 25.0
        sString = "Back"

    # Compute total
    subTotal = int(q) * price
    totalTax = subTotal * tax
    finalTotal = subTotal + totalTax + fee

    # Print subtotal
    print("\n========================================")
    print("         Transaction Summary\n")
    print("Qty:\t\t", str(q), " @\t", str("${:.2f}".format(price)))
    print("Section:\t\t", str(sString))
    print("Subtotal:\t\t", str("${:.2f}".format(subTotal)))
    print("Tax:\t\t\t", str("${:.2f}".format(totalTax)))
    print("Mandatory Mask Fee:\t", str("${:.2f}".format(fee)))
    print("\n")
    print("Total:\t\t\t", str("${:.2f}".format(finalTotal)))

    # Return final total for transaction object
    return finalTotal
