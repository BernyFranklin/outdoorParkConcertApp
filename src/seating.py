import io
import json

"""
    Module: seating
    Description: this module handles everything for seating
"""

def read():
    """
    This function opens the seating.json file and reads the data into 
    a variable.
    """

    # Path to seating.json
    filePath = "/Users/frankbernal/Documents/GitHub/outdoorParkConcertApp/src/seating.json"

    # Open file
    try:
        fileHandle = open(filePath)
    except IOError:
        print("Error loading file")
        raise IOError

    # Read the file
    data = json.load(fileHandle)

    # Return variable to caller
    return data

def status(row, col):
    """
    This function uses the read() function to store the JSON file into a variable. 
    Then the data is read into an empty dictionary.
    Seat selection status displayed based on params row and col
    """
    # Read json into a variable
    data = read()

    # Create empty dictionary
    seatingDict = {}

    # Read data into dictionary
    for elem in data:
        r = elem["row"]
        c = elem["col"]
        s = elem["status"]

        # Set key values to status
        seatingDict[(r, c)] = s

    # Get status of seat stated in params, if seat doesn't exist raise error
    try:
        stat = seatingDict[(row, col)]
        return stat
    except KeyError:
        return "Seat selection out of range"
    # Return status of seat
    #return stat

def displaySeatingChart():
    # Matrix has 20 rows and 26 columns and one header row
    n_row = 20
    n_col = 26
    h_row= 1

    # Names of colums for alpha numeric seating
    colList = ["A", "B", "C", "D", "E", "F", "G", "H", "I",
            "J", "K", "L", "M", "N", "O", "P", "Q", "R", 
            "S", "T", "U", "V", "W", "X", "Y", "Z"]

    # Border
    print("=============================================================")
    # Print explanation of chart
    print("a = Available")
    print("n = Not Available")
    print("x = Social Distancing Barriers")
     
    # Print available seating
    print() # Blank line to break up display
    # Used to start a new row
    for r in range(h_row):
        # Start row with a tab
        print(end="\t")
        # Continue to iterate through the column names
        for c in range(n_col):
            print(colList[c], end=" ")
        
    print("\n") #Blank line to break up display
    for r in range(n_row):
        print(r, end="\t")
        for c in range(n_col):
            print(status(r, c), end=" ")
        print()
    # Border
    print("=============================================================\n")
