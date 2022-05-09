import seating
import io
import json

"""
    Module: purchases
    Description: This module will handle all aspects of handling transaction data
"""

def addTransaction(email, numOfTix, section, total):
    """
    This function opens purchaseData.json and stores the data into a list called purchaseList.
    A dictionary is created for the purchase data called transactionDict. 
    The dictionary is appended to the list. The updated list is written back to the json file. 
    """
    # File opened and stored in list
    purchaseList = seating.read("purchaseData")
    # Dictionary created with passed data
    transactionDict = { "email": email,
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
