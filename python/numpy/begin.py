import numpy as np

print(np.__version__)

a = np.array([1,2,3])
print(a)
print(a.shape)
print(a.dtype)
print(a.ndim)
print(a.size)
print(a.itemsize)

print(a[0])
a[0]=10

b = a * np.array([2,0,2]) # element is multiplied

print(b)









# ARRAY VS LIST

l = [1,2,3]
a= np.array([1,2,3])

print(l)
print(a)

l = l+ [4] # appends 4
print(l)

a = a+ np.array([4]) # adds 4 to every elemnet
print(a)


l = l * 2 #  adds the elements again
print(l)

a = a * 2 # multipys every element by 2
print(a)
# SO WE KNOW NOW THAT IN ARRAY THE MATHEMATICLA OPERATOR OPERATES ON ELEMENTS





l1 = [1,2,3]
l2 = [4,5,6]
a1= np.array(l1)
a2= np.array(l2)

# DOT PRODUCT
dot = 0
for i in range(len(l1)):
    dot+= l1[i]*l2[i]
print(dot)

dot = np.dot(a1,a2)
print(dot)

sum1 = a1*a2
dot = np.sum(sum1)
print(dot)

dot = (a1*a2).sum()
print(dot)

dot = a1 @ a2
print(dot)



#MMULTIDIMENTINAL ARRAY

a = np.array([[1,2,6],[3,4,8]])
print(a)
print(a.shape)

print(a[1,0])
print(a[:,0])
print(a[0,:])
print()
print(a.T) #TRANSPOSE

a = np.array([[1,2],[3,4]])
print(np.linalg.inv(a)) # inverse
print(np.linalg.det(a))
print(np.diag(a)) # DIGONAL ELEMNETS





# SLICING
a = np.array([[1,2,3,4],[5,6,7,8]])
print(a)

b = a[0,1:3]
print(b)

c = a[-1,-1]
print(c)
print()

# boolean indexing

a = np.array([[1,2],[3,4],[5,6]])
print(a)

bool_idx = a>2
print(bool_idx)
print(a[bool_idx])
print(a[a>2])

b = np.where(a>2,a,-1) # FOR a>2 PRINTS A ELEMENT OTHERWISE -1

print(b)

# FANCY INDEXCING -> for printong the specific index elements only

a=np.array([10,1,38,41,50,62])
print(a)
b= [1,3,5]
print(a[b])
print()





# 🔄 RESHAPING ARRAYS

# Create a 1D array with values from 1 to 6
a = np.arange(1, 7)  # [1 2 3 4 5 6]
print("Original 1D array:")
print(a)
print("Shape:", a.shape)  # Shape: (6,)

# Reshape into 2 rows and 3 columns
b = a.reshape((2, 3))  # Shape: (2, 3)
print("\nReshaped to (2, 3):")
print(b)

# Reshape into 3 rows and 2 columns
b = a.reshape((3, 2))  # Shape: (3, 2)
print("\nReshaped to (3, 2):")
print(b)


# ➕ ADDING DIMENSIONS WITH np.newaxis

# Recreate original 1D array
a = np.arange(1, 7)  # [1 2 3 4 5 6]
print("\nOriginal 1D array again:")
print(a)

# Convert to column vector (6 rows, 1 column)
b = a[:, np.newaxis]  # Shape: (6, 1)
print("\nColumn vector using a[:, np.newaxis]:")
print(b)

# Convert to row vector (1 row, 6 columns)
b = a[np.newaxis, :]  # Shape: (1, 6)
print("\nRow vector using a[np.newaxis, :]:")
print(b)





# CONCATANATION

a = np.array([[1,2],[3,4]])
print(a)
print()
b = np.array([[5,6]])
print(b)
print()
c = np.concatenate((a,b), axis=0)
print(c)
print()
c = np.concatenate((a,b), axis= None)
print(c)
c = np.concatenate((a,b.T), axis=1)
print(c)



a = np.array([[1, 2], [3, 4]])  # shape (2, 2)
b = np.array([[5, 6]])         # shape (1, 2)

np.concatenate((a, b), axis=0)     # Adds row → shape (3, 2)
np.concatenate((a, b.T), axis=1)   # Adds column → shape (2, 3)
np.concatenate((a, b), axis=None)  # Flattens → shape (6,)


# HSTACK
a = np.array([1,2,3,4])
b = np.array([5,6,7,8])

c = np.hstack((a,b))
print(c)
print()
c= np.vstack((a,b)) # new array as new row
print(c)
print()





# BROADCASTING

# 🎯 BROADCASTING BASICS

# Example 1: Adding a scalar to an array
a = np.array([1, 2, 3])
b = 10  # Scalar value
print("Adding scalar to array:")
print(a + b)  # Each element of 'a' gets 10 added → [11 12 13]

# Example 2: Adding a 1D array to a 2D array (row-wise broadcast)
a = np.array([[1, 2, 3],
              [4, 5, 6]])
b = np.array([10, 20, 30])  # Shape: (3,)
print("\nAdding 1D array to 2D array (row-wise):")
print(a + b)  # 'b' is broadcast across each row

# Example 3: Adding a column vector to a 2D array (column-wise broadcast)
a = np.array([[1, 2, 3],
              [4, 5, 6]])
b = np.array([[10],
              [20]])  # Shape: (2,1)
print("\nAdding column vector to 2D array (column-wise):")
print(a + b)  # 'b' is broadcast across each column

# Example 4: Broadcasting with different shapes
a = np.ones((4, 1, 6))       # Shape: (4, 1, 6)
b = np.ones((1, 5, 1)) * 2   # Shape: (1, 5, 1)
print("\nBroadcasting across 3D arrays:")
print((a + b).shape)  # Result shape: (4, 5, 6)

# 🧠 Broadcasting Rule:
# Dimensions are compared from the end. If they match or one is 1, broadcasting is allowed.



