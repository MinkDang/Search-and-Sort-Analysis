# %% [markdown]
# # Comparing Binary and Linear Search

# %% [markdown]
# ## Configuration

# %% [markdown]
# ### Import

# %%
import numpy as np
from IPython.display import clear_output
from timeit import default_timer as timer

# %% [markdown]
# ### Integer Check

# %%
def int_check(prompt, no_zero = None):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            if no_zero is None:
                value = np.random.randint(np.iinfo(np.int32).max)
            else:
                print("Check input")
                continue
        
        if no_zero is None and value < 0:
            print("Please input a number larger or equal to 0")
            continue
        
        if no_zero is not None and (value < 1 or value > 10**6):
            print("Please input a number between 1 and 1,000,000")
            continue

        clear_output()
        return value

# %% [markdown]
# ### Ramdom setup

# %%
seed_info = int_check("Choose your seed: ") # If ValueError then a random seed between 0 and top limit of int32 would be selected
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
print(f"Seed: {seed_info}")

# %% [markdown]
# ### Get Number

# %%
tofind = int_check("Number to search for: ", True)

# %% [markdown]
# ## ***Binary* Search** ##

# %%
def BinarySearch():

    start = timer() # Performance - Start timer

    i_value = 1
    min_value = 0
    max_value = unique_arr_sorted.size

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
# ## ***Linear* Search**

# %% [markdown]
# ### General Function

# %%
def LinearSearch(arraytosearch, flag):

    start = timer() # Performance - Start timer

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


