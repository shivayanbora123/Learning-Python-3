# String Methods Part 2

# index will give the starting index of the character or the sequence of characters
x = "happy birthday"
print(x.index("birthday"))
# Will give an error saying: ValueError: substring not found
# print(x.index("birthdey"))

# find works similar to index but if the substring is not found,
# instead of giving an error, it will return -1
print(x.find("birthday"))
print(x.find("birthdey"))

# Both index and find are case sensitive

# strip will remove what ever sequence of characters that is specified in the arguments
# from both sides of the input string
y = "000000HappyBirthday000000"
print(y.strip("0"))
# Will strip away spaces from both sides of the string
print(y.strip())
# Will strip 0's from the left hand side of y
print(y.lstrip("0"))
# Will strip 0's from the right hand side of y
print(y.rstrip("0"))

name = "Shivayan "
# Will display the length of the string
print(len(name))
print(name)
print(name.strip())
# Won't strip anything
print(name.strip(""))
# Will strip away space from both sides of the string
print(name.strip(" "))
print(len(name.strip()))

# Weird behavior of strip() need to check
#print(y.strip("011H1asd213d10"))


# String split
s = "Hello World concatenate me!"
# Split a string by blank space (this is the default)
print(s.split())
# Split by a specific element (doesn't include the element that was split on)
print(s.split('W'))