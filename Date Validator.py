# This program determines if a date entered by the user is valid.  
year = int(input("Enter the year: ")) # Input: year
month = int(input("Enter the month: ")) # Input: month
day = int(input("Enter the day: ")) # Input: day
# Output: Valid date is printed or user is alerted that an invalid date was entered.

validDate = True
MIN_YEAR = 0
MIN_MONTH = 1
MAX_MONTH = 12
MIN_DAY = 1
MAX_DAY = 31

# Check to be sure date is valid
if year <= MIN_YEAR: # invalid year
    validDate = False
elif int(month) < MIN_MONTH or int(month) > MAX_MONTH: # invalid month
    validDate = False
elif int(day) < MIN_DAY or int(day) > MAX_DAY: # invalid day
    validDate = False

# Test to see if date is valid and output date and whether it is valid or not

if validDate == True:
    print(f"{month}/{day}/{year} is a valid date.")
    # Output statement
else: 
    print(f"{month}/{day}/{year} is not a valid date.")
    # Output statement
