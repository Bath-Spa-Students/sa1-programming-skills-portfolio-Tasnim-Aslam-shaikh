#The correct password
correct_password = "123456"

#Make a loop to ask for the password 
while True:
    #Ask the user to enter the password
    entered_password = input("Enter the password: ")
    
    #Check if the entered password is the correct one
    if entered_password == correct_password:
        print("Access has been granted.")
        break  #If the given password is correct
    else:
        print("Incorrect password. Retry again.")
