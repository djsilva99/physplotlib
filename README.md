# physplot

The physplot class allows one to load data from txt files, make simple treatment and plot the data in a fast and efficient way. This program is usefull when handling with output files from numerical simulations in a quick way or if one wants to make a quick plot from txt files to watch the content. This project is dynamic, i.e. is being modified to fulfill needs without defined periodicity. Below are the attributes and methods of physplot.

attributes:

self.header -> saves the data of the first line pointed out in in initialization
self.numberColumns -> saves the number of columns present in the object
self.data -> saves all the values present in the file. each entry corresponds to one line, Each entry is a list of
	values corresponding to each column

methods:

removePeriodicPoints -> allows to remove periodic points for specific columns.
singlePlot -> plots the columnY as a function of columnX
reset
average
save
removeValues
plotHist


Example: