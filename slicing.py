import numpy as np

array = np.array([[1,2,3,4],
                  [5,6,7,8],
                  [9,10,11,12],
                  [13,14,15,16]])
# array[start:end:step]
# [] is the subscript operator 
# Here ios how I would print first row of an 2d array
print(array[0:3])  #Here the end is exclusive, so it print one less row
print(array[1:4:2])