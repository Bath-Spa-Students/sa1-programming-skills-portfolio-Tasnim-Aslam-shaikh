#First, store the information is different variables
Name= "Tasnim Aslam Shaikh" #Add name as a string to the variable
Hometown= "Mumbai" #Add howmtown name as a string to the variable
Age= 17 #Add an integer for the variable

#Second, add the information a dictionary to store it
Bio = {
    "Name" : Name,
    "Hometown" : Hometown,
    "Age" : Age
}

#Third, Print the information in separate lines using just a single print statement
print (f"Name: {Bio['Name']}\nHometown: {Bio['Hometown']}\nAge: {Bio['Age']}")