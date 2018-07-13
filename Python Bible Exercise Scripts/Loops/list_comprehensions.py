# List comprehension is basically a shortcut method or a bit of 
# shorthand to combine variables, for loops and if statements to 
# create a list or to comprehend a listin all one line of code.

# Creating a list of all even numbers in the range of 1 to 101
even_numbers = [x for x in range(1,101) if x%2 == 0]
print(even_numbers)

# Creating a list of all odd numbers in the range of 1 to 101
odd_numbers = [x for x in range(1,101) if x%2 != 0]
print(odd_numbers)

words = ["the","quick","brown","fox","jumps","over","the","lazy","dog"]
answer = [[w.upper(),w.lower(),len(w)] for w in words]
print(answer)