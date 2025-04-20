"""
This program calculates prices for custom house signs.
"""

# Declare and initialize variables here.
# Charge for this sign.
charge = 0.0
# Number of characters.
numChars = 8
# Color of characters.
color = "gold"
# Type of wood.
woodType = "oak"
# Write assignment and if statements here as appropriate.
# Base charge for this sign is $35.00.
charge = 35.00
# Add $4.00 for each character over 5.
if numChars > 5:
    charge += (numChars - 5) * 4.00
#Extra charge for gold coloring
if color == "gold":
    charge += 15.00
# Extra charge for oak wood.
if woodType == "oak":
    charge += 20.00


# Output Charge for this sign.
print("The charge for this sign is $" + str(charge))