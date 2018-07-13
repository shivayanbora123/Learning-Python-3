# Dictionary in python is same as a Java map. 
# Works with a key value pair
# Downs't have any order. In order to access the elements,
# we have to use keys
students = {}
students = {"Alice":25,"Bob":27,"Claire":17,"Dan":21,"Emma":22}
print(students)
print(students["Dan"])

students["Fred"] = 25
print(students)
print(students["Fred"])

students["Alice"] = 26
print(students)
print(students["Alice"])

del students["Fred"]
print(students)

# This will output a new type called dict_keys which is
# iterable but not indexable
print(students.keys())

# To output values
print(students.values())

# To output items (List of tuples)
print(students.items())

# Converting the keys into a list
a = list(students.keys())