# New Formatting of Python Strings

A = "Part one"
B = "Part two"

# String concatenation
print(A + B)

# Contents of A printed three times in succession
print(A * 3)

C = 1
# If we do A + C, python will throw an error saying
# it can't convert 'int' object to 'str' implicitly
# as String and Integers are incompatible data types

# str(C) will convert the Integer into String
print(A + str(C))

# The format function will replace the curly braces 
# with the variables in it's arguments as shown below
# sequentially and if the variables contain data from
# another data type, it will implicitly convert it into
# string
print("{} - {}".format(A,C))
# The number inside the curled braces implies which argument
# to take in case there are multiple variables and we need to 
# modify the order
print("{1} - {0}".format(A,C))

# The .format() method has several advantages over the %s placeholder method:

# 1. Inserted objects can be called by index position:
print('The {2} {1} {0}'.format('fox','brown','quick'))
# Output: The quick brown fox

# 2. Inserted objects can be assigned keywords:
print('First Object: {a}, Second Object: {b}, Third Object: {c}'.format(a=1,b='Two',c=12.3))
# Output: First Object: 1, Second Object: Two, Third Object: 12.3

#3. Inserted objects can be reused, avoiding duplication:
print('A %s saved is a %s earned.' %('penny','penny'))
# vs.
print('A {p} saved is a {p} earned.'.format(p='penny'))
# Output1: A penny saved is a penny earned.
# Output2: A penny saved is a penny earned.

# Alignment, padding and precision with .format()
# Within the curly braces you can assign field lengths, left/right alignments, rounding parameters and more


print('{0:8} | {1:9}'.format('Fruit', 'Quantity'))
print('{0:8} | {1:9}'.format('Apples', 3.))
print('{0:8} | {1:9}'.format('Oranges', 10))
# Output: Fruit    | Quantity 
#         Apples   |       3.0
#         Oranges  |        10

# By default, .format() aligns text to the left, numbers to the right. 
# You can pass an optional <,^, or > to set a left, center or right alignment:
print('{0:<8} | {1:^8} | {2:>8}'.format('Left','Center','Right'))
print('{0:<8} | {1:^8} | {2:>8}'.format(11,22,33))
# Output: Left     |  Center  |    Right
#         11       |    22    |       33

# You can precede the aligment operator with a padding character
print('{0:=<8} | {1:-^8} | {2:.>8}'.format('Left','Center','Right'))
print('{0:=<8} | {1:-^8} | {2:.>8}'.format(11,22,33))
# Output: Left==== | -Center- | ...Right
#         11====== | ---22--- | ......33

# Field widths and float precision are handled in a way similar to placeholders. 
# The following two print statements are equivalent:
print('This is my ten-character, two-decimal number:%10.2f' %13.579)
print('This is my ten-character, two-decimal number:{0:10.2f}'.format(13.579))
# Output: This is my ten-character, two-decimal number:     13.58
# Output: This is my ten-character, two-decimal number:     13.58
# Note that there are 5 spaces following the colon, and 5 characters taken up by 13.58, 
# for a total of ten characters.

# For more information on the string .format() method visit: 
# https://docs.python.org/3/library/string.html#formatstrings