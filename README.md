# 🔎 Search and 🗃 Sort Algorithms Analysis

## 🧩 Version Details

1. `Search_v1`: Search for 1 item with time taken details included
2. `Search_v2`: Automated search for all values within array, returning *performance visualisation* between different search algorithms
3. `Sort_v1`: Sort an customise array and return bar chart visualisation
4. `Sort_v2`: Sort an array with the minimum length of 1 to the specified maximum array length

## 📍 Requirements

### 🉑 Language

<img src="./Others/python.png" alt="Windows icon" width=15> **Python 3.6** or above

> `python` or `python3` in terminal to check the version

### 📦 Libraries

#### Installation

- <img src="./Others/windows.png" alt="Windows icon" width=15> Windows only: Execute [`start.bat`][batch]

- Manually through system terminal with `pip install package` (e.g. *`pip install pandas`*)

#### Usages

| | [numpy](https://numpy.org/doc/stable/index.html) | [ipython](https://ipython.readthedocs.io/en/stable/) | [matplotlib](https://matplotlib.org/stable/index.html) | [pandas](https://pandas.pydata.org/pandas-docs/stable/index.html)
--- | :---: | :---: | :---: | :---:
**Search_v1** | 🟢 | 🟢 | ⚪ | ⚪
**Search_v2** | 🟢 | 🟢 | 🟢 | 🟢
**Sort_v1** | 🟢 | 🟢 | 🟢 | ⚪
**Sort_v2** | 🟢 | 🟢 | 🟢 | ⚪

## 🗝 Operation

1. `.ipynb` is the **recommended** format, to be used in environments that allow Jupyter Notebook execution

2. `.py`

    - Direct execution through `python` or `python3`

    - Execute [`start.bat`][batch] and select version.
    > Batch script `start.bat` is case sensitive

[batch]: start.bat

## 📥 Download

Check [releases](https://github.com/MinkDang/Search-and-Sort-Analysis/releases) for more details

1. Python: [`.zip`](https://github.com/MinkDang/Search-and-Sort-Analysis/releases/download/v1.0_Python/Search.and.Sort.Analysis.Python.zip)

2. Jupyter Notebooks: [`.zip`](https://github.com/MinkDang/Search-and-Sort-Analysis/releases/download/v1.0_Jupyter-Notebook/Search.and.Sort.Analysis.Jupyter.Notebooks.zip)
---

## ⏳ Performance

### ⚠ Warning

**Linear** Search is not time-efficient, adjust the parameters wisely

**Sorting** is not time-efficient, adjust the parameters wisely

- **Bubble sort (*Unoptimized*)** -- 4 times longer than *Insertion Sort*
- **Bubble sort (*Optimized*)** -- 2 times longer than *Insertion Sort*
- In `Sort_v2`, the recommend **upper limit** is **1000** as higher parameters would led to long execution time, ~~*turning your computer into a jet engine*~~ slowing other processes within your computer

### 💊 Testing

| **File** | Search_v1 | Search_v2 | Sort_v1 | Sort_v2 |
|---|---|---|---|---|
| **Demo** | [Deepnote](https://deepnote.com/project/Search-and-Sort-Analysis-eUaFHUuuT5acWy-01VhYnA/%2FSearch_v1.ipynb) | [Deepnote](https://deepnote.com/project/Search-and-Sort-Analysis-eUaFHUuuT5acWy-01VhYnA/%2FSearch_v2.ipynb) | [Deepnote](https://deepnote.com/project/Search-and-Sort-Analysis-eUaFHUuuT5acWy-01VhYnA/%2FSort_v1.ipynb) | [Deepnote](https://deepnote.com/project/Search-and-Sort-Analysis-eUaFHUuuT5acWy-01VhYnA/%2FSort_v2.ipynb) |
| **Execution time (Demo)** | < 1 min | 40 min | 70 min | 12.5 hours |
| **Notes** | Duplicates: 4884</br>Values Remain: 95116</br>Seed: 1</br>Number: 3620 | Duplicates: 4733 </br> Values Remain: 95267 </br> Seed: 1698699006 | Seed: 1440114639 </br> Array Length: 41001 | Seed: 1355045386 </br> Upper Limit: 5000 |

---

## 📊 Graphs

### [`Search_v2`](./Graphs/Search%20Comparison.png)

![Binary vs Linear Search](./Graphs/Search%20Comparison.png)

### [`Sort_v1`](./Graphs/Sort_v1%20comparison.png)

![41001 Array Sorting Performance](./Graphs/Sort_v1%20comparison.png)

### [`Sort_v2`](./Graphs/Sort_v2%20comparison.png)

![Different Sorting Algorithms' Performance](./Graphs/Sort_v2%20comparison.png)

## 📎 Other Links

### **Preview or run services** for Jupyter Notebook

[Deepnote](https://deepnote.com/), [Replit](https://replit.com/), [Datalore (from JetBrains)](https://datalore.jetbrains.com/), [Google Colab](https://colab.research.google.com/), [Binder](https://mybinder.org/)

More sites here [StackOverflow Answer](https://stackoverflow.com/a/48501883/14046889)

### Visual Studio Code useful links

- [Visual Studio Code Download](https://code.visualstudio.com/)
- [Data Science in Visual Studio Code (Extensions links included)](https://code.visualstudio.com/docs/datascience/overview)
- [Jupyter Notebooks in VS Code](https://code.visualstudio.com/docs/datascience/jupyter-notebooks)
- [Data Science in VS Code tutorial](https://code.visualstudio.com/docs/datascience/data-science-tutorial)
- [Python Interactive window](https://code.visualstudio.com/docs/python/jupyter-support-py)

### Jupyter Notebook website

<https://jupyter.org/>
