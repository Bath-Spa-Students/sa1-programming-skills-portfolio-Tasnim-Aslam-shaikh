#Name the function as 'check_even_odd' that accepts a single parameter 'number'
def check_even_odd(number):
    #Try to determine weather the number is odd or even.
    if number % 2 == 0:
#If the condition is true, a message will be passed indicating the number is even.
        return f"The number {number} is even."
    else:
#If the condition is false, a message will be passed indicatinf the number is not even and insted is odd.
        return f"The number {number} is odd."

def main():
#Add the main function that will serve as the entry point.
    try:
#Add a try block to handle errors that might occure during user input.
        user_input = int(input("Enter a number: "))
#Prompt the user to enter a number.
#Call the check_even_odd function and store the result.
        result = check_even_odd(user_input)
#Print the result.
        print(result)
#If the user enters non-integer input, display an error message saying the user to enter a valid integer.
    except ValueError:
        print("Please enter a valid integer.")

#Run the main function
if __name__ == "__main__":
    main()