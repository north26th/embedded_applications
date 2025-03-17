#Week 5 Homework - Embedded Applications
#Author: Ryan Page
#Date: 11/03/2025

#1.	Write a program to prompt for a file name,
#Read through the file line-by-line

#I wanted to use the skills I got from the weekly content
#I use a write function to generate a new file called text.txt
#2 lines are added as "L" and "R"
#They are written in, then stripped out via the below code.

f = open("test.txt", "w")
L = ["This is my homework test" "\n"]
R = ["This is line 2 of homework test" "\n"]
f.writelines(L)
f.writelines(R)
f.close()

while True:
    file_name = input("Enter the file name you want to read: ")
    try:
        with open(file_name, 'r') as file:
            for lines in file:
                print(lines.strip())  # Remove extra whitespace
        break  # Exit the loop once the file is successfully read
    except FileNotFoundError:
        print("File not found. Please check the file name and try again.")
    except Exception as e:
        print(f"An error occurred: {e}")
        break  # Exit loop on unexpected error
