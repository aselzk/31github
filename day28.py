# # #Nested if/else
# # if condition:
# #     if another condition:
# #         do this
# #     else:
# #         do this
# # else:
# #     do this


# #ex:
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
# if height >= 120:
#     print("Have a safe trip!")
#     age = int(input("What's your age?"))
#     if age <= 18:
#         print("Please pay 7$.")
#     else:
#         print("Please payy 12$")
# else: 
#     print("Sorry, you can't ride the rollercoaster :(")



# # # IF/ELIF/ELSE
# # if condition1: # is true do A 
# #     do A
# # elif condition2: # cond1 is not true -> do B
# #     do B
# # else:
# #     do this # if none of the above is not true than do this
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
# if height >= 120:
#     print("Have a safe trip!")
#     age = int(input("What's your age?"))
#     if age <= 12:
#         print("Please pay 5$.")
#     elif age <= 18:
#         print("Please pay 7$.")
#     #we can do as much elif conditions as we want
#     else:
#         print("Please payy 12$")
# else: 
#     print("Sorry, you can't ride the rollercoaster :(")



#ex
# Enter your height in meters e.g., 1.55
height = float(input("what's you height?"))
# Enter your weight in kilograms e.g., 72
weight = int(input("what's your weight?"))
bmi = (int(weight / (height * height)))
print(bmi)

if bmi <=18.5:
    print(f"Your bmi is {bmi}, you are underweighted.")
elif bmi >18.5:
    print(f"Your bmi is {bmi}, you are normal weight.")
elif bmi >=25:
    print(f"Your bmi is {bmi}, you are slightly overweighted.")
elif bmi >=30:
    print(f"Your bmi is {bmi}, you are overweighted.")
else:
    print(f"Your bmi is {bmi}, you are clinically overweighted.")
