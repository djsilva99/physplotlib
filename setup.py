# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""physplotlib: Library for plotting quickly data from log files

Usefull when handling with output files from numerical
simulations in a quick way. Loads data from text files, makes treatments
and plots the resulted data in a very simple manner.

"""

from setuptools import setup


setup(name='physplotlib',
      version='0.1.1',
      description='Library for plotting quickly data from log files',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 2.7',
          'Topic :: Scientific/Engineering :: Physics',
      ],
      keywords='plotting numerical simulations heatrapy log files',
      url='https://github.com/danieljosesilva/physplotlib',
      author='Daniel Silva',
      author_email='djsilva99@gmail.com',
      license='MIT',
      packages=['physplotlib'],
      install_requires=[
          'matplotlib',
      ],
      include_package_data=True,
      zip_safe=False)
