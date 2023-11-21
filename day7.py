#Operators
age1 = 24
age2 = 16
# if (both ages are higher than 18):
#     print("You are both adults")
# elif(One age is higher than 18):
#     print("One of you is an adult")
# else:
#     print("You are both children")

if (age1>=18 and age2>=18):
    print("You are both adults")
elif(age1>=18 or age2>=18):
    print("One of you is an adult")
else:
    print("You are both children")

#Boolean value: AND value
#True and True -> True
#True and False -> False
#False and True -> False
#False and False -> False

#Boolean value: OR value
#True or True -> True
#True or False -> True
#False or True -> True
#False or False -> False

is_hungry = False
if(not is_hungry):
    print("You are not hungry")

#Boolean value: NOT value
#not True -> False
#not False -> True

x = 6
y = 7
print(x == y)
