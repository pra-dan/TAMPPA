# TAMPPA: Time And Memory Profile PArser

---
> As a maiden attampt, I hope to make it super useful for the community. Please report bugs and make pull requests to improve it.
---

## Introduction:

TAMPPA is a supporting package for the popular profilers
* [line_profiler and kernprof](https://github.com/pyutils/line_profiler/blob/master/README.rst), and
* [memory_profiler](https://github.com/pythonprofilers/memory_profiler)

Both the packages do an excellent job by providing profiling results on the terminal.

```python3
Total time: 0.181071 s
File: main.py
Function: linearRegressionfit at line 35

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    35                                           @profile
    36                                           def linearRegressionfit(Xt,Yt,Xts,Yts):
    37         1         52.0     52.0      0.1      lr=LinearRegression()
    38         1      28942.0  28942.0     75.2      model=lr.fit(Xt,Yt)
    39         1       1347.0   1347.0      3.5      predict=lr.predict(Xts)
    40                                           
    41         1       4924.0   4924.0     12.8      print("train Accuracy",lr.score(Xt,Yt))
    42         1       3242.0   3242.0      8.4      print("test Accuracy",lr.score(Xts,Yts))
```

But, there seems to be no method to get these stats in a exportable file that can be used with flexibility. 

On dumping the logs to a `.txt` file still requires an individual to parse data from the text by self and then convert the content into a `.csv` file; which is a common format for sharing statistical data and plotting using MATPLOTLIB. 

This is exactly what **TAMPPA** does ! It outputs one `.csv` file per function and another text file `func_names.txt` and `again_func_names.txt` for accessing these files easily.

## Pre-requisites:
**Note: Both the parsers need a .txt file to parse results from**

* Run both the profilers or the profiler whose results you need as a `csv`, and save the logs on the console to a `.txt` file. For e.g saving the memory profiling results of the python application `mainm.py` and saving the results to `mem_res_1.txt`

```python3
$ python -m memory_profiler mainm.py > mem_res_1.txt
```

*   Avoid printing anything on the console. Try it with `python main.py` and nothing should be printed to the console. So, comment out all the print and log statements.

## Installation
Any particular release can be installed using `pip`:
```python3
$ pip install tamppa
```

To enter development mode,
```python3
$ git clone https://github.com/pra-dan/TAMPPA.git
```
## Usage
Refer to the following once the Installation is over.

### Time Profile Parser
Initially, if we have only the `.txt` file.
```python3
.
└── tim_prof_results.txt
0 directories, 1 file
```

Run `tim_parse` or time parser, in a Python environment (`$ python`)
```python3
>>> from tamppa import tim_parse
>>> tim_parse("tim_prof_results.txt")
```

On successful execution, the lonely directory is populated as
```python3
.
├── again_func_names.txt
├── import_data_tim_.csv
├── linearRegressionfit_tim_.csv
├── parse_data_tim_.csv
├── randForestRegressorfit_tim_.csv
└── tim_prof_results.txt

0 directories, 6 files
```

Additionally, a plot is also generated as
![mem_res](https://github.com/pra-dan/TAMPPA/blob/master/resources/tim_res.png)

### Memory Profile Parser
Similarly, if we have only the `.txt` file for the `memory_profiler`.
```python3
.
└── mem_res_1.txt

0 directories, 1 file
```

Run `mem_parse` or time parser, in a Python environment (`$ python`)
```python3
>>> from tamppa import mem_parse
>>> mem_parse("mem_res_1.txt")
```

On successful execution, the lonely directory is populated as
```python3
.
├── func_names.txt
├── function_wise_time_results.csv
├── import_data_mem_.csv
├── linearRegressionfit_mem_.csv
├── mem_res_1.txt
├── parse_data_mem_.csv
└── randForestRegressorfit_mem_.csv

0 directories, 7 files
```

Additionally, a plot is also generated as
![mem_res](https://github.com/pra-dan/TAMPPA/blob/master/resources/mem_res.png)

## TODOs:
- [ ] (Provide the entire package a executable-like interface; such that the parsers can be called simply as `$ mem_parse file.txt -plot true`)

- [ ] (Add flags to toggle plots for both parsers)


## References:

* [Packaging Python Projects](https://packaging.python.org/tutorials/packaging-projects/)

* [Jacob Tomlinson's Blogs](https://www.jacobtomlinson.co.uk/series/creating-an-open-source-python-project-from-scratch/)
