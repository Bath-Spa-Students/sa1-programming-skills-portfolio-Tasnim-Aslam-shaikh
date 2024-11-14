#Program that collect user's name, hometown, and age, and prints them.

#First is to collect user's info
Users_name = input("Enter your full name: ") #User must type their name
Users_hometown = input("Enter your hometown: ") #User must type their hometown

#Rectifiying wrong input to stop the error
while True:
    Users_age = input("Enter your age: ")  #The info should be an integer 
    if Users_age.isdigit():  #Check if the input is a digit
        Users_age = int(Users_age)  #Convert age to integer
        break  #If age is valid
    else:
        print("Please enter your age in digits.")

#Add the information in a dictionary to store it
user_info = {
    "Name": Users_name,
    "Hometown": Users_hometown,
    "Age": Users_age
}

# Print the values on separate lines using a single print() statement
print(f"\nName: {user_info['Name']}\nHometown: {user_info['Hometown']}\nAge: {user_info['Age']}")
