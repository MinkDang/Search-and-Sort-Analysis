# 🔎 Search and 🗃 Sort Algorithms Analysis

## 🧩 Version Details

1. `Search_v1`: Search for 1 item with time taken details included
2. `Search_v2`: Automated search for all values within array, returning *performance visualisation* between different search algorithms

## 📍 Requirements

### 🛠 Language: **Python 3.6** or above

### 📦 Libraries:

These can be installed through running the `start.bat` file **(Windows only)**

Install manually through your system terminal through `pip install package` *(e.g: `pip install pandas`)*

* numpy
* ipython
* pandas *(Not used in version 1)*
* matplotlib *(Not used in version 1)*

## 🗝 Operation

1. `.ipynb` is a **recommended** format, to be used in environments that allow Jupyter Notebook execution

2. `.py` can be executed by running `start.bat` file or from your system terminal

> What VERSION are you running (1 or 2)?

Possible input
* `1` for `Search_v1.py`
* `2` for `Search_v2.py`

---

## ⏳ Performance notes

    Please note that LINEAR search will consume much more performance and time than BINARY search

### Testing specs:

Computer

* CPU: Intel(R) Core(TM) i5-1035G1 CPU @ 1.00GHz, 1190 Mhz, 4 Core(s), 8 Logical Processor(s)
* RAM: 16GB
* CPU Usage: 50% by `python.exe`

Data setup

* Seed: 1
* Min: 1
* Max: 1,000,000
* Array length before duplication removal: 100,000

**Result**:

* Binary Search: 2 seconds
* Linear Search - *Sorted*, Linear Search - *Unsorted*: 4 minutes each → 8 minutes in total
* Graphing - 5 to 10 seconds

---

## 📎 Other Links

### __Online cloud computing service__ for Jupyter Notebook

* [Deepnote](https://deepnote.com/)
* [Replit](https://replit.com/)
* [Datalore (from JetBrains)](https://datalore.jetbrains.com/)
* [Google Colab](https://colab.research.google.com/)
* [Binder](https://mybinder.org/)

Performance are limited unless paid versions are in used

### Jupyter Notebook website

<https://mybinder.org/>

### Visual Studio Code useful links

* [Visual Studio Code Download](https://code.visualstudio.com/)
* [Data Science in Visual Studio Code (Extensions links included)](https://code.visualstudio.com/docs/datascience/overview)
* [Jupyter Notebooks in VS Code](https://code.visualstudio.com/docs/datascience/jupyter-notebooks)
* [Data Science in VS Code tutorial](https://code.visualstudio.com/docs/datascience/data-science-tutorial)
* [Python Interactive window](https://code.visualstudio.com/docs/python/jupyter-support-py)

### Documentations

* [matplotlib](https://matplotlib.org/stable/index.html)
* [pandas](https://pandas.pydata.org/pandas-docs/stable/index.html)
* [numpy](https://numpy.org/doc/stable/index.html)
* [jupyter](https://jupyter.readthedocs.io/en/latest/)