import numpy as np

arr = np.array([1,1,1,2,4,2,44,22,44,5])

sort = np.sort(arr)

u, c = np.unique(arr, return_counts=True)

dup = u[c > 1]