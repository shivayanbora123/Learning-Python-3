# Scopes of variables in Python:
# 1. Global scope
# 2. Local scope
# In general, functions create local scopes whereas loops and if statements don't

a = 250
b = [1,2,3]

def f1():
   #a = 100
   #b = a+10
   #print(a)
    global a # It must be on a separate line. This will allow the function to edit a global variable
    a = 100  # global: Overrides the global variable value
    b = 10
    print(a)
    print(b)

def f2():
    a = 50 # local
    b[0] = 5 # Without even using the global keyword, this will 
             # modify the global variable. This works the same for
             # lists and dictionaries
    print(a)
    # print(b): Error as b is local to f1 function

f1()
f2()

# When we try to change a global variale from inside a local scope Python stops 
# that from happening and automatically creates a local variable with the same name
print(a)
print(b)