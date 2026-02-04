import numpy as np

array = np.array([[1,2,3],[3,4,5]])
print(array.ndim)
print(array)

array2= np.array([[1,2,3],[4,5,6]])
print(array2.ndim)
print(array2)
print(array*array2)

array3= np.array([[[1,2,3],[2,3,4],[2,3,4]],
                 [[2,4,5],[4,5,6],[1,3,4]],
                 [[3,4,5],[1,2,3],[1,2,3]]])
print(array3.ndim)
print(array3)
print(array3.shape)