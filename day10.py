#Lists Methods - to change data and lists
#the difference btw Functions and Methods
#Functions - can work on its own 
#Methods - to make a change to data
#    list.append() - to add item into the end of the list
#    list.insert() - to add item into the btw of the list

countries = ["KG", "Canada", "USA"]
countries.append("Spain")
countries.insert(2, "Italy") #italy index is 2, one shift to the right
print (countries)


#in order to swap places
#can be done by creating variables into temp
countries = ["KG", "Canada", "USA"]
temp = countries[0] 
countries[0] = countries[1]
countries[1] = temp
print (countries)

#also swap can be done in one line
countries[0], countries[1] = countries[1], countries[0]

#Methods
#   list.sort[] - sort the value descendingly - from the lowest to the highest
#   list.reverse - the first item becomes the last item, the last becomes the first

ages = [56, 72, 24, 46]
ages.sort()
print (ages)

ages.reverse()
print (ages)

#quiz
list1=["Go","Java","C","Rust"]
print(min(list1))

list1=["Go","Java","C","Python"]
print(max(list1))

#pop() returns and removes the last value from the list 
list1 = [4, 4, 3, 1]
list1.pop(2)
print(list1)

#with insert method, we can insert a new item in between values so item 8 will be inserted into index 1
list1=['UK','India','Canada']
list1.insert(1,8)
print(list1)
