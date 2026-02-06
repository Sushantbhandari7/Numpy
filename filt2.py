import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60])

# Filter for values greater than 25 AND less than 55
filtered_arr = arr[(arr > 25) & (arr < 55)] 

print("Filtered array (25 < x < 55):", filtered_arr)
# Output: Filtered array (25 < x < 55): [30 40 50]
