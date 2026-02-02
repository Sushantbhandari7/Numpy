import numpy as np

# Scalar Arthemetic

array = np.array([1,2,3,4])

print(array+4)
print(array-2)
# Simmilar operators /, **, * etc

# Vectorized math function
array = np.array([2,5,7,9])
print(np.sqrt(array))
print(np.round(array)) # for rounding down use np.floor and for up use np.ceil
print(np.pi)



# Excersise 
radii = np.array([2,3,4])
Area = np.pi * np.square(radii)
print(Area)

# Element-wise arthemetic
array1= np.array([1,2,3,4])
array2= np.array([2,3,4,5])

print(array1 + array2)

# Comparision operator 
print(array1[array1<2])