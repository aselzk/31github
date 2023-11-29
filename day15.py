#Arguments
#adding argument in order to get the input value to be multiplied/modified
#should return the users input_number multiplied into the specific number
def input_number(num):
    return int(input("Enter a number: ")) * num

input1 = input_number(10)
print(input1)

#Function can have multiple Parameters(arguments), that are separated by comma (,)
#Position of the values are matter -> num1=10, num2=20
def input_number(num1, num2):
    return int(input("Enter a number: ")) * num1-num2

input1 = input_number(10,20)
print(input1)

#also we can pass named parameters
def input_number(num3, num4):
    return int(input("Enter a number: ")) * num3-num4

input1 = input_number(num3=10, num4=20)
print(input1)

#also can be set default parameters
# in this case user not required to pass the number -> will get the default parameter
def input_number(num=10):
    return int(input("Enter a number: ")) * num

input1 = input_number()
print(input1)

#but if we would pass even though default value is set -> then the python will get the user's value
def input_number(num=10):
    return int(input("Enter a number: "))

input1 = input_number(5)
print(input1)

