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

# Test output
data = read()

print(data)