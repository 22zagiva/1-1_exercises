#!/usr/bin/env python3

# display a welcome message
print("The Miles Per Gallon program")
print()

# get input from the user
length = int(input("please enter the length: "))
width = int(input("please enter the width:\t "))

# calculate area and perimeter
are = length * width
peri = length * 2 + width * 2
            
# format and display the result
print()
print("area:\t  " + str(are))
print("perimeter: " + str(peri))
print()
print("Bye")


