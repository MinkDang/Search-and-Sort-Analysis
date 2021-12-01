import numpy as np

arr = np.array([1,1,1,2,4,2,44,22,44,5])

# Determine duplicates value using numpy
# https://stackoverflow.com/questions/11528078/determining-duplicate-values-in-an-array 
s = np.sort(arr, axis=None)
s[:-1][s[1:] == s[:-1]]

# Test unique number for return_index behaviour. Same outcome can be achieved by Pandas.unique()
# https://stackoverflow.com/questions/15637336/numpy-unique-with-order-preserved/15637512#15637512 
_, idx = np.unique(arr, return_index=True)
test = arr[np.sort(idx)]