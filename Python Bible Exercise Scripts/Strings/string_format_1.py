# Old Formatting of Python Strings

# You can use %s to inject strings into your print statements. 
# The modulo % is referred to as a "string formatting operator".
print("I'm going to inject %s here." %'something')

# You can pass multiple items by placing them inside a tuple after the % operator.
print("I'm going to inject %s text here, and %s text here." %('some','more'))

# It should be noted that two methods %s and %r convert any python object 
# to a string using two separate methods: str() and repr().
# %r and repr() deliver the string representation of the object, 
# including quotation marks and any escape characters.
print('He said his name was %s.' %'Fred')
print('He said his name was %r.' %'Fred')

# The %s operator converts whatever it sees into a string, including integers and floats. 
# The %d operator converts numbers to integers first, without rounding.
print('I wrote %s programs today.' %3.75)
print('I wrote %d programs today.' %3.75)

# Floating point numbers use the format %5.2f. 
# Here, 5 would be the minimum number of characters the string should contain; 
# these may be padded with whitespace if the entire number does not have this many digits. 
# Next to this, .2f stands for how many numbers to show past the decimal point. 

print('Floating point numbers: %5.2f' %(13.144))
# Output: Floating point numbers: 13.14

print('Floating point numbers: %1.0f' %(13.144))
# Output: Floating point numbers: 13

print('Floating point numbers: %1.5f' %(13.144))
# Output: Floating point numbers: 13.14400

print('Floating point numbers: %10.2f' %(13.144))
# Output: Floating point numbers:      13.14

print('Floating point numbers: %25.2f' %(13.144))
# Output: Floating point numbers:                     13.14

# Nothing prohibits using more than one conversion tool in the same print statement:
print('First: %s, Second: %5.2f, Third: %r' %('hi!',3.1415,'bye!'))
# Output: First: hi!, Second:  3.14, Third: 'bye!'