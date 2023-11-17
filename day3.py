#Variables
#can be upper/lower case
#can not be Python preserved words, like: if/elif/import/del
#need to change the case of preserved words to: If/Elif/Import/Del
amount_of_apples = 2
cost_of_apple = 5
print(amount_of_apples * cost_of_apple)

#variables can be reassigned
cost_of_apple = cost_of_apple + 2
amount_of_apples = 2
print(amount_of_apples * cost_of_apple)

#Shortcut operator to cost_of_apple = cost_of_apple + 2
#Shortcut operator can be used to all other operators as well
cost_of_apple = 5
cost_of_apple += 2
amount_of_apples = 2
print(amount_of_apples * cost_of_apple)

#Quiz
amount = 4
cost = 2
cost += 2
print(amount * cost)

y = 5
y = "Jack"
print(y)

age = 22
AGE = 44
age /= 2
print(age + AGE)
