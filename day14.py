#Functions
#   1.python functions
#   2.module functions
#   3.own functions

#Own functions
#Ex.: when we want repeat some code - we can create own function

input1 = int(input("Enter a number: "))
input2 = int(input("Enter a number: "))
input3 = int(input("Enter a number: "))
input4 = int(input("Enter a number: "))
input5 = int(input("Enter a number: "))

#instead this repeated code:
#def built in function
#function body: return int(input("Enter a number: "))
#return: tells to return a certain value
def input_number():
    return int(input("Enter a number: "))

