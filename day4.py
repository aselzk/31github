#Comments
#Allow to add info into code
#is created by a # followed by text


#Input Function
#to input data and to accept an optional parameter that can be used in order to write a message before the user input
#Can be variable
#Always a string
#not Numeric function
age = input("How old are you?")
#the value is user's answer (Always a string)
#in order to make it numeric:
#   Type casting:
#Integers int()
#Floating point float()
print(int(age) - 10)
#A program that doesn't use any input is called: DEAF program


#Quiz:
inputString = input('Enter a string: ')
print(inputString, sep='#', end='&')

age =input("My age is: " )
print (age)

print(int(15.5)-10) #int - whole number

#String Methods
# (+) operator for strings to concatenate
print(10 + 2)

# (*) operator for strings to repeat the string
print("ha" * 10)

# no output when * to "0" or "negative number"
print("ha" * 0)
print("ha" * -1)

# in order to make numbers to string we've seen: Type casting
print(int("22"))
# to make opposite
#to return string into integers
print(str(22))

cost_of_apples = 2
amount_of_apples = input("How many apples do you want?")
total_sum = cost_of_apples * int(amount_of_apples)
print("You have to pay: " + str(total_sum))

#Quiz:
Num = input("Enter a Number: ") #(converts number to string)
print (Num * 3 ) # means the string repeats, not multiplication

inputString = input('Enter a string: ')
print(inputString*2)

Num = input("Enter a Number: ")
Num = int(Num) #(converts into whole number)
print ( Num * 3 )

year_of_birth = int(input("In what year were you born? "))
print("You were born in " + ...(year_of_birth))

print("ha"*2)

#All string methods returns new values. They do not change the original string.


#Comparison Operators
# 6 types of comparison operators:
#   1. Equal "==": checks if it equal to each other
print(2 == 2) #returns TRUE
print("Hello" == "Bye")

#   2. Not Equal "!=": exact opposite
print(2 == 2)
print("Hello" == "Bye") #returns TRUE

#   3. Greater than ">": if its greater
print(19 > 2)
print(2 > 19)

#   4. Greater than or equal to ">=": if its greater or equal
print(19 >= 2)
print(19 >= 19)

#   5. Smaller than "<": if its greater
print(19 <= 2)
print(19 <= 19)

#   6. Smaller than or equal to "<=": if its smaller or equal
print(19 <= 2)
print(19 <= 19)

#quiz:
y = 20
x = y += 3
print(x)

min_score = 13
score = 13

print(score > min_score)
print(score <= min_score)

'python'>'Python' #(true)

y = 20
x = y += 3
print(x)
