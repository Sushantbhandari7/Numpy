import numpy as np

array = np.array([[1,2,3,4,5],[6,7,8,9,10]])

print(np.sum(array))
print(np.std(array))
# for minimun value np.min()
# for maximum np.max()
# for posityion for max or min np.argmin/max()

print(np.sum(array, axis = 0))

