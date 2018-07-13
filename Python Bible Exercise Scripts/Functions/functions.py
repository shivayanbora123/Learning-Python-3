# A function is a block of organised and reusable code 
# that performs an actions or gives some result
# Function definition has to come before a function call
def add(x,y):
    return x+y

print(add(5,10))

# Note: Returing a value is not the same as printing
# Function for creating a reversed iterable
def rev(word):
    return word[::-1]

print(rev("Shivayan"))