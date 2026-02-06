import numpy as np

# 1. Create a NumPy array
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# 2. Define the condition (e.g., elements greater than 5)
# This creates a boolean array [False, False, False, False, False, True, True, True, True, True]
boolean_mask = arr > 5

# 3. Use the boolean mask to filter the original array
filtered_arr = arr[boolean_mask]

print(filtered_arr)
# Output: [6 7 8 9 10]

# The condition can be applied directly during indexing:
filtered_arr_direct = arr[arr > 5]
print(filtered_arr_direct)
# Output: [6 7 8 9 10]
