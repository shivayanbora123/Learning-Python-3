# if condition :
num1 =  100
num2 = 1000
if num1 > num2:
    print("num1 is bigger than num2")
elif num2 > num1:
    print("num2 is bigger than num1")
else:
    print("Both numbers are equal")

# not operator
x = 10
y = 20

if not y < x:
    print("It worked!")

# and operator
c = 10
d = 5
if c >= 10 and d >= 1:
    print("It worked again!!")

# nand operation
if not(c > 10 and d > 1):
    print("NAND Operation worked!!")

# or operator
a = 5
b = -1
if a > 1 or b > 1:
    print("or function 1")

b = 5
if a > 1 or b > 1:
    print("or function 2")

if a > 100 or d > 100:
    print("or function 3")

# nor operation
if not(a > 100 or d > 100):
    print("NOR Operation worked!!")

# Complex operation
a = 6
b = 2
if (a>5 and b>5) or (a>1 and b>1):
    print("Complex operation worked!!")