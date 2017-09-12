# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""Physplot.

This module contains classes to load data from csv (or txt) files, make
operations between columns or lines, and plot the respective treated
data. It uses the library matplotlib and is intended to be used by
engineers and scientists, who needs to make plots quickly after obtaiing
the data."""


from statplot import statplot
from dyplot import dyplot
from treatfile import treatfile

__all__ = ["statplot", "dyplot", "treatfile"]
