#Loops
#While - to execute code as long as the condition is true, means code can be run repeatedly
secret_number = 3
guess = int(input("Guess a number: "))
while guess != secret_number:
    guess = int(input("Guess a number: "))
else:
    print("Congratulations, you got it!")

#quiz:
i = 1
x = 3
sum = 0
while ( i <= x ):
 sum += i
 i += 1
print(sum)

#1<=3
#i = 0+1
#i = 1+1
#i = 1+2
#sum 1+2+3

i = 5
while True:
    if i % 0o11 == 0:
        break # If the condition in the if statement is true (if i is divisible evenly by 9), the break statement is executed, which exits the loop.
    print(i)
    i += 1

i = 2
while True:
    if i%3 == 0:
        break
    print(i)
    i += 2

x = 0
while (x < 50):
  x+=2
print(x)

i = 1
while True:
    if i % 0o7 == 0:
        break
    print(i)
    i += 1

#Loop: for/in -> to execute code for each item in sequence
# Range function:
# Break= the break statement is executed, which exits the loop.
# Continue=to skip, will go to the next value
