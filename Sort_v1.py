# %% [markdown]
# # Comparing Insertion Sort, Selection Sort and Bubble Sort

# %% [markdown]
# ## Configuration

# %% [markdown]
# ### Import

# %%
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import clear_output
from timeit import default_timer as timer

# %% [markdown]
# ### Data processing
# 

# %% [markdown]
# Import CSV with filter from <https://simplemaps.com/data/world-cities>

# %%
cities = np.loadtxt('CSVs/simplemaps_worldcities_basicv1.74/worldcities.csv', 
delimiter = ',', usecols = [1], skiprows = 1, dtype = object, encoding = 'utf-8')

# %% [markdown]
# Sample size customisation

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

        if no_zero is not None and (value <= 0 or value > len(cities)):
            print("Please input a number larger than 0 and smaller than " + str(len(cities)))
            continue
        
        clear_output()
        return value

seed_info = int_check('Choose your seed ( ≥ 0 ): ') # If ValueError then a random seed between 0 and top limit of int32 would be selected
np.random.seed(seed_info)

sample_size = int_check('Choose your sample size ( > 0 and ≤ 41001): ', True)
cities_selection = cities[np.random.choice(len(cities), size = sample_size, replace = False)] # replace = False: No duplicates in the return random -> Max size = 41001

print(f"Seed: {seed_info}, Length of array: {sample_size}")

# %% [markdown]
# ## __*Insertion*__ **sort**
# Insertion sort is a sorting algorithm that places an unsorted element at its suitable place in each iteration.

# %%
def Insertion_sort(tosort, descending = None):
    new_reference = tosort.copy()

    start = timer() # Performance - Start timer

    for i in range(1, len(new_reference)):
        key = new_reference[i]
        j = i - 1

        # Compare key with each element on the left of it until an element smaller/larger than it is found
        if descending == None:
            while j >= 0 and key < new_reference[j]:
                new_reference[j + 1] = new_reference[j]
                j -= 1
        # Descending order, change key < new_reference[j] to key > new_reference[j]
        else:
            while j >= 0 and key > new_reference[j]:
                new_reference[j + 1] = new_reference[j]
                j -= 1
        
        # Place key at after the element just smaller/larger than it.
        new_reference[j+1] = key
    
    end = timer() # Performance - End timer

    return (end - start)*10**6

insertion_ascending = Insertion_sort(cities_selection)
insertion_descending = Insertion_sort(cities_selection, True)
print(f"INSERTION Sort\nAscending: {insertion_ascending} microseconds\nDescending: {insertion_descending} mircroseconds")

# %% [markdown]
# ## **_Selection_ sort**
# Selection sort is a sorting algorithm that selects the smallest element from an unsorted list in each iteration and places that element at the beginning of the unsorted list.

# %%
def Selection_sort(tosort, descending = None):
    new_reference = tosort.copy()

    start = timer() # Performacnce - Start timer
    
    for i in range(len(new_reference)):
        idx = i

        for j in range(i + 1, len(new_reference)):

            # Select the minimum/maximum element in each loop
            if descending == None:
                if new_reference[j] < new_reference[idx]:
                    idx = j
            # Descending order, change '<' to '>'
            else:
                if new_reference[j] > new_reference[idx]:
                    idx = j
         
        # Swapping
        (new_reference[i], new_reference[idx]) = (new_reference[idx], new_reference[i])
    
    end = timer() # Performance - End timer
    
    return (end - start)*10**6

selection_ascending = Selection_sort(cities_selection)
selection_descending = Selection_sort(cities_selection, True)
print(f"SELECTION Sort\nAscending: {selection_ascending} microseconds\nDescending: {selection_descending} mircroseconds")

# %% [markdown]
# ## **_Bubble_ sort**
# Bubble sort is a sorting algorithm that compares two adjacent elements and swaps them until they are not in the intended order.

# %%
def Bubble_sort(tosort, descending = None):
    new_reference = tosort.copy()

    start = timer() # Performance - Start timer

    # Loop to access each array element
    for i in range(len(new_reference) - 1):

        # Loop to compare array elements
        for j in range(0, len(new_reference) - 1):

            # Compare two adjacent elements and swap in order
            if descending == None:
                if new_reference[j] > new_reference[j + 1]:
                    (new_reference[j], new_reference[j + 1]) = (new_reference[j + 1], new_reference[j])
            # Descending order, change '<' to '>'
            else:
                if new_reference[j] < new_reference[j + 1]:
                    (new_reference[j], new_reference[j + 1]) = (new_reference[j + 1], new_reference[j])
    
    end = timer() # Performance - End timer
    
    return (end - start)*10**6

