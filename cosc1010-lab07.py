# Nelia Koontz
# UWYO COSC 1010
# 10/30/24
# Lab 07
# Lab Section: 15 
# Sources, people worked with, help given to: 
# https://virtualnerd.com/act-math/advanced-arithmetic/probability-counting/factorial-definition
# https://www.google.com/search?client=firefox-b-1-d&q=python+multiply+numbers+in+list#fpstate=ive&vld=cid:9fedbf63,vid:xuU2w7n_2mc,st:0
# https://www.w3schools.com/python/ref_string_replace.asp
# https://www.w3schools.com/python/ref_string_split.asp
# python crash course book
# I had a very difficult time getting the last program to recognize an integer. In the end, 
# I had messed up the spacing

# Prompt the user for an upper bound
print("This program will give a factorial of an upper bound.")
prompt =("Please enter a whole number for the upper bound:")
user_input = input(prompt) 

# Write a while loop that gives the factorial of that upper bound
# This will need to be a positive number
# For this you will need to check to ensure that the user entered a number
    # To do so you can use the methods `.isdigit()` or `.isnumeric()`
    # If a user did not enter a number output a statement saying so
# You will continue to prompt the user until a proper integer value is entered
while user_input.isdigit() == False:
    print("This is not a number")
    user_input = input(prompt)

if user_input.isdigit() == True:
    num = int(user_input)

factorial = 1
fact_calc = []
if num == 0:
    print(f"The result of the factorial based on the given bound is {factorial}")
else:
    while num >= 1:
        fact_calc.append(num)
        num -= 1

for num in fact_calc:
    factorial = factorial * num

print(f"The result of the factorial based on the given bound is {factorial}")

print("*"*75)
# Create a while loop that prompts a user for input of an integer values
# Sum all inputs. When the user enters 'exit' (regardless of casing) end the loop
# Upon ending the loop print the sum
# Your program should accept both positive and negative input
# Remember all inputs from stdin are strings, so you will need to convert the string to an int first
# Before you convert the number you need to check to ensure that it is a numeric string
    # To do so you can use the methods `.isdigit()` or `.isnumeric()`
    # This will return true if every digit in your string is a numerical character
    # However, that means a string such as `-1` would return false, even though your program should accept negative values
    # This means you will need to have a check to see if `-` is first character of the string before you check if it is numerical
    # If it is in the string you will need to remove the `-` character, and know that it will be a negative number, so a subtraction from the overall sum
    # I recommend checking out: https://www.w3schools.com/python/ref_string_replace.asp to figure out how one may remove a character from a string
# All this together means you will have an intensive while loop that includes multiple if statements, likely with some nesting 
# The sum should start at 0

print("This program will sum all integers entered.\n Enter 'quit' to stop")
prompt = ("Please enter an integer:")
pos_nums = []
neg_nums = []

active = True

while active:
    user_num = input(prompt)
    user_num = user_num.lower()
    if user_num == 'quit':
        active = False
    else:
        if user_num[0] == "-": #check for "-"
            neg_num = user_num.replace("-", "0")
            if neg_num.isdigit() == True:
                neg_num = int(neg_num)
                neg_nums.append(neg_num)
            else:
                print(f"{user_num} is not a number, try again")
        if user_num.isdigit() == True:
            pos_num = int(user_num)
            pos_nums.append(pos_num)
        if user_num.isdigit() == False and user_num[0] != "-":
            print(f"{user_num} is not a number, try again")
            
num_sum = 0            
pos_add = sum(pos_nums)
neg_add = 0
for num in neg_nums:
    neg_add = neg_add +- num
num_sum = pos_add + neg_add

print(f"Your final sum is {num_sum}")

print("*"*75)
# Now you will be creating a two operand calculator
# It will support the following operators: +,-,/,*,% 
# So accepted input is of the form `operand operator operand` 
# You can assume that the user is competent and will only input strings of that form 
# You will again need to verify that the operands are numerical values
# For this assume only positive integers will be entered, no need look for negative numbers 
# You will need to check the string for which operator it contains
# Once you do, you will need to remove the operands from the string
# This can be done in multiple ways:
    # You can go through the string in a loop and create a substring of the characters until an operator is reached
        # Upon reaching the operator you will switch to another substring and add all characters following to the second new string 
    # Alternatively you can use the `.split()` method to split the string around an operator: https://www.w3schools.com/python/ref_string_split.asp
# Your program will need to work with whatever spacing is given  
    # So, it should function the same for `5 + 6` as `5+6`
# Print the result of the equation
# Again, loop through prompting the user for input until `exit` in any casing is input 
#prompt

print("This program will calcuate two numbers")
print("The following operators are valid: '+','-','/','*','%'")
print("Enter 'exit' to stop")
prompt = ("Please enter a calculation:")

op_list = ['+','-','/','*','%']
num_list = []
int_list = []
operator = []
num1 = []
num2 = []

active = True

while active:
    user_input = input(prompt)
    user_input = user_input.lower()
    if user_input == 'exit':
        active = False
    else:
        for op in op_list:
            if op in user_input:
                num_list = user_input.split(op, 1)
                operator = op
            num1 = num_list[0]
            num2 = num_list[1]
        if num1.isdigit():
            num1 = int(num1)
        else:
            print("not a number")
        if num2.isdigit():
            num2 = int(num2)
        else:
            print("not a number")
        if type(num1) == int and type(num2) == int:
            if operator == '+':
                print(num1 + num2)
            if operator == '-':
                print(num1 - num2)
            if operator == '/':
                print(num1 / num2)
            if operator == '*':
                print(num1 * num2)
            if operator == '%':
                print(num1 % num2)