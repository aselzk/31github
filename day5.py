#conditional statements
#if condition whether the code should be run or not
age = int(input("How old are you?"))
if age >=18:
    print("You are an adult!")

#else condition - when we have false statement
else:
    print("The condition is false!")

#elif to add another condition
#elif:
    print("Only the second condition is true!")

if age >= 18:
    if age == 18:
        print("You are exactly 18 years old!")
    else:
        print("You are older than 18 years old!")

#Quiz:
x = 0
a = 6
b = 6
if a > 0:
    if b < 0: 
        x = x + 6 
    elif a > 6:
        x = x + 5
    else:
        x = x + 4
else:
    x = x + 3

print(x)
