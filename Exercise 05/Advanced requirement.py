#Make a dictionary with months as keys and number of days as the values
days_in_month = {
    1: 31, #January
    2: 28, #February (when a non-leap year)
    3: 31, #March
    4: 30, #April
    5: 31, #May
    6: 30, #June
    7: 31, #July
    8: 31, #August
    9: 30, #September
    10: 31, #October
    11: 30, #November
    12: 31 #December
}

#Ask the user to input the month in number that they wanna know about
while True:
    month = int(input("Enter the month number (1-12): "))
    
    #Check if the month is given in a valid input
    if month in days_in_month:
        #Separate handling for February (Adjustment for leap year)
        if month == 2:
            #Ask user if it's a leap year
            is_leap_year = input("Is it a leap year? (yes/no): ").strip().lower()
            if is_leap_year == 'yes':
                print("February has 29 days in a leap year.")
            else:
                print("February has 28 days in a non-leap year.")
        else:   #Output the number of days for the given month other then February
            print(f"The month {month} has {days_in_month[month]} days.") 
    else:
        print("Invalid month number. Please enter a number between 1 and 12.")
else:
    print("Please enter a valid integer for the month number.")