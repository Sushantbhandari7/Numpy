import numpy as np

ages = np.array([[21,23,22,25,16,15,67],
                 [39,22,15,99,18,19,20]])
filtered_data = ages[ages < 18]
print(filtered_data)