bubble_1_ascending = Bubble_sort(cities_selection)
bubble_1_descending = Bubble_sort(cities_selection, True)
print(f"BUBBLE Sort\nAscending: {bubble_1_ascending} microseconds\nDescending: {bubble_1_descending} mircroseconds")

# %% [markdown]
# ## **_Bubble_ sort** (Optimised)

# %%
def Bubble_sort_optimised(tosort, descending = None):
    new_reference = tosort.copy()

    start = timer() # Performance - Start timer

    # Loop to access each array element
    for i in range(len(new_reference)):
        
        # Loop to compare array elements (1 less item each loop)
        for j in range(0, len(new_reference) - i - 1):

            # Compare two adjacent elements and swap in order
            if descending == None:
                if new_reference[j] > new_reference[j + 1]:
                    (new_reference[j], new_reference[j + 1]) = (new_reference[j + 1], new_reference[j])
            # Descending order, change '<' to '>'
            else:
                if new_reference[j] < new_reference[j + 1]:
                    (new_reference[j], new_reference[j + 1]) = (new_reference[j + 1], new_reference[j])

    end = timer() # Performance - End timer

    return (end - start)*10**6

bubble_2_ascending = Bubble_sort_optimised(cities_selection)
bubble_2_descending = Bubble_sort_optimised(cities_selection, True)
print(f"BUBBLE Sort (Optimised)\nAscending: {bubble_2_ascending} microseconds\nDescending: {bubble_2_descending} mircroseconds")

# %% [markdown]
# ## Result Visualisation
# Example from https://matplotlib.org/stable/gallery/lines_bars_and_markers/barchart.html

# %%
labels = ['Insertion', 'Selection', 'Bubble', 'Bubble (Optimised)']
ascending_list = [insertion_ascending, selection_ascending, bubble_1_ascending, bubble_2_ascending]
descending_list = [insertion_descending, selection_descending, bubble_1_descending, bubble_2_descending]

for i in range(4):
    ascending_list[i] = int(ascending_list[i])
    descending_list[i] = int(descending_list[i])

x = np.arange(len(labels))
width = 0.35 # Width of each bar

fig, ax = plt.subplots(figsize = (20,10))

rects1 = ax.bar(x - width/2, ascending_list, width, label='Ascending')
rects2 = ax.bar(x + width/2, descending_list, width, label='Descending')
plt.rcParams["font.size"] = "18"

# Change y-label when suitable
yticks = ax.get_yticks().astype(str)
zeros_count = int(yticks[1].count('0')) - 1

if zeros_count > 1:
    for i in range(1, len(yticks)):
        yticks[i] = str(int(float(yticks[i])))[:zeros_count*-1] + ' * 10^' + str(zeros_count)

    ax.set_yticklabels(yticks)

# Other setup
ax.set_ylabel('Time (Microseconds)')
ax.set_title('''Different sorting algorithms' performance on {} array items'''.format(sample_size), fontsize = 20)
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend(loc = 'upper left')

bbox = dict(boxstyle="round", ec="w", fc="k", alpha=.75)
ax.bar_label(rects1, label_type = 'center', c = 'w', fmt = '%d', bbox = bbox, fontsize = 18, padding = -10)
ax.bar_label(rects2, label_type = 'center', c = 'w', fmt = '%d', bbox = bbox, fontsize = 18, padding = 10)

save_fig = input("Would you like to save the plot in high resolutions (yes): ")
if save_fig.lower() == 'yes':
    plt.savefig('Sort_v1 comparison.png', dpi = 300, facecolor = 'w', transparent = False, bbox_inches = 'tight')

plt.show()

# %% [markdown]
# # *Other links*
# 
# [Python Objects Nature and Numpy Arrays (Why a copy of array is needed when sorting) | StackOverflow](https://stackoverflow.com/a/3059553/14046889)
# 
# [How to get randomly select n elements from a list using in numpy?](https://stackoverflow.com/a/39563965/14046889)
# 
# [How to switch position of two items in a Python list?](https://stackoverflow.com/questions/2493920/how-to-switch-position-of-two-items-in-a-python-list)
# 
# [Sorting Algorithms](https://www.programiz.com/dsa/sorting-algorithm)


