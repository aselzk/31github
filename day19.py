#Function - Arguments
age = 22
def multiply(num):
    num *= 2
    print("In multiply:", str(num))
    multiply(age) #here we've created another variable - that's num => 22*2=44
print(age) #but the original age var => 22

#howeverl if we have lists in variable 
nums = [1, 2, 3]
def change_first_item(list):
    list[0]=9
    change_first_item(nums)
    print(nums)

def my_function(*ages):
    print("The older friend is " + ages[0] + "years")
my_function("13", "12", "11")
