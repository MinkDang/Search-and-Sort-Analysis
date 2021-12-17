# %% [markdown]
# # Comparing Binary and Linear Search

# %% [markdown]
# ## Configuration

# %% [markdown]
# ### Import

# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import clear_output
from timeit import default_timer as timer

# %% [markdown]
# ### Ramdom setup + Linear Search Confirmation

# %%
def int_check(prompt, flag = None):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            if flag is False:
                value = np.random.randint(np.iinfo(np.int32).max)
            else:
                print("Check input")
                continue
        
        if value < 0:
            print("Please input a number larger than 0")
            continue

        if flag is True and value < range_low:
            print("Invalid top end")
            continue
        
        clear_output()
        return value

range_low = int_check("Choose the bottom end of your randomness ( ≥ 0 ): ")
range_high = int_check("Choose the top end of your randomness ( ≥ 0 ): ", True)
random_size = int_check("Choose the size of the array ( ≥ 0 ): ")

seed_info = int_check("Choose your seed ( ≥ 0 ): ", False) # If ValueError then a random seed between 0 and top limit of int32 would be selected
np.random.seed(seed_info)
arr = np.random.randint(low = range_low, high = range_high, size = random_size)

exec_unsort = input("CONFIRMING LINEAR search on UNSORTED array (yes): ")
exec_sort = input("CONFIRMING LINEAR search on SORTED array (yes): ")

# %% [markdown]
# ### Duplication handling

# %%
unique_arr_unsorted = pd.unique(arr)

unique_arr_sorted = np.sort(unique_arr_unsorted)

print(f"{arr.size - unique_arr_sorted.size} duplicate values removed from array")
print(f"{unique_arr_sorted.size} values remaining")
print(f"Seed: {seed_info}")

# %% [markdown]
# ## **_Binary_ Search** ##

# %%
def BinarySearch():

    start = timer() # Performance - Start timer

    min_value = 0
    max_value = unique_arr_sorted.size

    while min_value <= max_value:
        mid_value = int(min_value + (max_value - min_value) / 2)
        if unique_arr_sorted[mid_value] == tofind:
            end = timer() # Performance - End timer
            return (end - start)*10**6
        elif tofind < unique_arr_sorted[mid_value]:
            max_value = mid_value - 1
        else:
            min_value = mid_value + 1
            
bs_performance = []

for tofind in unique_arr_sorted:
    performance = BinarySearch()
    if performance is not None:
        bs_performance.append(performance)

binary_df = pd.DataFrame({'Number': unique_arr_sorted, 'Time (microseconds)': bs_performance})

# %% [markdown]
# ## **_Linear_ Search**
# Be aware of the computing power and time this would taken

# %% [markdown]
# ### General Function

# %%
def LinearSearch(arraytosearch):

    start = timer() # Performance - Start timer

    for item in arraytosearch:
        if tofind == item:
            end = timer() # Performance - End timer
            return (end - start)*10**6

# %% [markdown]
# ### *Unsorted* array

# %%
if exec_unsort.lower() == 'yes':
    ls_unsorted_performance = []

    for tofind in unique_arr_unsorted:
        performance = LinearSearch(unique_arr_unsorted)
        if performance is not None:
            ls_unsorted_performance.append(performance)

    linear_unsorted_df = pd.DataFrame({'Number': unique_arr_unsorted, 'Time (microseconds)': ls_unsorted_performance}).sort_values(by = ['Number'])

# %% [markdown]
# ### *Sorted* array

# %%
if exec_sort.lower() == 'yes':
    ls_sorted_performance = []

    for tofind in unique_arr_sorted:
        performance = LinearSearch(unique_arr_sorted)
        if performance is not None:
            ls_sorted_performance.append(performance)

    linear_sorted_df = pd.DataFrame({'Number': unique_arr_sorted, 'Time (microseconds)': ls_sorted_performance})

