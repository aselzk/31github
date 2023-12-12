#control flow with 
#if
#else
#and Conditional Operations
if condition:
    do this
else:
    do this

#ex
water_level = 50
if water_level > 80:
    print("Drain water")
else:
    print("Continue")

#ex replit
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height < 120:
  print("Sorry, you can't ride the rollercoaster :(")
else: 
  print("Have a safe trip!")

#Comparison Operators
# > greater than
# < less than
# >= greater than or equal to
# <= less than or equal to
# == equal to
# != not equal to

# Which number do you want to check?
number = int(input())
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

if number % 2 == 0:
    print("Number is even.")
else:
    print("Number is odd.")
    
