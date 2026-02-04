import numpy as np

array1 = np.array([[1],[2],[3],[4],[5],[6]])
array2 = np.array([1,2,3,4,5,6])

print(array1 * array2)

# Working of Broadcasting in NumPy
# Broadcasting applies specific rules to find whether two arrays can be aligned for operations or not that are:

# Check Dimensions: Ensure the arrays have the same number of dimensions or expandable dimensions.
# Dimension Padding: If arrays have different numbers of dimensions the smaller array is left-padded with ones.
# Shape Compatibility: Two dimensions are compatible if they are equal or one of them is 1.

# a= np.array([[1,2,3],
#              [1,2,3],
#              [1,2,3]])
# b= np.array([[1,2,3],[1,2,3]])
# print(a*b)  this will cause an error because you cannot broadcast shaped (3,3) with (2,3)


