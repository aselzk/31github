#Lists
countries = ["KG", "Canada", "USA"]
print(countries[0])
print(countries[1])
print(countries[2])

#to change the value in the 1st index
countries[0] = "UK"
print(countries[0])

#to know the length of the lists
countries = ["KG", "Canada", "USA","UK"]
print(len(countries))

#to delete items in the list
countries = ["KG", "Canada", "USA","UK"]
del countries[1]
print (countries)

#to reverse the list
list1=[2,5,3,1]
list1[::-1]

#quiz
list1 = [10, 11, 12, 13, 14]
print(list1[::3])
