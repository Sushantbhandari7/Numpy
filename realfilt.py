import numpy as np

ages = np.array([[21,23,22,25,16,15,67],
                 [39,22,15,99,18,19,20]])
# teenagers = ages[ages < 18]
# adults = ages[(ages > 18) & (ages <= 65)]
# seniors = ages[ages > 65]
# print(seniors)
# In order to put the same dimension as the main array we have to put np.where functioon 

main_array = np.where((ages>18) & (ages <= 65), ages , -1)
print(main_array)
adults = ages[(ages>18) & (ages <= 65)]
print(adults)