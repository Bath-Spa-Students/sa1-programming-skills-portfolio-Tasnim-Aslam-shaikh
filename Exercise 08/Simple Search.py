student = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]
print (student[4])

#List of string names
student = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

#Type the sting name you want to search for from the above
search_student = "Sam"

#Search for the name from the list above
if search_student in student:
    print("student was mentioned in the list")
else:
    print("student was not mentioned in the list")