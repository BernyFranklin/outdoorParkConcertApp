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
    This function takes row and col as parameters and returns status of that seat
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

    # Get status of seat stated in params
    stat = seatingDict[(row, col)]
    # Return status of seat
    return stat

stat = status(1, 4)
print(stat)
