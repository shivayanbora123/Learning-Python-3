# range() function creates a range iterable in pythion 3. Im python 2 however, it creates 
# a list
print("Using range() iterable")
for number in range(1,9):
    print(number)

print("Using range() iterable in steps")
for number in range(1,50,2):
    print(number)

print("Using List")
for nums in [10,20,30,40]:
    print(nums)

print("Using Strings")
for letter in "Shivayan":
    print(letter)

# Counting the number of vowels and consonants in a word
vowels = 0
consonants = 0
for letter in "Shivayan":
    if letter.lower() in "aeiou":
        vowels += 1
    elif letter == ' ':
        # pass is similar to continue in Java
        pass
    else:
        consonants += 1

print("Number of vowels: {}".format(vowels))
print("Number of consonants: {}".format(consonants))