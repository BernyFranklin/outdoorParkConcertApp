from string import ascii_uppercase
import json

"""
This test module is for experimenting creating my seating charts and loading them to a json
"""

row = []
col = []
i = 0

while i < 20:
    row.append(i)
    i += 1

for letter in ascii_uppercase:
    col.append(letter)
    
seatingDict = []
#print(row)
#print(col)

for rows in row:
    for cols in col:
        if rows%2 == 0:
            seatingDict.append({"row": rows, "col": cols, "status": "a" })
        else:
            seatingDict.append({"row": rows, "col": cols, "status": "x" })

#serialize json
json_object = json.dumps(seatingDict, indent = 4)

#write to test.json
with open("test.json", "w") as outfile:
    outfile.write(json_object)
#print(seatingDict)
