import numpy as np
array3= np.array([[[1,2,3],[2,3,4],[2,3,4]],
                 [[2,4,5],[4,5,6],[1,3,4]],
                 [[3,4,5],[1,2,3],[1,2,3]]])
print(array3[1][1][2])    #This is chain indexing 

print(array3[1,2,1])
