# Formatted String Literals (f-strings)

# Introduced in Python 3.6, f-strings offer several benefits over the older .format() string method 
# described above. For one, you can bring outside variables immediately into to the string rather 
# than pass them as arguments through .format(var).

name = 'Fred'
print(f"He said his name is {name}.")
# Output: He said his name is Fred.

# Pass !r to get the string representation:
print(f"He said his name is {name!r}")
# Output: He said his name is 'Fred'

# Float formatting follows "result: {value:{width}.{precision}}"
# Where with the .format() method you might see {value:10.4f}, 
# with f-strings this can become {value:{10}.{6}}
num = 23.45678
print("My 10 character, four decimal number is:{0:10.4f}".format(num))
print(f"My 10 character, four decimal number is:{num:{10}.{6}}")
# Output: My 10 character, four decimal number is:   23.4568
# Output: My 10 character, four decimal number is:   23.4568
# Note that with f-strings, precision refers to the total number of digits, 
# not just those following the decimal. 
# This fits more closely with scientific notation and statistical analysis. 
# Unfortunately, f-strings do not pad to the right of the decimal, even if precision allows it:


num = 23.45
print("My 10 character, four decimal number is:{0:10.4f}".format(num))
print(f"My 10 character, four decimal number is:{num:{10}.{6}}")
# Output: My 10 character, four decimal number is:   23.4500
# Output: My 10 character, four decimal number is:     23.45

# If this becomes important, you can always use .format() method syntax inside an f-string:
num = 23.45
print("My 10 character, four decimal number is:{0:10.4f}".format(num))
print(f"My 10 character, four decimal number is:{num:10.4f}")
# Output: My 10 character, four decimal number is:   23.4500
# Output: My 10 character, four decimal number is:   23.4500
# For more info on formatted string literals visit:
# https://docs.python.org/3/reference/lexical_analysis.html#f-strings