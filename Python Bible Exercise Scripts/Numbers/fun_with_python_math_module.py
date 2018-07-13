import math

# This is an inbuilt Python function which will Round up to either floor or roof based on the value in the decimal point. If the value is more than 0.5, it'll be roof else floor
print(round(1.5))

# Will round to the floor value
print(math.floor(1.5))
# Will round to the roof/ceiling value value
print(math.ceil(1.5))
# Will print the value of pi in mathematics i.e. 3.141....
print(math.pi)
# Will print the value of e in mathematics i.e. 2.718....
print(math.e)

# math module has inbuilt trigonometic and inverse trigonometric functions as well but it takes the inputs as radians and not in degrees
print(math.sin(math.pi/2))
print(math.sin(math.pi)) # Since pi is an approximation, this will not yeild 0. We need to use floor in conjunction with it
print(math.floor(math.sin(math.pi)))
print(math.cos(0))
print(math.asin(0))
print(math.acos(0))

# To find the hypotenuse of a right angled triangle
# This is also useful for finding resultant vectors in vector algebra as well
print(math.hypot(3,4))

# To find the power of a number
print(math.pow(2,3)) # Same as 2 ** 3 in python but it will output an integer instead of a float
print(2 ** 3)

# To find the exponential
print(math.exp(2))

# To find natural logs i.e. log with base e
print(math.log(math.e))

# To find logs of a particular base
print(math.log10(1000))
print(math.log2(8))

# Extra: Check out numpy and scipy modules of python for more mathematical operations used in data science