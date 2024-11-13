#Make a dictionary with months as keys and number of days as the values
days_in_month = {
    1: 31,  # January
    2: 28,  # February 
    3: 31,  # March
    4: 30,  # April
    5: 31,  # May
    6: 30,  # June
    7: 31,  # July
    8: 31,  # August
    9: 30,  # September
    10: 31, # October
    11: 30, # November
    12: 31  # December
}

#Ask the user to input the month in number that they wanna know about
while True:
    month = int(input("Enter the month (1-12): "))

#Check if the month is given in a valid input
    if 1 <= month <= 12:
        #Output the number of days for the given month
        print(f"The month {month} has {days_in_month[month]} days.")
    else:
        print("Please enter a valid month number between 1 and 12.")
else:
    print("Invalid input. Please enter a numeric value between 1 and 12.")