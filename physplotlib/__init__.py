# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""Physplot.

This module contains classes to load data from csv (or txt) files, make
operations between columns or lines, and plot the respective treated
data. It uses the library matplotlib and is intended to be used by
engineers and scientists, who need to make plots quickly after obtaiing
the data.

The module relies on 3 classes:

#########
treatfile
#########

This class loads and treats the data with filters and operations. This
classe is builts to extract relevant information from log files, which
can be afterwards stored in a file or used by statplot class to plot
the resulting information.

#########
statplot
#########

This class loads data from csv (or txt) files or from previously treated data,
e.g. with the treatfile class, and plots quickly the data in a personalized
manner. This class is inteded to be used in logbooks, such as jupyter
notebook.

#########
dyplot
#########

This class loads data from a file constantly and makes dynamic and
personalized plots. This class is intended to be used during a simulation, or
during data aquizition.

"""


from statplot import statplot
from dyplot import dyplot
from treatfile import treatfile

__all__ = ["statplot", "dyplot", "treatfile"]
