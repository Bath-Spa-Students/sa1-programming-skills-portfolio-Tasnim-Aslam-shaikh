#The correct password
correct_password = "1234561234"

#Set a maximum number of attempts 
max_attempts = 5
attempts = 0

while attempts < max_attempts:
    #Ask the user to enter the password
    user_password = input("Enter the password: ")

    #Check if the entered password is the correct one
    if user_password == correct_password:
        print("Access has been granted.")
        break
    else:
        #Increasing the number of attempts and inform the user of remaining attempts
        attempts += 1
        remaining_attempts = max_attempts - attempts
        if remaining_attempts > 0:
            print(f"Incorrect password. {remaining_attempts} attempts left.")
        else:
            print("Maximum attempts reached.")