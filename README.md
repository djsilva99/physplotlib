# physplotlib

<img src="https://github.com/danieljosesilva/physplotlib/blob/master/img/physplotlib.png" alt="Drawing" height="40"/> physplotlib v0.1.2

physplotlib is a python2.7 library for plotting data. It loads data from text files, makes simple treatments and plots data in a very simple manner. physplotlib is useful when handling with output files from numerical simulations or to plot quickly data from text files. 

author: Daniel Silva (djsilva99@gmail.com) <br> current version: v0.1.2

![physplotlib-screenshot](https://github.com/danieljosesilva/physplotlib/blob/master/img/physplotlib.gif)


## Table of contents

1. [Installation](#instalation)
2. [Introduction](#introduction)
3. [treatfile class](#treatfile)
    1. [filter](#treatfile-filter)
    2. [compute](#treatfile-compute)
    3. [save to file](#treatfile-savefile)
4. [statplot class](#statplot)
    1. [load file](#statplot-loadfile)
    2. [load data](#statplot-loaddata)
    3. [reset](#statplot-reset)
    4. [vertical plot](#statplot-verticalplot)
    5. [horizontal plot](#statplot-horizontalplot)
    6. [operation](#statplot-operation)
5. [dyplot class](#dyplot)
    1. [vertical plot](#dyplot-verticalplot)
    2. [horizontal plot](#dyplot-horizontalplot)


## 1. Instalation <a name="instalation"></a>

To install use the pip package manager:

```bash
$ pip install physplotlib
```

To import the physplotlib module type in the python shell:

```python
>>> import physplotlib as pp
```

From this point on use the prefix pp. before any object creation


## 2. Introduction <a name="introduction"></a>

The physplotlib library contains classes to load data from csv (or txt) files, to make operations between columns or lines, and to plot the respective treated data. It uses the library matplotlib and is intended to be used by engineers and scientists, who need to make plots quickly after obtaining data. In particular, it is intended for people handling with output files from numerical simulations, e.g. for the visualization of the output data that is generated by the <a href='https://github.com/danieljosesilva/heatrapy'>heatrapy</a> package. The module relies on 3 classes:

**treatfile**

This class loads and treats the data with filters and operations. It can extract relevant information from log files, which can be stored afterwards in a file or used by statplot class to plot the resulting information.

**statplot**

This class loads data from csv (or txt) files or from previously treated data, e.g. with the treatfile class, and plots the data in a personalized, but simple, manner. statplot is appropriate to be used in logbooks, such as jupyter notebook.

**dyplot**

This class loads data from a given file and makes dynamic plots. dyplot is appropriate to be used during a simulation, or during data acquisition. 


## 3. treatfile class <a name="treatfile"></a>

treatfile can be used to make simple operations with csv (or txt) files before plotting or converting into other csv (or txt) files. It loads data from txt files, filters the values that comes after a given string and makes some operations, before exporting the data back or plotting with the `staticplot` class. To initialize the object type

```python
>>> foo = pp.treatfile(file_name, filter)
```

where `file_name` is the url of the text file to be treated, and `filter` is a list. Each entry of `filter` is a 2 string list where the first element corresponds to the string before the value to be filtered and the second element corresponds to the string after the value to be filtered. The default value for the second string is '\n' and thus can be neglected. This initialization will load the data into `foo.data`, which has a dimension of `len(<filter>)`. Each element of `foo.data` is a list of filtered data. This initialization also loads the file_name into `foo.file_name`, and the header into `foo.header`, which is a list of the string labels of `foo.data`. 

### i. filter <a name="treatfile-filter"></a>

To filter the data from `foo.data`, use the filter method:

```python
>>> foo.filter(column, values)
```

where `values` is a list of values used for the filter, and `column` is the column to be filtered for the values in the `values` list.

### ii. compute <a name="treatfile-compute"></a>

To compute the entries of the `foo.data` use the calculate method:

```python
>>> foo.calculate(column, operation, add_info='default')
```

where `column` is the integer referring to the column to operate. `operation` is a string that identifies the operation, and can have the following values:

* `'H:M:S to sec'` which converts the entries with format H:M:S into a float number (seconds)
* `'error'` which calculates the error of a column with respect to the column given in the input variable `add_info`.

### iii. save to file <a name="treatfile-savefile"></a>

To save the data into a file use the saveFile method:

```python
>>> foo.saveFile(file_name, delim=',')
```

where `file_name` is the url of the text file to be saved, and `delim` is a string with the delimitation between columns. The default value is ','.


## 4. statplot class <a name="statplot"></a>

statplot can be used to make static plots of data stored in csv (or txt) files. It loads data, makes simple treatment and plots the data in a simple manner, without refreshing constantly while the source file is being changed. To initialize the object type

```python
>>> foo = pp.statplot()
```

This initialization creates the `foo.data` variable, which is a list of books. Each entry of a book list corresponds to different loaded data. The initialization also creates the `foo.header` variable, which is a list of headers for the books, and `foo.file_name`, which is a list that indicates the origin of the data (loaded file or loaded values). 


### i. load file <a name="statplot-loadfile"></a>

To load data from a file type

```python
>>> foo.loadFile(file_name, header=True, delim=',')
```

where `file_name` is the url of the text file to be loaded, `header` is a boolean that indicates if the file has a header, and `delim` is a string that defines the separation of the column. Note that loading a file does not remove existing data but appends the new data.


### ii. load data <a name="statplot-loaddata"></a>

To load the whole data from python variables type

```python
>>> foo.loadFile(header, data, dataName)
```
where `header` is a list for the `foo.header` value, `data` is the value for `foo.data`, and `dataName` is the value for `foo.file_name` (equivalent of file names).

### iii. reset <a name="statplot-reset"></a>

To remove all the data from the `foo` object type

```python
>>> foo.reset()
```


### iv. vertical plot <a name="statplot-verticalplot"></a>

To plot each entry of a column from a book type

```python
>>> foo.verticalPlot(data_index_list, list_x_Column, list_y_Column_list,
...                  xtype='lin', ytype='lin', symbol='default', title=None,
...                  legenda='default', x_title=None, y_title=None,
...                  legend_position='upper right', legend_size=10,
...                  x_limits='default', y_limits='default', grid=False,
...                  area='default', line='default')
```

This command plots the data using matplotlib.pyplot, with the input variables that are listed below:

* `data_index_list`: list of the books to be plotted
* `list_x_Column`: list of X Columns to be plotted (for each book)
* `list_y_Column`: list of Y Columns to be plotted (for each book)
* `xtype`: x scale mode
* `ytype`: y scale mode
* `symbol`: list of symbols used for each book
* `title`: plot title
* `legenda`: list of labels with respect to the plotted data
* `x_title`: x axis title
* `y_title`: y axis title
* `legend_position`: position of the labels (given by matplotlib.pyplot)
* `legend_size`: size of the labels
* `grid`: boolean that indicates if there is a grid
* `area`: if not 'default' fills an area of the plot [xmin,xmax,ymin,ymax,alpha,color]
* `line`: if not 'default' creates a line [xmin,xmax,ymin,ymax,symbol]
* `x_limits`: list of 2 element: the first is the minimum x value and the second is the maximum x value
* `y_limits`: list of 2 element: the first is the minimum y value and the second is the maximum y value


### v. horizontal plot <a name="statplot-horizontalplot"></a>

To plot each entry of a row from a book type

```python
>>> foo.horizontalPlot(data_index_list, x_line_list, columns_list,
...                    x_line_value='default', x_column='default',
...                    symbol='o-', limits='default',
...                    xlabel='file column index', ylabel='value',
...                    x_shift='default', x_length='default',
...                    title='default', legend_position='upper right',
...                    legend_size=10, xtype='lin', ytype='lin')
```

This method plots the data using matplotlib.pyplot, with the input variables that are listed below:

* `data_index_list`: list of the books to be plotted
* `x_line_list`: list of lists of the lines to be plotted (for each book). If x_line_value is True, x_line_list is the value of the x_column.
* `columns_list`: defines the range of indexes to be plotted (for each data index)
* `xtype`: x scale mode
* `ytype`: y scale mode
* `x_column`: list of columns for the x values (for each book)
* `symbol`: list of symbols used in the plot for each book
* `title`: plot title
* `legend_position`: position of the labels (given by pyplot)
* `legend_size`: size of the labels
* `limits`: list of 2 element: the first is the minimum y value and the second is the maximum y value
* `xlabel`: name of the x axis
* `ylabel`: name of the y axis
* `x_shift`: list of the index correction
* `x_length`: list of the space step. If 'default' the x axis is shows the indexes. If a float number, the x axis will show the length accordingly


### vi. operation <a name="statplot-operation"></a>

To realize operations between columns of any stored book in `foo.data` type

```python
>>> object.operation(operation, data_to_operate, add_info='default',
...                  data_index_list='default'):
```

This method computes that data according to the input variables listed below:

* `operation`: string that indicates the operation 
  * 'error': calculates the relative error of `data_to_operate` with respect to `add_info` (other column).
* `data_to_operate`: columns to be operated.
  * 'error': [[book index x, column index x], [book index y, column index y]]
* `add_info`: additional information needed for the operation
  * 'error': references x and y columns [[book index x, column index x], [book index y, column index y]]
* `data_index_list`: book index where the result is stored



## 5. dyplot class <a name="dyplot"></a>

dyplot can be used to plot the data from csv (or txt) files, refreshing the plot constantly while the source file is being changed, i.e. plots dynamically.

To initialize the object type

```python
>>> foo = pp.dyplot(file_name, header=True, delim=',')
```

where `file_name` is the url of the file to be loaded. ,`header:` is a boolean that tells if the file has a header, and `delim` is a string that defines the separation of the column.


### i. vertical plot <a name="dyplot-verticalplot"></a>

To plot columns type

```python
>>> foo.verticalPlot(x_column, y_columns_list, time_interval=1000)
```

where `x_column` is column index of the x data, `yColumnList` is column index list of the y data, and `time_interval` is the refresh time in milliseconds. This method plots each entry of the input list `y_column_list` as a function of the input list `xColumn`.


### ii. horizontal plot <a name="dyplot-horizontalplot"></a>

To plot rows type

```python
>>> foo.horizontalPlot(columns, x_column='default', limits='default',
...                    x_shift=0, x_length='default', xlabel='file column index',
...                    ylabel='value', time_interval=1000, symbol='o-')
```
This method plots the values of the last line of the file as a function of column index, with the following input variables.

* `columns`: list that defines the range of indexes to be plotted
* `time_interval`: refresh time in milliseconds
* `symbol`: matplotlib symbol
* `xlabel`: name of the x axis
* `ylabel`: name of the y axis
* `limits`: list of length = 2 that defines the limits of the y scale
* `x_shift`: int value that defines the correction of the index
* `x_length`: space step. If equal to 'default' the x axis only shows the indexes. If equal to a floating number, the x axis will show the length accordingly