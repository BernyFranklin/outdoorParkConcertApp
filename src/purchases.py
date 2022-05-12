import seating
import json

"""
    Module: purchases
    Description: This module will handle all aspects of handling transaction data
"""

def addTransaction(email, name, numOfTix, section, total):
    """
    This function opens purchaseData.json and stores the data into a list called purchaseList.
    A dictionary is created for the purchase data called transactionDict. 
    The dictionary is appended to the list. The updated list is written back to the json file. 
    """
    # File opened and stored in list
    purchaseList = seating.read("purchaseData")
    # Dictionary created with passed data
    transactionDict = { "email": email,
                        "name": name,
                        "qty": numOfTix,
                        "section": section,
                        "total": total }
    # Dict appended to list
    purchaseList.append(transactionDict)
    # JSON serialized
    jsonObject = json.dumps(purchaseList, indent = 4)
    # JSON updated with new data
    with open("purchaseData.json", "w") as purchaseFile:
        purchaseFile.write(jsonObject)

def printAllTransactions():
    """
    This function prints a list of all transactions to include name, number of tickets sold, section, and total.
    Counts are kept for how many tickets in each section and the entire venue, as well as grand total for event.
    At the end of the list data for each section, venue, and grand total are displayed. 
    """
    # Load data from json file to list
    transactionList = seating.read("purchaseData")

    # Keep track of how many transactions and how many each section
    transactionCount = 0
    frontCount = 0
    middleCount = 0
    backCount = 0
    totalCount = 0
    grandTotal = 0.0

    # Header for selection
    print("========================================")
    print("         Display All Purchases          ")
    # Iterate through items
    for i in transactionList:
        # Count the transaction
        transactionCount += 1
        
        # Count for each section
        if i["section"] == "F":
            frontCount += int(i["qty"])
        elif i["section"] == "M":
            middleCount += int(i["qty"])
        elif i["section"] == "B":
            backCount += int(i["qty"])

        # Add transaction total to grandTotal
        grandTotal += i["total"]

        # Print data for each transaction
        print("========================================")
        print("Transaction: " + str(transactionCount))
        print("Name:\t\t\t" + str(i["name"]))
        print("Number of Tickets:\t" + str(i["qty"]))
        print("Section:\t\t" + str(i["section"]))
        print("Total:\t\t\t" + str("${:.2f}\n".format(i["total"])))
    
    # Calculate total of tickets sold
    totalCount = frontCount + middleCount + backCount

    # Print totals for entire event
    print("========================================")
    print("             Total purchases            ")
    print("========================================")
    print("Front section:\t" + str(frontCount))
    print("Middle section:\t" + str(middleCount))
    print("Back section:\t" + str(backCount))
    print("Entire venue:\t" +str(totalCount))
    print("\nGrand total:\t" + str("${:.2f}\n".format(grandTotal)))
    
def searchByName():
    """
    This function will search transactions by name and display the data associated with that name.
    """
    #Print menu selection
    print("\n========================================")
    print("             Search By Name            ")
    print("=======================================\n")

    # Store data from JSON into a list
    listOfTransactions = seating.read("purchaseData")

    # Ask for user's search name
    nameToSearch = input("Enter a name to search: ")
    # Convert to title to match format of json
    nameToSearch = nameToSearch.title()

    # Keep track of matches
    matchCount = 0
    # Iterate through data
    for transaction in listOfTransactions:
        # If name matches name in dict element, print the data
        if nameToSearch in transaction["name"]:
            print("------------------------------")
            print("Name:\t\t\t" + str(transaction["name"]))
            print("Section:\t\t" + str(transaction["section"]))
            print("Number of tickets:\t" + str(transaction["qty"] + "\n"))
            matchCount += 1
    
    # If no matches, inform user
    if matchCount == 0:
        print("\nSorry, we didn't find any purchases under that name\n")
    # If 1 match print "match"
    elif matchCount == 1:
        print("We found " + str(matchCount) + " match with the name " + nameToSearch + "\n")
    # If more matches print "matches"
    else:
        print("We found " + str(matchCount) + " matches with the name " + nameToSearch + "\n")
