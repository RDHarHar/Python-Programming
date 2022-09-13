# Python Programming
# Practice Program 2 - Greatest Common Divisor

infinite = 1

while infinite == 1:
    terminate = 0

    largeInt = int(input("Please enter in the larger of the numbers (only whole numbers please): "))
    smallInt = int(input("Please enter in the smaller of the numbers (only whole numbers please): "))

    origLarge = largeInt
    origSmall = smallInt

    if largeInt < 0 or smallInt < 0:
        print("One of the numbers you entered was less than 0. This program will now restart.")
        terminate = 1

    if smallInt > largeInt:
        print("The smaller number you entered is larger than the large number you entered. The program will now restart.")
        terminate = 1

    if terminate == 0:
        while smallInt != 0:
            holder = smallInt
            smallInt = largeInt % smallInt
            largeInt = holder

        if smallInt == 0:
            greatCommDiv = largeInt
            print(f"The greatest common divisior of ", origLarge, " and ", origSmall, " is ", greatCommDiv, ".")