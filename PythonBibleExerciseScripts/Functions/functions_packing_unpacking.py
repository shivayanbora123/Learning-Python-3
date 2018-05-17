numbers = [1,2,3,4,5]

print(1,2,3,4,5)
#  1 2 3 4 5

print(numbers)
# [1, 2, 3, 4, 5]

# Unpacking the list
print(*numbers)
#  1 2 3 4 5

print("abc")
# abc

# Both have the same output
print(*"abc")
print("a","b","c")
# a b c

# This will work for only two numbers
def add(x,y):
    return x + y

# This is going to pack whatever numbers that comes here into one tuple called numbers
def add_modified(*numbers):
    total = 0
    for number in numbers:
        total = total + number
    return total

# Positional arguments
print(add_modified(1,2,3,4,5,6,7,8,9,10))

def about(name, age, likes):
    sentence = "Meet {}! They're {} years old and they like {}".format(name,age,likes)
    return sentence

# Keyword arguments using packing. Here also, the sequence of parameters don't matter
# Key becomes the parameter and the Value becomes the argument
dictionary = {"name":"Shivayan", "age":27, "likes":"Python"}
about(**dictionary)

# When we pack down these keyword arguments, 
# we're going to produce a dictionary out of them

# **kwargs is a convention for keyword arguments
# *args is normal arguments
# This will create a dictionary name kwargs
def foo(**kwargs):
    # This will give us a set of tuples and each one is 
    # going to have a key and a value
    for key, value in kwargs.items():
        print("{}:{}".format(key, value))

foo(huda = "Female", ziyad = "Male")