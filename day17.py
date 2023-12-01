#List as Argument
#we can pass List to the function as well
def multiply_values(list):
    multiplied_values = []

    for item in list:
        multiplied_values.append(item * 2)
    return multiplied_values
print(multiply_values([1, 2, 3]))
print(multiply_values([-4, -5, -6]))


def my_functions(names):
    for i in names:
        print(i, end=' ')
names = ["john", "mark", "emmy"]
my_functions(names)


def mean_func(list1):
    return sum(list1) / len(list1)
print(mean_func ([5, 6, 7, 8]))


def get_odd_func(numbers):
    odd_numbers = [num for num in numbers if num % 2]
    return odd_numbers
print(get_odd_func([7, 4, 5, 6, 9, 8, 12]))


def double_list(numbers):
    return 2 * numbers
numbers = [1, 2, 3]
print(double_list(numbers))


def my_function(numbers):
    for i in numbers:
        print(i*2+10, end='')
numbers = [1, 2, 3]
my_function(numbers)


def get_odd_func(numbers):
    odd_numbers = [num for num in numbers if num % 2]
    return odd_numbers
print(get_odd_func([1, 2, 3, 4, 5, 6]))
