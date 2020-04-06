#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 09:01:19 2020

@author: tushar
"""

import matplotlib.pyplot as plt
year = [1950, 1970, 1990, 2010]
pop = [2.5, 3.692, 5.2, 6.97]

# LINE PLOT
# The first parameter goes into X-axis
# plt.plot(year, pop) # This is the line plot
# plt.show() # Need to call this after every graph is generated/plotted in code
plt.clf()

# SCATTER PLOT === Good for judging correaltion. Sometimes the line plot 
# is too messy. Then we can try scatter plot. ===
# plt.subplot(1)
plt.scatter(year, pop) # This is the scatter plot (Only points, no line)
plt.xscale('log') # To put X-axis on a log scale - this change carries 
# over to next cell as well
plt.show()
# plt.clf() # Cleans the figure

# HISTOGRAM === Good for showing distribution of data
help(plt.hist) # Help function for python
values = [0, 0.6, 1.4, 1.6, 1.6, 1.7, 2.5, 2.6, 3.3, 4, 5]
# plt.subplot(2)
plt.hist(values, bins=3, orientation='horizontal') # Orientation is by default 'vertical'
# plt.xscale('linear')
plt.show()
# plt.clf()

plt.xlabel('Year')
plt.ylabel('Population')
plt.set_title('Simple Plot')


