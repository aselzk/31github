#Errors
#when python execute the code and smth goes wrong
#Python raises an Exceptions
#that means - Exception stops the program and creates a special type of data
#if Exception has been raised - the Exception expects smth to take care of it
#however if there is nothing to take care of it -> Will throw Error Message -> <<NameError: name 'naem' is not defined>>

# name = 'Lydia'
# print('My name is'+ naem)
# print('All done!')


#but if the exception has been resolved the program will be resumed and execution will continue
#Exception can be handled with TRY and EXCEPT
try:
    name = 'Lydia'
    print('My name is'+naem)
except:
    print('Something went wrong')
print('All done!')


#Exceptions can be used when Specific Error was given
#example:
# x = int(input("Enter a number: "))
# y = 1/x
# print(y)

# print("All done!")

#in this example user can put as an input string or put 0 (that also will throw an error)
# the same example with Exception
try:
    x = int(input("Enter a number: "))
    y = 1/x
    print(y)
except ZeroDivisionError:
    print("You cannot divide by zero.")
except ValueError: #if value is a String 
    print("Please enter an integer.")
except:
    print("Something else went wrong")
print("All done!")

#Hierarchy Exceptions
#orders of the exceptions matters
#need to look for Python common errors-to ensure to trobleshoot correctly

try:
    x = int(input("Enter a number: "))
    y = 1/x
    print(y)
except ArithmeticError: #ZeroDivisionError is in ArithmeticError by hierarchy
    print("Calculation failed.")
except ValueError: #if value is a String 
    print("Please enter an integer.")
except:
    print("Something else went wrong")
print("All done!")
