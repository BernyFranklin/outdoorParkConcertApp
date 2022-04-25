import io
import re

"""
    Module: Tickets
    Description: This module processes all aspects of purchasing tickets.
"""

def quantity():
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

def isNumeric(qty):
    """
    This function verifies ticket quantity is numeric and returns a bool
    """

    numeric = re.compile(r'([0-9])+')

    if re.fullmatch(numeric, qty):
        return True
    else:
        return False