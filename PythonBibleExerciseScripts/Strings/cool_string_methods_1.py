# String Methods Part 1

# To print the number of occurances of a particular character in a string
print("Hello".count("e"))
# It's case sensitive
print("Hello".count("h"))
# It takes in multiple strings as an input
print("Hello".count("ll"))

text = "Happy Birthday"
print(text.count("a"))
print(text.count("day"))

x = "Happy Birthday"
print(x)
# Both the below functions won't modify the strings as strings are 
# immutable but they can be overwritten in a variable
# To lowercase
print(x.lower())
# To uppercase
print(x.upper())
x = x.upper()
print(x)
# It will capitalize just the first letter of the string
print(x.capitalize())
# It will capitalize just the first letter of every word
print(x.title())
x = x.title()
# To check if x is lowercase
print(x.islower())
# To check if x is uppercase
print(x.isupper())
# To check if x is title case
print(x.istitle())

# isalpha will check if the string only contains letters
# i.e. no numbers, spaces or special characters

print(x.isalpha())

y = "123"
z = "Hello112"
w = "heja%$"
u = "hello"
print(y.isalpha())
print(z.isalpha())
print(w.isalpha())
print(u.isalpha())

# isdigit checks if the string contains only numbers and nothing else
print(y.isdigit())
print(z.isdigit())

# isalnum checks if the string contains only alphanumeric characters
# and no spaces or special characters
print(x.isalnum())
print(y.isalnum())
print(z.isalnum())
print(w.isalnum())
print(u.isalnum())