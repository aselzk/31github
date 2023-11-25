#Itirating Lists
#for loop function to loop over lists

#to calculate average - total amount combined and devided by the length of the lists
ages=[56, 72, 24, 46]
total = 0 
for age in ages:
    total += age
average = total / len(ages)
print(average)

#quiz
for letter in 'KodeKloud':
    if letter == 'e':
        continue #skip
    print('Letter : ' + letter)

sum = 0
values = [2,9,1,7]
for number in values:
    sum += number
print(sum)

for x in [0, 2, 1, 3]:
    for y in [0, 4, 1, 2]:
            print('*')

for x in [0, 1, 1, 3]:
    for y in [0, 2, 1, 2]:
            print('*')



#Understanding Lists
#Difference between Lists and the Variables
name = "Lydia"
ages = [56, 72, 24, 46]
ages2 = ages #we just copy values from ages
ages[0] = 92 #whenever we change the value in the elements of ages lists
#the same changes will be in ages2 list
print(ages2[0])


#quiz
list1 = [1, 2, 3, 4]
for index, j in enumerate(list1):
     print(index, j)

list1 = [[1,2,3,2,5],[4,5,6,7],[8,9,10]]
for i in list1:
      if len(i)==4:
        print(i)


list1 = [10, 11, 12, 13, 14]
print(list1[::1]) #So:
#[start::] will return the list starting from 'start' until the last element
#[:end:] will return all from the first element until the one preceding 'end'
#[0:-3] will return elements starting from the first one until (but not including) the third to last
#[::2] will return every second element of the list
#[::-3] will return every third element counting backwards


letters = ["A", "B", "C", "D", "E"]
print(letters[1:])


#Slicing Lists
#list[:end:] will return all from the first element until the one preceding 'end'

letters = ["A", "B", "C", "D", "E"]
firstTwo = letters[0:2]
print(firstTwo)

letters = ["A", "B", "C", "D", "E"]
print(letters[1:])

letters = ["A", "B", "C", "D", "E"]
print(letters[1:-1])#first and the last element cut out

letters = ["A", "B", "C", "D", "E"]
print(letters[:])#no indexes - will be copied


#del keyword for slicing the list 
#to modify original array, however without del (just using slicing) won't change the original array (just the previously modified)
letters = ["A", "B", "C", "D", "E"]
del letters[1:3]

letters = ["A", "B", "C", "D", "E"]
del letters[:]#no indexes to delete the whole list

#quiz
list1 = [1, 66, "python", [11, 55, "cat"], [ ], 2.22, True]
print(list1.upper())
