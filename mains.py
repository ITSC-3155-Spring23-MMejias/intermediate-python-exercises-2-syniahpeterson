# Syniah Peterson
# I used https://www.w3schools.com/python/numpy/numpy_creating_arrays.asp to import numpy
# I used https://www.geeksforgeeks.org/numpy-mean-in-python/ to find the mean
# I used https://www.geeksforgeeks.org/numpy-median-in-python/ to find the median
# I used https://www.geeksforgeeks.org/numpy-std-in-python/ to find the standard deviation
import numpy as np

arr = []
for i in range(10):
    rand_num = np.random.normal(0, 1, 1)
    arr.append(rand_num)
print(arr)
print("Mean: ", np.mean(arr))
print("Median: ", np.median(arr))
print("Standard deviation: ", np.std(arr))
