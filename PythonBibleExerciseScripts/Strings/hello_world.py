name = "Ziyad"
print(type(name))

message = 'John said to me "I will see you later"'
message1 = "John said to me 'I will see you later'"

print(message)
print(message1)

romeo = """Bacon ipsum dolor amet tail 
beef ribs jowl frankfurter, brisket meatloaf 
ground round. Tongue spare ribs sausage biltong, 
filet mignon short ribs pork belly meatball kevin
tenderloin andouille. Fatback buffalo drumstick,
frankfurter meatloaf ham picanha filet mignon rump 
kielbasa meatball cow shank swine. Beef sirloin 
hamburger, filet mignon buffalo leberkas meatloaf 
pastrami porchetta drumstick bresaola venison 
andouille cow pig. Spare ribs turkey picanha, 
bacon beef pork chop short ribs filet mignon 
landjaeger pancetta. Prosciutto pork belly 
tenderloin tongue meatball shankle, meatloaf 
burgdoggen. Filet mignon flank capicola ham 
sirloin meatball."""

romeo1 = '''Bacon ipsum dolor amet tail 
beef ribs jowl frankfurter, brisket meatloaf 
ground round. Tongue spare ribs sausage biltong, 
filet mignon short ribs pork belly meatball kevin
tenderloin andouille. Fatback buffalo drumstick,
frankfurter meatloaf ham picanha filet mignon rump 
kielbasa meatball cow shank swine. Beef sirloin 
hamburger, filet mignon buffalo leberkas meatloaf 
pastrami porchetta drumstick bresaola venison 
andouille cow pig. Spare ribs turkey picanha, 
bacon beef pork chop short ribs filet mignon 
landjaeger pancetta. Prosciutto pork belly 
tenderloin tongue meatball shankle, meatloaf 
burgdoggen. Filet mignon flank capicola ham 
sirloin meatball.'''

print(romeo)
print(romeo1)

hello = "Hello World!"
print(hello)

# /n: Newline Character
# /t: Tab

# String immutability example:
# Let's try to change the first letter to 'x'
#s[0] = 'x'
# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# <ipython-input-26-976942677f11> in <module>()
#       1 # Let's try to change the first letter to 'x'
# ----> 2 s[0] = 'x'
# TypeError: 'str' object does not support item assignment