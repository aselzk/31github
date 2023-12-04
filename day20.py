#Tuples
#immutable data - data that can't be changed
#data in tuples can be written in Paranthesis
tuple1 = (1, 2, 3)
print(tuple1)

#modifying the list is not available, for ex: with append
# tuple1.append(4) # will throw error

#within the tuple it can be any data: numbers, integers, strings
# tuple1 = (1, "Lydia", age, (1,2))

#tuple can have only 1 element, but needs to be followed with (,)
# tuple1 = (1,)

#Dictionaries
#consist keys and values
#for ex: in usernames
usernames = {
    "lydia":"lydiahallie",
    "sarah":"sarah123",
    "max":"max123"
}

print(usernames["sarah"])

#can use built-in methods in dictionaries in order to easier to get the contents
# dictionary.keys()
# dictionary.values()
# dictionary.items()

print(usernames.keys())

#Dictionary with for loop
for key in usernames.keys():
    print(key + "-" + usernames[key])

print(usernames.values()) #exact the same as keys method

print(usernames.items()) #returns tuples with the key-value pair

#to Update - we can edit the existing data in variables (usernames)
#also, there is UPDATE method
usernames.update({"chloe":"chloe123"})
print(usernames)

#to Delete 
del usernames["max"]
print(usernames)

#to Delete ALL data
usernames.clear()
print(usernames)

#to Delete last item in data
usernames.popitem()
print(usernames)

#to Copy item in data
usernames.popitem()
print(usernames)
