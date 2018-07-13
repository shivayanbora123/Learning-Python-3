# Strings are an iterable datatype i.e. you can go
# step by step along it until you get to the end and
# each of the steps is called an element. Each element
# has an index starting at 0
word = "supercalifragilisticexpialidocious"
print(word[0]) # Original data is unchanged as strings are immutable
print(word[2])

# Slicing
# variable[start:end:step]
print(word[0:5:1]) # Excludes the 5th index and will take upto 4th index
print(word[0:5:2]) # Excludes the 5th index and will take upto 4th index
print(word[5:9:1])

print(word[5:]) # From 5th index to the end of string
print(word[5::2]) # From 5th index to the end of string in steps of two

print(word[:7]) # From start upto index 6th

print(word[::-1]) # From the end to the start in steps of -1 i.e. reverse a string

# If we want to count from backwards, the index of the last element is -1 and second last is -2 etc.
print(word[-2])

# We can use index function to get the index which will return the starting of
# the first instance of the string
print(word.index("cali"))
print(word.index("fragi"))

print(word[word.index("cali"):word.index("fragi")])

print(word[word.index("docious"):])

print(word[word.index("fragilistic"):word.index("exp")])