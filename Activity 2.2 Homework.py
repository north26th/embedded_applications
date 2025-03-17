#Week 5 Homework - Embedded Applications
#Author: Ryan Page
#Date: 12/03/2025
#Activity 2.2
#Create a file called Homework.txt. First add a new line to the file:” This is a Homework, Activity 2, Question 3”
#Print the content of Homework.txt.


#Opening a file - note - will create a new file if not present

file = open("Homework.txt", "w")
L = ["This is Homework, Activity 2, Question 3"]
file.write("Hello \n")
file.writelines(L)
file.close()

#open the file for reading
file = open("Homework.txt", "r")
print("The contents of 'Homework.txt' is : \n")
print(file.read())
print



