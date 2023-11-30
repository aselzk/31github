#Return Function
#to return function's result back to caller
#there are cases when we want to print early - before the function


#with printing - some Actions are happening
def print_sum(num1, num2):
    sum = num1 + num2
    print("The sum is: ", str(sum))
print_sum = print_sum(1, 1)

#with Return Statement python won't reach till the print sum function and return as nothing
def print_sum(num1, num2):
    sum = num1 + num2
    return
    print("The sum is: ", str(sum))


#lets say we don't want print if the sum=0
def print_sum(num1, num2):
    sum = num1 + num2
    if(sum == 0):
        return
    print("The sum is: ", str(sum))
print_sum(15, 10)


def print_sum(num1, num2):
    sum = num1 + num2
    if(sum == 0):
        return
    print("The sum is: ", str(sum))
print_sum(-1, 1)

#If we want return if the num is even, but if not will be printed NONE
def is_even(num):
    if(num % 2 == 0):
        return True
print(is_even(6))

def is_even(num):
    if(num % 2 == 0):
        return True
print(is_even(9))

#quiz
def is_true(a):
    return bool(a)

result = is_true(6<3)
print("The result is", result)

def add(x, y):
    return x+y
