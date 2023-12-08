# #Mathematical Operations
# print(3*2)
# print(6/2) #when we check the type is float
# print(type(6/2))
# print(2**2) #Exponents

# #PEMDAS
# # ()
# # **
# # */
# # +-


#in order to change from float to integer
print(int(3*3+3/3-3))

# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
weight=72
height=1.65


#need to change the types
weight_as_int = int(weight)
height_as_int = float(height)

#calculation using operator
bmi = weight / height**2

print(int(weight / (height * height)))


#Number manipulation
#round decimals 
print(round(8 / 3)) #8/3=2.6666666

#to round two decimal places
print(round(8 / 3, 2)) #2.67

#// will directly change the float to integer
print(round(8 // 3)) #2 -> integer

#F String - Converting other types of data into String (instead of typing -> str(score))
#FSTRING very helpful when we face a Type Error. when we'res trying to concatenate a String to an Integer.
score = 0
height = 1.8
isWinning = True
print(f"your score is {score}, you height is {height}, you are winning is {isWinning}")


#Create a program using maths and f-Strings that tells us how many weeks we have left, if we live until 90 years old.
#It will take your current age as the input and output a message with our time left in this format:
#You have x weeks left
#age = input()
age = 15
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

#MY_SOLUTION
weeks_in_year = 52
weeks_in_ninety_years = 52 * 90
print(weeks_in_ninety_years)

weeks_left = int(age) * weeks_in_ninety_years

print(f"you have {weeks_left} weeks left")


#ANGELA_SOLUTION
age = input()
# Your code below this line 👇
years = 90 - int(age)
weeks = years * 52

print(f"You have {weeks} weeks left.")
