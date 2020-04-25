#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 09:01:19 2020

@author: tushar
"""

import matplotlib.pyplot as plt
year = [1950, 1970, 1990, 2010]
pop = [2.5, 3.692, 5.2, 6.97]

year += [1920, 1930]
pop += [1.1, 1.9]
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
plt.title('Whatever Graph')
plt.yticks(range(0, 10, 2), ['0', '2B', '4B', '6B', '8B']) # Second param list is displayed 
# and mapped to first param
# plt.xticks(range(1,2000,100))

# f, ax = plt.subplots(2)
# ax[0].set_title('Simple Plot')
# ax[0].plt(year, pop)
# ax[1].hist(values, bins=3)

# Subplot is a separate entity, so both earlier plot and 
# the subplots are shown in separate windows
# f, axarr = plt.subplots(2)
# f, axarr = plt.subplots(2, sharey=True)
# axarr[0].plot(year, pop)
# axarr[0].set_title('Sharing X axis')
# axarr[1].scatter(year, pop)
# axarr[0].clf()

# Showing bubles corresponding to 1) size and 
# 2) color
# Addint 3) Opcaity
plt.clf()
# s for size of each scatter dot
# c for color of each scatter dot
# alpha for opacity, lower means more transparent
plt.scatter(year, pop, s=[1,2,3,34,55,86],
            c=['red', 'green', 'blue', 'yellow', 'black', 'pink'],
            alpha = 0.5) 

# 4) Text
# 5) Gridlines
plt.text(1950, 3.60, 'TEXT') # coordinates acc to X and Y axes
plt.grid(True) # Grids are acc to the displayed values on axes

from gapminder import gapminder
print(gapminder.loc[gapminder['country']=='Bangladesh'])
# Same as gapminder.loc['Bangladesh']


plt.clf()

x, y = range(10), range(10)
fig, ax = plt.subplots(2, 2)
ax[0,0].plot(x, y, color='r') # NO assignment and NO plt.plot
ax[0,1].plot(x, y)
ax[1,0].plot(x, y)
ax[1,1].plot(x, y)
plt.show()


plt.clf()
# fig = plt.figure()

plt.subplot(2, 2, 1)
plt.plot(x, y)

plt.subplot(2, 2, 2)
plt.plot(x, y)

plt.subplot(2, 2, 3)
plt.plot(x, y)

plt.subplot(2, 2, 4)
plt.plot(x, y)

plt.show()





