# %% [markdown]
# ## Performance visualisation

# %% [markdown]
# ### Binary Search
# *log(n)* trend line

# %%
fig1 = binary_df.plot(x = 'Number', y = 'Time (microseconds)', kind = 'scatter', figsize = (30 , 10), fontsize = 14, loglog = True, c = 'firebrick')

fig1.set_ylabel('Time (microseconds)', fontdict = {'fontsize': 15})
fig1.set_xlabel('Number (n)', fontdict = {'fontsize': 15})

fig1.set_title('Binary Search Performance', fontdict = {'fontsize': 15})

plt.show()
plt.close()

# %% [markdown]
# ### Linear Search

# %% [markdown]
# #### Unsorted Array

# %%
if exec_unsort.lower() == 'yes':
    fig2 = linear_unsorted_df.plot(x = 'Number', y = 'Time (microseconds)', kind = 'scatter', figsize = (30 , 10), fontsize = 20, loglog = True, c = 'sandybrown')

    fig2.set_ylabel('Time (microseconds)', fontdict = {'fontsize': 15})
    fig2.set_xlabel('Number (n)', fontdict = {'fontsize': 15})
    
    fig2.set_title('Linear Search - Unsorted - Performance', fontdict = {'fontsize': 17})
    
    plt.show()
    plt.close()

# %% [markdown]
# #### Sorted Array

# %%
if exec_sort.lower() == 'yes':
    fig3 = linear_sorted_df.plot(x = 'Number', y = 'Time (microseconds)', kind = 'scatter', figsize = (30 , 10), fontsize = 20, loglog = True, c = 'darkgoldenrod')

    fig3.set_ylabel('Time (microseconds)', fontdict = {'fontsize': 15})
    fig3.set_xlabel('Number (n)', fontdict = {'fontsize': 15})

    fig3.set_title('Linear Search - Sorted - Performance', fontdict = {'fontsize': 17})
    
    plt.show()
    plt.close()

# %% [markdown]
# ### Combined graphs

# %%
fig_combined = binary_df.plot(x = 'Number', y = 'Time (microseconds)', kind = 'scatter', figsize = (30 , 10), fontsize = 20, loglog = True, label = 'Binary Search', c = 'firebrick', zorder = 3)

if exec_sort.lower() == 'yes':
    linear_sorted_df.plot(x = 'Number', y = 'Time (microseconds)', kind = 'scatter', label = 'Linear Search - Sorted', c = 'darkgoldenrod', ax = fig_combined, zorder = 2)

if exec_unsort.lower() == 'yes':
    linear_unsorted_df.plot(x = 'Number', y = 'Time (microseconds)', kind = 'scatter', label = 'Linear Search - Unsorted', c = 'sandybrown', ax = fig_combined)

details = 'DATA: Seed: ' + str(seed_info) + '; Min: ' + str(range_low) + '; Max: ' + str(range_high) + '; Length of array: ' + str(unique_arr_sorted.size) + ' (Duplicates Removed: ' + str(arr.size - unique_arr_sorted.size) + ')' 

fig_combined.grid(axis = 'y', linestyle = (0, (5, 10)))
fig_combined.set_ylabel('Time (mircoseconds)', fontdict = {'fontsize': 15})
fig_combined.set_xlabel('''Number (n)

{}'''.format(details), fontdict = {'fontsize': 15})
fig_combined.set_title('Search Performance Visualisation', fontdict = {'fontsize': 17})

lgnd = fig_combined.legend(loc = "upper left", scatterpoints = 1, fontsize = 15)
for handle in lgnd.legendHandles:
    handle.set_sizes([100])

save_fig = input("Would you like to save the plot in high resolutions (yes): ")
if save_fig.lower() == 'yes':
    plt.savefig('Search Comparison.png', dpi = 300, facecolor = 'white', transparent = False, bbox_inches = 'tight')

plt.show()
plt.close()


