### Advanced Requirements:
# 1) Ignore Capitalization: Modify your program to accept answers regardless of the capitalization
#(e.g., "paris", "Paris", and "PaRis" should all be considered correct).

#Writing the question to the variable and modifying it to answer it no matter if it is capital or lower case 
Answer = input("What is the capital of France?:")
if Answer.strip().lower() == "paris": #(writing the answer for the question without mattering if its in lower or upper case)
    print("The answer is correct") #(if the answer is correct then show'the answer is correct')
else:
     print("The answer is wrong") #(if the answer is wrong then show ' the answer is wrong)


# 2) Multiple Questions: Extend the program into a quiz that asks for the capitals of 10 European countries.
#  Provide feedback for each question.

#Writing the 1st question to the variable (modification to the upper and the lower case)
Answer = input("What is the capital of Albania?:")
if Answer.strip().lower() == "tirana":
    print("The answer is correct") #(if the answer is correct then it show this)
else:
     print("The answer is wrong") #(if the answer is wrong then it show this)

#Writing the 2nd question to the variable 
Answer = input("What is the capital of Belarus?:")
if Answer.strip().lower() == "minsk": 
     print("The answer is correct") 
else:
    print("The answer is wrong") 

#Writing the 3rd question to the variable 
Answer = input("What is the capital of Bosnia and Herzegovina?:") 
if Answer.strip().lower() == "sarajevo": 
     print("The answer is correct") 
else:
    print("The answer is wrong") 

#Writing the 4th question to the variable 
Answer = input("What is the capital of Croatia?:") 
if Answer.strip().lower() == "zagreb": 
     print("The answer is correct") 
else:
    print("The answer is wrong") 

#Writing the 5th question to the variable 
Answer = input("What is the capital of Bulgaria?:") 
if Answer.strip().lower() == "sofia": 
     print("The answer is correct") 
else:
    print("The answer is wrong") 

#Writing the 6th question to the variable 
Answer = input("What is the capital of Czech Republic?:") 
if Answer.strip().lower() == "prague": 
     print("The answer is correct") 
else:
    print("The answer is wrong") 

#Writing the 7th question to the variable 
Answer = input("What is the capital of Estonia?:") 
if Answer.strip().lower() == "tallinn": 
     print("The answer is correct") 
else:
    print("The answer is wrong") 

#Writing the 8th question to the variable 
Answer = input("What is the capital of Georgia?:") 
if Answer.strip().lower() == "tbilisi": 
     print("The answer is correct") 
else:
    print("The answer is wrong") 

#Writing the 9th question to the variable 
Answer = input("What is the capital of Hungary?:") 
if Answer.strip().lower() == "budapest": 
     print("The answer is correct") 
else:
    print("The answer is wrong") 

#Writing the 10th question to the variable 
Answer = input("What is the capital of Iceland?:") 
if Answer.strip().lower() == "reykjavik": 
     print("The answer is correct") 
else:
    print("The answer is wrong") 