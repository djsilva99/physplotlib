# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""Contains the class statplot.

Used to make static plots of data stored in csv (or txt) files.

"""

import matplotlib.pyplot as plt
import pylab


class statplot:

    """Plots statically data from csv (or txt) files.

    Loads data from csv (or txt) files, makes simple treatment and plots the
    data in a fast and efficient way, without refreshing constantly while the
    source file is being changed.

    """

    def __init__(self):
        """Initializes the object."""

        self.header = []
        self.data = []
        self.file_name = []
        self.header_saved = None
        self.data_saved = None

    def loadFile(self, file_name, header=True, delim=','):
        """Loads the data from a csv (or txt) file

        filemName: the file name
        header: boolean that tells if the file has a header
        delim: string that indicates the separation of the column

        """

        self.data.append([])
        f = open(file_name, 'r')
        lines = f.readlines()
        self.header.append([])
        number_columns = len(lines[0].split(delim))
        self.file_name.append(file_name)
        if header is True:
            for i in range(len(lines[0].split(delim))):
                self.header[-1].append(lines[0].split(delim)[i])
        lines.pop(0)
        self.data[-1] = [[] for i in range(number_columns)]
        for line in lines:
            for i in range(number_columns):
                self.data[-1][i].append(float(line.split(delim)[i]))
        f.close()

        # loads the initial data if method reset is used afterwards
        self.file_name.append(file_name)
        self.header_saved = self.header[:]
        self.data_saved = self.data[:]

    def loadData(self, header, data, dataName):
        """Loads data from python lists.

        header: matrix saved in self.header
        data: saved in self.data
        dataName: list of names (equivalent of file names)
        """

        self.header.append(header)
        self.data.append(data)
        self.file_name.append(dataName)
        self.header_saved = self.header
        self.data_saved = self.data

    def reset(self):
        """Resets all the data from file_name."""

        self.header = self.header_saved
        self.data = self.data_saved

    def verticalPlot(self, data_index_list, list_x_Column, list_y_Column_list,
                     xtype='lin', ytype='lin', symbol='default', title=None,
                     legenda='default', x_title=None, y_title=None,
                     legend_position='upper right', legend_size=10,
                     x_limits='default', y_limits='default', grid=False,
                     area='default', line='default'):
        """Plots columns.

        Plots each entry of the input list list_y_Column_list[book] as a
        function of the input list list_x_Column[book]. book is defined in
        data_index_list.

        data_index_list: list of the books to be plotted
        list_x_Column: list of X Columns (for each book)
        list_y_Column: list of Y Columns (for each book)
        xtype: x scale mode of the plot
        ytype: y scale mode of the plot
        symbol: list of symbols used in the plot for each book
        title: plot title
        legenda: list of legend with respect to the plotted data
        x_title: x axis title
        y_title: y axis title
        legend_position: position of the legend (given by pyplot)
        legend_size: size of the legend
        grid: set if there is a grid
        area: if not 'default' fills an area of the plot
                [xmin,xmax,ymin,ymax,alpha,color]
        line: if not 'default' creates a line
                [xmin,xmax,ymin,ymax,symbol]
        x_limits: list of 2 element: the first the minimum x value and the
                second the maximum x value to be plotted
        y_limits: list of 2 element: the first the minimum y value and the
                second the maximum y value to be plotted

        """

        if x_title is not None:
            plt.xlabel(x_title)
        if y_title is not None:
            plt.ylabel(y_title)
        if symbol == 'default':
            symbol = ['o-' for i in range(len(data_index_list))]

        # for only one plot
        if len(data_index_list) == 1 and len(list_y_Column_list[0]) == 1:
            plt.title(self.file_name[data_index_list[0]])
            if x_title is None:
                plt.xlabel(self.header[data_index_list[0]][list_x_Column[0]])
            if y_title is None:
                plt.ylabel(self.header[data_index_list[0]]
                           [list_y_Column_list[0][0]])
            plt.plot(self.data[data_index_list[0]][list_x_Column[0]],
                     self.data[data_index_list[0]][list_y_Column_list[0][0]],
                     symbol[0])
            if xtype != 'lin':
                plt.xscale(xtype)
            if ytype != 'lin':
                plt.yscale(ytype)

        # for multiplots
        else:
            if title is not None:
                plt.title(title)

            for k in range(len(data_index_list)):
                j = 0
                for i in list_y_Column_list[k]:
                    if legenda == 'default':
                        index = data_index_list[k]
                        labell = self.file_name[data_index_list[k]] + '::'
                        labell += self.header[index][list_x_Column[k]]
                        labell += '::' + self.header[data_index_list[k]][i]
                    else:
                        labell = legenda[k][j]
                    plt.plot(self.data[data_index_list[k]][list_x_Column[k]],
                             self.data[data_index_list[k]][i], symbol[k],
                             label=labell)
                    j = j + 1
            plt.legend(loc=legend_position, shadow=False,
                       prop={'size': legend_size})
            if xtype != 'lin':
                plt.xscale(xtype)
            if ytype != 'lin':
                plt.yscale(ytype)

        # plotting
        if x_limits != 'default':
            plt.xlim(x_limits)
        if y_limits != 'default':
            plt.ylim(y_limits)
        if area != 'default':
            plt.axvspan(area[0], area[1], ymin=area[2],
                        ymax=area[3], alpha=area[4], color=area[5])
        if line != 'default':
            plt.plot([line[0], line[1]], [line[2], line[3]], line[4])
        plt.grid(grid)
        plt.show()

    def horizontalPlot(self, data_index_list, x_line_list, columns_list,
                       x_line_value='default', x_column='default',
                       symbol='o-', limits='default',
                       xlabel='file column index', ylabel='value',
                       x_shift='default', x_length='default',
                       title='default', legend_position='upper right',
                       legend_size=10, xtype='lin', ytype='lin'):
        """Plots columns.

        Plots the values of lines as a function of column index (or length)

        data_index_list: list of the books to be plotted
        x_line_list: list of lists of the lines to be ploted (for each book).
                If x_line_value is True, x_line_list is the value of the
                x_column.
        columns_list: indicates the range of indexes to be ploted
                (for each data index)
        xtype: x scale mode of the plot
        ytype: y scale mode of the plot
        x_column: list of columns for the x values (for each book)
        symbol: list of symbols used in the plot for each book
        title: plot title
        legend_position: position of the legend (given by pyplot)
        legend_size: size of the legend
        limits: list of 2 element: the first the minimum y value and the
                second the maximum y value to be plotted
        xlabel: name of the x axis
        ylabel: name of the y axis
        x_shift: list of the index correction
        x_length: list of the space step. If default the x axis will only
                show the indexes. If a float number, the x axis will show the
                length accordingly

        """

        if x_line_value == 'default':
            x_line_value = [True for i in range(len(data_index_list))]
        if x_column == 'default':
            x_column = [0 for i in range(len(data_index_list))]
        if x_length == 'default':
            x_length = ['default' for i in range(len(data_index_list))]
        if x_shift == 'default':
            x_shift = [0 for i in range(len(data_index_list))]
        if symbol == 'default':
            symbol = ['o-' for i in range(len(data_index_list))]
        if title != 'default':
            plt.title(title)

        # extracts the needed information for the plotting
        if len(x_line_list) == 1:
            if len(data_index_list) == 1 and len(x_line_list[0]) == 1:
                index = data_index_list[0]
                col = x_column[0]
                title = self.file_name[index] + '\n'
                title += self.header[index][col].split('(')[0]
                value = self.data[index][col][x_line_list[index][0]]
                title += ' (' + str(value) + ' '
                title += self.header[index][col].split('(')[1].split(')')[0]
                title += ')'
            else:
                title = self.file_name[data_index_list[0]]
            plt.title(title)
        for o in range(len(data_index_list)):
            if x_line_value[o] is True:
                templist = []
                for value in x_line_list[o]:
                    for j in self.data[data_index_list[o]][x_column[o]]:
                        if value < j:
                            templist.append(j)
                            break
                x_line_list[o] = templist
                col = x_column[o]
                index = data_index_list[o]
                x_line_list[o] = [self.data[index][col].index(xline)
                                  for xline in x_line_list[o]]
            for k in range(len(x_line_list[o])):
                x = []
                li = []
                for i in range(columns_list[o][0], columns_list[o][1]):
                    x.append(i - x_shift[o])
                    li.append(self.data[data_index_list[o]]
                              [i][x_line_list[o][k]])
                if len(data_index_list) == 1:
                    index = data_index_list[0]
                    col = x_column[0]
                    label = self.header[index][col].split('(')[0]
                    label += ' = '
                    label += str(self.data[index][col][x_line_list[o][k]])
                    label += ' '
                    val = self.header[index][col].split('(')[1].split(')')[0]
                    label += val
                else:
                    index = data_index_list[o]
                    col = x_column[o]
                    label = self.header[index][col].split('(')[0] + ' = '
                    label += str(self.data[index][col][x_line_list[o][k]])
                    val = self.header[index][col].split('(')[1].split(')')[0]
                    label += ' ' + val
                    label += ' (' + self.file_name[o] + ')'
                if x_length[o] != 'default':
                    x = [i * x_length[o] for i in x]
                if len(data_index_list) != 1 or len(x_line_list[o]) != 1:
                    plt.plot(x, li, symbol, label=label)
                else:
                    plt.plot(x, li, symbol)

        # plotting
        plt.legend(loc='upper left', shadow=True)
        if limits != 'default':
            plt.ylim(limits)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        if xtype != 'lin':
            plt.xscale(xtype)
        if ytype != 'lin':
            plt.yscale(ytype)
        plt.legend(loc=legend_position, shadow=False,
                   prop={'size': legend_size})
        plt.show()

    def operation(self, operation, data_to_operate, add_info='default',
                  data_index_list='default'):
        """Makes operations between columns of any book.

        Makes an operation on the data_to_operate, with add_info if required.
        The output goes to data_index_list

                operation: string that indicates the operation
                        'error': calculates the relative error of
                                data_to_operate with respect to
                                add_info (other column).
                data_to_operate: columns to be operated.
                        'error': [[book index x, column index x],
                                [book index y, column index y]]
                add_info: additional information needed for the operation
                        'error': reference x and y columns
                                [[book index x, column index x],
                                [book index y, column index y]]
                data_index_list: book index where the result is stored

        """

        if data_index_list == 'default':
            data_index_list = -1
            self.data.append([])
            self.header.append([])

        # 'error' operator
        if operation == 'error':
            if type(add_info) == type([[1, 2], [3, 4]]):
                header_string = operation + ' (' + str(data_to_operate)
                header_string += ' - ' + str(add_info[0][1])
                self.header[data_index_list].append(header_string)
                header_string = operation + ' (' + str(data_to_operate)
                header_string += ' - ' + str(add_info[1][1])
                self.header[data_index_list].append(header_string)
                self.data[data_index_list].append([])
                self.data[data_index_list].append([])
                data = self.data[data_to_operate[0][0]][data_to_operate[0][1]]
                self.data[data_index_list][-2] = data
                loop = self.data[data_to_operate[0][0]][data_to_operate[0][1]]
                for j in range(len(loop)):
                    ai = add_info
                    ref = pylab.interp(self.data[data_index_list][-2][j],
                                       self.data[ai[0][0]][ai[0][1]],
                                       self.data[ai[1][0]][ai[1][1]])
                    final = (self.data[data_to_operate[1][0]]
                             [data_to_operate[1][1]][j] - ref) / ref
                    self.data[data_index_list][-1].append(final)
            else:
                print 'type of add_info list not correct.'
