# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""Contains the class dyplot.

Used to make dynamic plots of data stored in csv (or txt) files.

"""

import matplotlib.pyplot as plt
import matplotlib.animation as animation


class dyplot:

    """Plots dynamically data from csv (or txt) files.

    Loads data from csv (or txt) files, refreshing the plot constantly
    while the source file is being changed.

    """

    def __init__(self, fileName, header=True, delim=','):
        """Initializes the object.

        filemName: file name
        header: boolean that tells if the file has a header
        delim: string that indicates the separation of the column

        """

        self.delim = delim
        self.fig = None
        self.xColumn = None
        self.yColumnsList = []
        self.fileName = fileName
        self.initialValue = None
        self.finalValue = None
        self.ax1 = None
        self.headerState = header
        f = open(fileName, 'r')
        lines = f.readlines()
        f.close()
        self.header = []
        if header is True:
            for i in range(len(lines[0].split(delim))):
                self.header.append(lines[0].split(delim)[i])

    def animateVertical(self, i):
        """Blind method.

        Used to make vertical plots when verticalPlot method
        is called.

        """

        graph_data = open(self.fileName, 'r').read()
        lines = graph_data.split('\n')
        if self.headerState is True:
            lines = lines[1:]
        xs = []
        li = []
        for i in self.yColumnsList:
            li.append([])
        for line in lines:
            if len(line) > 1:
                lineArray = line.split(self.delim)
                xs.append(lineArray[self.xColumn])
                for i in range(len(self.yColumnsList)):
                    li[i].append(float(lineArray[self.yColumnsList[i]]))
        self.ax1.clear()
        for i in range(len(self.yColumnsList)):
            string = str(self.header[self.yColumnsList[i]])
            self.ax1.plot(xs, li[i], 'o-', label=string)
            self.ax1.axes.set_xlabel(self.header[self.xColumn])
        self.ax1.legend(loc='upper left', shadow=True)

    def animateHorizontal(self, i):
        """Blind method.

        Used to make horizontal plots when horizontalPlot method
        is called

        """

        graph_data = open(self.fileName, 'r').read()
        lines = graph_data.split('\n')
        if self.headerState is True:
            lines = lines[1:]
        xs = [
            j + self.xShift for j in range(self.initialValue, self.finalValue)]
        if self.xLength != 'default':
            xs = [x * self.xLength for x in xs]
        li = lines[-2].split(self.delim)
        li = [float(lis) for lis in li]
        if self.xColumn != 'default':
            title = self.fileName + '\n'
            title += self.header[self.xColumn].split('(')[0] + ' = '
            title += str(li[self.xColumn]) + ' '
            title += self.header[self.xColumn].split('(')[1].split(')')[0]
        for i in range(self.initialValue):
            li.pop(0)
        for i in range(len(li) - (self.finalValue - self.initialValue)):
            li.pop()
        self.ax1.clear()
        if self.limits != 'default':
            self.ax1.axes.set_ylim(self.limits)
        self.ax1.plot(xs, li, self.symbol, label='temp')
        self.ax1.set_xlim([min(xs), max(xs)])
        self.ax1.set_xlabel(self.xlabel)
        self.ax1.set_ylabel(self.ylabel)
        if self.xColumn != 'default':
            self.ax1.set_title(title)

    def verticalPlot(self, xColumn, yColumnsList, timeInterval=1000):
        """Plots columns.

        Plots each entry of the input list yColumnList as a
        function of the input list xColumn time interval is the refreshing
        time step in milliseconds.

        xColumn: column index of the x data
        yColumnList: column index list of the y data
        timeInterval: refresh time in milliseconds

        """

        self.fig = plt.figure()
        self.ax1 = self.fig.add_subplot(1, 1, 1)
        self.xColumn = None
        self.yColumnsList = []
        self.xColumn = xColumn
        self.yColumnsList = yColumnsList
        ani = animation.FuncAnimation(
            self.fig, self.animateVertical, interval=timeInterval)
        plt.show(block=False)

    def horizontalPlot(self, columns, xColumn='default', limits='default',
                       xShift=0, xLength='default', xlabel='file column index',
                       ylabel='value', timeInterval=1000, symbol='o-'):
        """Plots lines.

        Plots the values of the last line of the file as a
        function of column index.

        columns: list that indicates the range of indexes to be plotted
        timeInterval: refresh time in milliseconds
        symbol: matplotlib symbol of the plot
        xlabel: name of the x axis
        ylabel: name of the y axis
        limits: list of length = 2 that indicates the limits of the y scale
        xShift: int value that indicates the correction of the index
        xLength: space step. If equal to 'default' the x axis will only show
            the indexes. If a float number, the x axis will show the length
            accordingly
        """

        self.symbol = symbol
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.xShift = xShift
        self.xLength = xLength
        self.limits = limits
        self.fig = plt.figure()
        self.ax1 = self.fig.add_subplot(1, 1, 1)
        self.xColumn = xColumn
        self.yColumnsList = []
        self.initialValue = columns[0]
        self.finalValue = columns[1]
        ani = animation.FuncAnimation(
            self.fig, self.animateHorizontal, interval=timeInterval)
        plt.show()
