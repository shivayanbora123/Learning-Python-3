# Function parameters are the ones we have in the definition of the
# function on what needs to be sent to it. e.g. here name, age and 
# likes are parameters

# likes will have a default value of "Python". Also, default values 
# of parameters must go at the end. And we can put multiple parameters
# with default values
def about(name, age, likes = "Python"):
    sentence = "Meet {}! They're {} years old and they like {}".format(name,age,likes)
    return sentence

# Function arguments are the values that we send to the function while calling it as 
# shown below i.e. "Shivayan", 27 and "Python"
# This is an example of positional arguments where the position of the arguments 
# corresponds to which parameter it belongs to
print(about("Shivayan",27,"Dirty Bomb"))

# These are keyword arguments where we are assiging particular arguments 
# to the parameters of the function. As shown below, it needn't be in any
# particular order
print(about(age = 27, name = "Shivayan", likes = "Python"))

print(about("Shivayan",27))