"""
Program: lines.py
Author: Ryan Harwick
Date: 2022-10-04

This programs reads a text file and out puts how many lines are in the program, then lets you choose an individual line to output.
"""

def createList():
    userFile = input("Please enter in the name of the file: ")
    f = open(userFile, 'r')

    usLi = []

    for line in f:        
        usLi.append(line.strip('\n'))

    return usLi

userList = createList()

while True:
    print(f"There are", len(userList), "lines in this document.")
    showLine = int(input("Enter the line number you would like to see (0 to end program): "))

    if showLine == 0:
        print("Ending program.")
        break
    elif showLine > int(len(userList)):
        print("Error: Line does not exist")
    else:
        print(f"The line", showLine, "is", userList[int(showLine - 1)])