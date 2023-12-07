#Data types
#Strings 
#Integers
#Float
#Boolean

#Data Types
#String
print("Hello"[0])
print("Hello"[4])
print("123" + "456")  # will concatenate because the py will see it as a STRING

#In order to do the math operations/numbers
#Integer - whole number - no decimals
print(123 + 456)  # no quotes = means no string

#Large integers like millions: 123_456_678 will be written with underscore

#float: decimal numbers -> 3.09
#Boolean -> True/False (NO QUOTES "", WITH "" will be counted as a STRING)

#TypeError
num_char = len(input("What's your name?\n"))
print(num_char) #result 4
# print("Your name has " + num_char + " characters.")#will be TypeError: can only concatenate str (not "int") to str
#cause "Your name has " => str, num_char => int

#TypeChecking
a = 123
print(type(a))

a = float(123)
print(type(a))


#TypeConversion
new_num_char = str(num_char)
print("Your name has " + new_num_char + " characters.")

#ex:
print(70 + float("105.5")) #result 175.5
print(str(70) + str(100)) #result 70100
