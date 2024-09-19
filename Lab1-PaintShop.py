# LAB 1 - THE PAINT SHOP
# Code a Python program that calculates the amount of paint you need to cover the walls in your family room. 
# The salesperson at the home improvement store told you to buy 1 gallon of paint for every 150 square feet of 
# wall you need to paint.

# Assuming that the room is rectangular in shape, the program should take in as input the width of your 
# two sets of walls and the height of the room.

# The program should output the number of gallons required to paint the room. 
# Paint is sold only by the gallon.

#Purpose/Concepts: Input and output to screen, string concatentation, datatype casting, simple math operations

###
"""

Already passed in assignment on Brightspace, 
just testing to see if I can get this to work on
GitHub

"""
###

#Initial Variable(s)
sqr_feet_per_gallon = 150

#Welcome User to the shop

print("Welcome to the Paint Shop!")
print("We only sell paint in Gallons.")
print("Let us know your room dimensions in feet and we'll find out how much paint you need.")

#Get room size from customer

walls_height = float(input("What is the height of your walls? "))
print("Your room has 4 walls.")
wall_1_length = float(input("What is the length of wall 1? "))
wall_2_length = float(input("What is the length of wall 2? "))
wall_3_length = float(input("What is the length of wall 3? "))
wall_4_length = float(input("What is the length of wall 4? "))

#Calculate amount of paint
wall_1_sqr_feet = wall_1_length * walls_height
wall_2_sqr_feet = wall_2_length * walls_height
wall_3_sqr_feet = wall_3_length * walls_height
wall_4_sqr_feet = wall_4_length * walls_height

total_sqr_feet = wall_1_sqr_feet + wall_2_sqr_feet + wall_3_sqr_feet + wall_4_sqr_feet
total_gallons = int((total_sqr_feet/sqr_feet_per_gallon))

#How much paint (in gallons) is needed for the room?

if total_gallons == 0:
    print("You need 1 gallon of paint.") #<----- Changed this because if someone only needs 0.5 gallons, they still need to buy at least 1
elif total_gallons == 1:
    print("You need 1 gallon of paint")
else:
    print("You need {0} gallons of paint".format(total_gallons))