# Tuples are similar to lists but it is immutable
our_tuple = 1,2,3,"A","B","C"
print(our_tuple)
print(type(our_tuple))

our_tuple1 = (1,2,3,"A","B","C")
print(our_tuple1)
print(type(our_tuple1))

# Can be sliced
print(our_tuple[0:3])

# Creating tuples from lists
A = [1,2,3]
new_tuple = tuple(A)
print(new_tuple)

# Assigning multiple variables:
(X,Y,Z) = 1,2,3
print(X)
print(Y)
print(Z)

# Individual elements from the list
D,E,F = [1,2,3]
print(D)
print(E)
print(F)

# Individual elements from the string
G,H,I = "789"
print(G)
print(H)
print(I)