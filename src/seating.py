import io
import json
from string import ascii_uppercase

"""
    Module: seating
    Description: this module handles everything for seating
"""

def read(fileName):
    """
    This function opens the seating.json file and reads the data into 
    a variable.
    """

    # Path to seating.json
    filePath = "/Users/frankbernal/Documents/GitHub/outdoorParkConcertApp/src/"
    file = fileName
    fileToOpen = str(filePath) + str(file) + ".json"

    # Open file
    try:
        fileHandle = open(fileToOpen)
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
    data = read("seating")

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
        # Return status of seat
        return "Seat selection out of range"

def displaySeatingChart():
    """
    This function prints a seating chart availability, the data is located in seating.json
    It will print 'a' for available, 'n' for not available, and 'x' for social distance barriers
    """
    # Matrix has 20 rows and 26 columns and one header row
    n_row = 20
    n_col = 26
    h_row= 1

    # Border
    print("\n=============================================================")
    print("                         View Seating                        ")
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
        for letter in ascii_uppercase:
            print(letter, end=" ")
        
    print("\n") #Blank line to break up display
    for r in range(n_row):
        print(r, end="\t")
        for c in range(n_col):
            print(status(r, c), end=" ")
        print()
    
def seatSearch(numberOfSeats, section):
    """
    This function uses section input for start and stop params for the range() function
    And iterates through the seating chart via the status() function, if 'a' is found N times,
    it will store the seat selection in a list of [row, col] values.
    """
    # Verify valid section
    if section == 'F':
        startRow = 0
        # endRow is last row in section +1 since range stop value is noninclusive
        endRow = 6         
    elif section == 'M':
        startRow = 5
        # endRow is last row in section +1 since range stop value is noninclusive
        endRow = 11
    elif section == 'B':
        startRow = 10
        # endRow is last row in section +1 since range stop value is noninclusive
        endRow = 20
    else:
        return "Invalid Section Detected\n"
    
    # seatsRequested is passed numberOfSeats
    seatsRequested = numberOfSeats
    # Counter to keep track of how many a's found
    seatsSearched = 0
    # Number of colums to iterate through
    n_col = 26
    # Empty list to store seat data
    seatsConfirmed = []
    noSeatsConfirmed = [99, 99]
    # Iterate through each row in section
    for row in range(startRow, endRow):
        # Iterate through each col in row
        for col in range(n_col):
            # If available
            if status(row, col) == 'a':
                seatsSearched += 1                                  # Update counter
                # If found requested number of available seats
                if seatsSearched == seatsRequested:                 
                    # Add seat value to list, decrement counter each append
                    while seatsSearched != 0:
                        seat = [row, (col - (seatsSearched - 1))]   # Use current col and subtract back to 1st instance
                        seatsConfirmed.append(seat)                 # Add seat to list
                        seatsSearched -= 1                          # Decrement Counter
                    # Return the list of seats
                    return seatsConfirmed
            # If unavailable
            elif (status(row, col) == 'x') or (status(row,col) == 'n'):
                # Reset counter and keep looking
                seatsSearched = 0
            
    return noSeatsConfirmed
    
def updateSeatingChart(seatList):
    """
    This function updates the seatingDict statuses from available to unavailable,
    to include 2 social distancing seats if available. Then function updates the json file
    """
    # seatList passed to seats
    seats = seatList
    # Last seat selected
    lastSeat = seats[-1]
    # emptySeat1 and emptySeat2 created after last seat
    emptySeat1 = [lastSeat[0], (lastSeat[-1] + 1)]   # lastSeat +1
    emptySeat2 = [lastSeat[0], (lastSeat[-1] + 2)]   # lastSeat +2

    # Import data from json
    data = read("seating")

    # Store data into dict
    seatingDict = {}

    # Read data into dictionary
    for elem in data:
        r = elem["row"]
        c = elem["col"]
        s = elem["status"]

        # Set key values to status
        seatingDict[(r, c)] = s

    # Set new values for each seat
    for seat in seats:
        seatingDict.update({(seat[0], seat[1]): "n"})

    # Set 2 social distance seats
    if (lastSeat[-1] + 1) <= 25:
        seatingDict.update({(emptySeat1[0], emptySeat1[1]): "x"})
    if (lastSeat[-1] + 2) <= 25:
        seatingDict.update({(emptySeat2[0], emptySeat2[1]): "x"})

    # Create empty updated list
    updatedSeatingList = []
    # Append list with new updated dict values 
    for key in seatingDict.keys():
        row = key[0]
        col = key[1]
        updatedSeatingList.append({"row": row, "col": col, "status": seatingDict[(row, col)]})
    
    # Serialize New JSON file
    jsonObject = json.dumps(updatedSeatingList, indent = 4)

    # Write to seating.json
    with open("seating.json", "w") as outfile:
        outfile.write(jsonObject)

def reinitializeSeatingJson():
    """
    This function reinitiliazes the json to display an empty venue.
    """
    r = []
    c = []
    i = 0
    j = 0
    seatingList = []

    while i < 20:
        r.append(i)
        i += 1
    while j < 26:
        c.append(j)
        j += 1
    
    for rows in r:
        for cols in c:
            if rows%2 == 0:
                seatingList.append({"row": rows, "col": cols, "status": "a" })
            else:
                seatingList.append({"row": rows, "col": cols, "status": "x" })

    #serialize json
    json_object = json.dumps(seatingList, indent = 4)

    #write to test.json
    with open("seating.json", "w") as outfile:
        outfile.write(json_object)

# Uncomment and run this module to reinitialize the seating.json file
#reinitializeSeatingJson()