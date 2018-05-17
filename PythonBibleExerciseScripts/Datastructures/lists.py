our_list = [27,46,-5,17,99]
print(our_list)
print(type(our_list))

# Can have data from multiple datatypes
jackson = ["A","B","C",1,2,3,"Do","Rey","Mi",True,False]

# Lists are iterable
print(jackson[4])
print(jackson[7])
print(jackson[-2])

x = jackson[6]
print(x)

# Lists can be sliced
print(jackson[0:3:1])

# Lists can have other lists inside them as well
our_list = [1,2,[3,4,5],6,7,8]
print(our_list[2])
print(our_list[2][0])
print(our_list[2][1:])
print(our_list[2][0::2])

# 2D Matrix/Table structure [rows][columns]
our_table = [[1,2,3],[4,5,6],[7,8,9]]

print(our_table[1][2])
print(our_table[2][1])

# We can create 3D cube structures as well

# More ways to add items to lists
A = [5,12,72,55,89]
# 1st method: Will add in the end
A = A + [1]
A = A + ["BCD"]

# 2nd Method: Will take each element of the string 
# and add it separately to the list. 
# Can take only iterable inputs like 
# strings or different lists
A = A + list("BCD")
print(A)

A = A + list(str(123))
print(A)

B = [5,12,72,55,89,1]

B = B + [[5,6,7,8]]
print(B)

# append() method of lists returns null vale 
# or in terms of python, NoneType
# Here B is no longer a list and if we want to use 
# it as a list, we need to reinitialize it as one
B = B.append(10)
print(B)
print(type(B))

# This also returns NoneType
# Lists are mutable
C = [5,12,72,55,89,1]
C.insert(2,100)
print(C)
C.insert(2,[1,20,30])
print(C)