import numpy as np

py_list = [1, 2, 3]  
np_array = np.array([1, 2, 3])

print("List * 2:", py_list * 2)      # Repeats list
print("Array * 2:", np_array * 2)    # Multiplies each element


# CREATING ARRAY
np.array([1, 2, 3])          # From list
np.zeros((2, 3))             # 2x3 array of zeros
np.ones((3,))                # 1D array of ones
np.arange(0, 10, 2)          # [0, 2, 4, 6, 8]
np.linspace(0, 1, 5)         # 5 values from 0 to 1
np.random.rand(2, 2)         # Random 2x2 array



#SLICING ARRAY
a = np.array([[10, 20, 30],
              [40, 50, 60]])

print(a[0, 1])      # Element at row 0, col 1 → 20
print(a[:, 1])      # All rows, column 1 → [20 50]
print(a[1, :])      # Row 1 → [40 50 60]
print(a[0:2, 1:])   # Subarray → [[20 30], [50 60]]


# ARURHEMATIC
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a + b)        # [5 7 9]
print(a * b)        # [4 10 18]
print(a ** 2)       # [1 4 9]



# AGGREGATIONS:

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(np.sum(a))    # 6
print(np.mean(b))   # 5.0
print(np.max(b))    # 6
print(np.min(a))    # 1







# 🔹 1. Scalar Broadcasting  
a = np.array([1, 2, 3])
scalar = 5
print("Scalar Broadcasting:")
print(a + scalar)  # Adds 5 to each element → [6 7 8]

# 🔹 2. Row-wise Broadcasting
matrix = np.array([[1, 2, 3],
                   [4, 5, 6]])
row = np.array([10, 20, 30])
print("\nRow-wise Broadcasting:")
print(matrix + row)  # Adds row to each row of matrix

# 🔹 3. Column-wise Broadcasting
col = np.array([[100],
                [200]])
print("\nColumn-wise Broadcasting:")
print(matrix + col)  # Adds column to each column of matrix

# 🔹 4. 3D Broadcasting
a_3d = np.ones((2, 1, 3))         # Shape: (2, 1, 3)
b_3d = np.array([[[10], [20]]])  # Shape: (1, 2, 1)
print("\n3D Broadcasting:")
result = a_3d + b_3d              # Final shape: (2, 2, 3)
print("Result shape:", result.shape)
print(result)

# 🔹 5. Shape Debugging
print("\nShape Debugging:")
print("a_3d shape:", a_3d.shape)
print("b_3d shape:", b_3d.shape)
