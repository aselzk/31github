#Scopes
#Variables that are declared within the function body - are available only to that function (not global)
# def input_numbers():
#     result = int(input("Enter a number: ")) * 100
#     return result
# print(result) #(result variable is within the function, so this print will throw an error)


#Variables type:
#LEGB
#Local - var within function
#Enclosing - var are in local scope of enclosing functions
#Global - var defined on top level
#Built-in - names that are pre-assigned



#However we can declare variable outside of the function body
num = 100 #variable outside the function
def input_numbers():
    result = int(input("Enter a number: ")) * 100
    return result
    num = 50 #if we declare variable inside the function scope - python will get the var that is inside
             #if we didn't have this variable inside the scope - python will look to the global scope


#If we want within the function variable to be accessible and be global - need to add global function
num = 100 #variable outside the function
def input_numbers():
    global own_num
    own_num = 50
    result = int(input("Enter a number: ")) * own_num
    return result
     

#quiz
x=30
def my_function():
    global x
    x = 20
my_function()
print(x) #20

def my_function():
    x=20
    def my_inner_function():
        print(x)
    my_inner_function()
my_function() #20


def my_function():
    def my_inner_function():
        x=20
    print(x)
    my_inner_function()
my_function() #error



x=20
def my_function():
    print(x,end=' ') #means space and the numb x

my_function()
print(x,end=' ') #20 20

def my_function():
    a = 20
myfunc()
print(a) #error, cause var inside the scope

def my_function():
    def my_inner_function():
    x=20
    print(x)
    my_inner_function()
my_function()
