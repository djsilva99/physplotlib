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

    def __init__(self, file_name, header=True, delim=','):
        """Initializes the object.

        filemName: file name
        header: boolean that tells if the file has a header
        delim: string that indicates the separation of the column

        """

        self.delim = delim
        self.fig = None
        self.x_column = None
        self.y_columns_list = []
        self.file_name = file_name
        self.initial_value = None
        self.final_value = None
        self.ax1 = None
        self.header_state = header
        f = open(file_name, 'r')
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

        graph_data = open(self.file_name, 'r').read()
        lines = graph_data.split('\n')
        if self.header_state is True:
            lines = lines[1:]
        xs = []
        li = []
        for i in self.y_columns_list:
            li.append([])
        for line in lines:
            if len(line) > 1:
                line_array = line.split(self.delim)
                xs.append(line_array[self.x_column])
                for i in range(len(self.y_columns_list)):
                    li[i].append(float(line_array[self.y_columns_list[i]]))
        self.ax1.clear()
        for i in range(len(self.y_columns_list)):
            string = str(self.header[self.y_columns_list[i]])
            self.ax1.plot(xs, li[i], 'o-', label=string)
            self.ax1.axes.set_xlabel(self.header[self.x_column])
        self.ax1.legend(loc='upper left', shadow=True)

    def animateHorizontal(self, i):
        """Blind method.

        Used to make horizontal plots when horizontalPlot method
        is called

        """

        graph_data = open(self.file_name, 'r').read()
        lines = graph_data.split('\n')
        if self.header_state is True:
            lines = lines[1:]
        xs = [
            j + self.x_shift for j in range(self.initial_value, self.final_value)]
        if self.x_length != 'default':
            xs = [x * self.x_length for x in xs]
        li = lines[-2].split(self.delim)
        li = [float(lis) for lis in li]
        if self.x_column != 'default':
            title = self.file_name + '\n'
            title += self.header[self.x_column].split('(')[0] + ' = '
            title += str(li[self.x_column]) + ' '
            title += self.header[self.x_column].split('(')[1].split(')')[0]
        for i in range(self.initial_value):
            li.pop(0)
        for i in range(len(li) - (self.final_value - self.initial_value)):
            li.pop()
        self.ax1.clear()
        if self.limits != 'default':
            self.ax1.axes.set_ylim(self.limits)
        self.ax1.plot(xs, li, self.symbol, label='temp')
        self.ax1.set_xlim([min(xs), max(xs)])
        self.ax1.set_xlabel(self.xlabel)
        self.ax1.set_ylabel(self.ylabel)
        if self.x_column != 'default':
            self.ax1.set_title(title)

    def verticalPlot(self, x_column, y_columns_list, time_interval=1000):
        """Plots columns.

        Plots each entry of the input list yColumnList as a
        function of the input list x_column time interval is the refreshing
        time step in milliseconds.

        x_column: column index of the x data
        yColumnList: column index list of the y data
        time_interval: refresh time in milliseconds

        """

        self.fig = plt.figure()
        self.ax1 = self.fig.add_subplot(1, 1, 1)
        self.x_column = None
        self.y_columns_list = []
        self.x_column = x_column
        self.y_columns_list = y_columns_list
        ani = animation.FuncAnimation(
            self.fig, self.animateVertical, interval=time_interval)
        plt.show(block=False)

    def horizontalPlot(self, columns, x_column='default', limits='default',
                       x_shift=0, x_length='default', xlabel='file column index',
                       ylabel='value', time_interval=1000, symbol='o-'):
        """Plots lines.

        Plots the values of the last line of the file as a
        function of column index.

        columns: list that indicates the range of indexes to be plotted
        time_interval: refresh time in milliseconds
        symbol: matplotlib symbol of the plot
        xlabel: name of the x axis
        ylabel: name of the y axis
        limits: list of length = 2 that indicates the limits of the y scale
        x_shift: int value that indicates the correction of the index
        x_length: space step. If equal to 'default' the x axis will only show
            the indexes. If a float number, the x axis will show the length
            accordingly
        """

        self.symbol = symbol
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.x_shift = x_shift
        self.x_length = x_length
        self.limits = limits
        self.fig = plt.figure()
        self.ax1 = self.fig.add_subplot(1, 1, 1)
        self.x_column = x_column
        self.y_columns_list = []
        self.initial_value = columns[0]
        self.final_value = columns[1]
        ani = animation.FuncAnimation(
            self.fig, self.animateHorizontal, interval=time_interval)
        plt.show()
