# --------------------------------------------------------
#        Name: <Ashley Jagai, Heejae Yoon>
# Course Info: CSC111 - Fall 2021
# Description: Submission for Assignment 1
#        Date: <09/21/21>
# --------------------------------------------------------

# INSTRUCTIONS (you may delete these comments if you like)
# In this assignment, you will write a short python program 
# that simulates basic calculator functionality. 

# The user interface of your calculator should ask the user 
# to input two numbers, and then a string indicating which 
# mathematical operation to perform. For example:

#    Enter the first number: 5
#    Enter the second number: 10
#    Enter the operation (+, -, *, /, or **): *
#    The answer is: 50

# Your calculator should support add, subtract, multiply, 
# divide and power (exponentiation) operations. If you choose, 
# you may also support integer division with a remainder.

# Your calculator should be able to handle both integers 
# and floats.

# print("Your code goes instead of this print")
# Assignment01 Solution
num_1 = eval(input("Enter the first number:"))
num_2 = eval(input("Enter the second number:"))
operation = str(input("Enter the operation (+, -, *, /, or **):"))

if operation == "+":
    print ("The answer is:", (num_1 + num_2))
elif operation == "-":
    print ("The answer is:", (num_1 - num_2))
elif operation == "*":
    print ("The answer is:", (num_1 * num_2))
elif operation == "/":
    print ("The answer is:", round((num_1 / num_2),3))
elif operation == "**":
    print ("The answer is:", (num_1 ** num_2))
else:    
   print("This is an invalid input") 
