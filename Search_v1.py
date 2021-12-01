# %% [markdown]
# # Comparing Binary and Linear Search

# %% [markdown]
# ## Configuration

# %% [markdown]
# ### Import

# %%
import numpy as np
from timeit import default_timer as timer

# %% [markdown]
# ### Ramdom setup

# %%
seed_info = int(input("Choose your seed: "))

np.random.seed(seed_info)

arr = np.random.randint(low = 1, high = 10**6, size = 10**5)

# %% [markdown]
# ### Duplication handling

# %%
_, idx = np.unique(arr, return_index=True)

unique_arr_unsorted = arr[np.sort(idx)]

unique_arr_sorted = np.unique(arr)

print(f"{arr.size - unique_arr_sorted.size} duplicate values removed from array")
print(f"{unique_arr_sorted.size} values remaining")

# %% [markdown]
# ### Get Number

# %%
tofind = int(input("Number to search for: "))

# %% [markdown]
# ## **_Binary_ Search** ##

# %%
def BinarySearch():

    start = timer() # Performance - Start timer

    i_value = 1
    min_value = 0
    max_value = unique_arr_sorted.size
    found = False

    while min_value <= max_value:
        mid_value = int(min_value + (max_value - min_value) / 2)
        if unique_arr_sorted[mid_value] == tofind:
            end = timer() # Performance - End timer
            print(f"Number {tofind} found \
                \nPosition in array: {mid_value + 1} \
                \nLoops: {i_value} \
                \nTime: {(end-start)*10**6} microseconds")
            return
        elif tofind < unique_arr_sorted[mid_value]:
            max_value = mid_value - 1
            i_value += 1
        else:
            min_value = mid_value + 1
            i_value += 1
    
    end = timer() # Performance - End timer
    print(f"Number {tofind} NOT found \
        \nMaximum Loops: {i_value} \
        \nMax time: {(end - start)*10**6} mircoseconds")

BinarySearch()

# %% [markdown]
# ## **_Linear_ Search**

# %% [markdown]
# ### General Function

# %%
def LinearSearch(arraytosearch, flag):

    start = timer() # Performance - Start timer

    found = False

    for index, item in enumerate(arraytosearch):
        if tofind == item:
            end = timer() # Performance - End timer
            strvalue = "sorted"
            if flag:
                strvalue = "unsorted"
            
            print(f"Number {tofind} found \
                \nPosition in {strvalue} array: {index + 1} \
                \nLoops: {index + 1} \
                \nTime: {(end-start)*10**6} microseconds")
            return
    end = timer() # Performance - End timer
    print(f"Number {tofind} NOT found \
        \nMaximum Loops: {arraytosearch.size} \
        \nMax time: {(end-start)*10**6} microseconds")
    

# %% [markdown]
# ### *Unsorted* array

# %%
LinearSearch(unique_arr_unsorted, True)

# %% [markdown]
# ### *Sorted* array

# %%
LinearSearch(unique_arr_sorted, False)


