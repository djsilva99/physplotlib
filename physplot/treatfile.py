# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""Contains the class treatfile

Used to make simple operation with csv (or txt) files before plotting
or converting into other csv (or txt) files

"""


class treatfile:

    """Load and treat data from csv (or txt) files

    Load data from txt files, filter the values that comes after a given
    string and makes some operations, before exporting the data back or
    plotting with staticplot class.

    """

    def __init__(self, file_name, filter):
        """Initializes the object.

        filem_name: file name
        filter: list of 2 string lists to use in the filter:
                strings before and after the desired value.
                The second string can be neglected

        """

        # loads the data
        f = open(file_name, 'r')
        lines = f.readlines()
        f.close()

        # first data filter
        self.data = [[] for i in range(len(filter))]
        i = 0
        for j in range(len(filter)):
            for line in lines:
                splitLine = line.split(filter[j][0])
                if len(splitLine) != 1:
                    if len(filter[j]) == 1:
                        try:
                            self.data[i].append(float(splitLine[1]))
                        except ValueError:
                            self.data[i].append(splitLine[1])
                    else:
                        try:
                            self.data[i].append(
                                float(splitLine[1].split(filter[j][1])[0]))
                        except ValueError:
                            self.data[i].append(
                                splitLine[1].split(filter[j][1])[0])
            i = i + 1

        # other important definitions
        self.file_name = file_name
        self.header = [name[0] for name in filter]

        # saves original self variables
        self.data_saved = self.data[:]
        self.header_saved = self.header[:]

    def filter(self, column, values):
        """Filters the data with the values (list) in column

        column: column to be filtered for the values in the values list
        values: list of values used for the filter

        """

        newData = [[] for i in range(len(self.data))]
        for i in range(len(self.data[column])):
            if self.data[column][i] in values:
                for j in range(len(self.data)):
                    newData[j].append(self.data[j][i])
        self.data = newData

    def reset(self):
        """Resets all treated data"""

        self.data = self.data_saved
        self.header = self.header_saved

    def removeColumn(self, column):
        """Removes column from self.data"""

        self.header.pop(column)
        self.data.pop(column)

    def removeLine(self, line):
        """Removes line from all columns"""

        for i in range(len(self.data)):
            self.data[i].pop(line)

    def calculate(self, column, operation, add_info='default'):
        """Makes an operation into a column.

        Creates a new column with the data from column treated with operation,
        and additional information if required.

        column: column where the operation is applied
        operation: string that indicated the operation:
                'H:M:S to sec': converts time format H:M:S to seconds
                'error': calculates the error of a column with respect to a
                        reference column
        add_info: additional information:
                        'error': reference column index
        """

        # converts time format H:M:S to seconds
        if operation == 'H:M:S to sec':

            self.data.append([])
            for i in self.data[column]:
                H, M, S = i.split(':')
                H = float(H)
                M = float(M)
                S = float(S)
                self.data[-1].append(3600 * H + 60 * M + S)
            self.header.append(self.header[column] + ' (' + operation + ')')

        # calculates the error of a column with respect to column info
        if operation == 'error':
            if type(add_info) == type(1):
                self.data.append([])
                i = 0
                for value in self.data[column]:
                    final = (self.data[column][i] -
                             self.data[add_info]) / self.data[column][i]
                    self.data[-1].append(final)
                    i = i + 1
                header_string = ' column/reference: '
                operation = operation + header_string, column, '/', add_info
                self.header.append(
                    self.header[column] + ' (' + operation + ')')
            else:
                print 'type of add_info list not correct.'

    def saveFile(self, file_name, delim=','):
        """Saves the data into a file

        file_name: file name where data is saved
        delim: separation string between entries
        """

        f = open(file_name, 'wt')
        for i in range(len(self.header)):
            if i != 0:
                f.write(delim)
            f.write(self.header[i])
        f.write('\n')

        for j in range(len(self.data[0])):
            for i in range(len(self.data)):
                if i != 0:
                    f.write(delim)
                f.write(str(self.data[i][j]))
            f.write('\n')
        f.close()
