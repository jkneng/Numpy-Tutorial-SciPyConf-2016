# Copyright 2016 Enthought, Inc. All Rights Reserved
"""
Wind Statistics
----------------

Topics: Using array methods over different axes, fancy indexing.

1. The data in 'wind.data' has the following format::

        61  1  1 15.04 14.96 13.17  9.29 13.96  9.87 13.67 10.25 10.83 12.58 18.50 15.04
        61  1  2 14.71 16.88 10.83  6.50 12.62  7.67 11.50 10.04  9.79  9.67 17.54 13.83
        61  1  3 18.50 16.88 12.33 10.13 11.17  6.17 11.25  8.04  8.50  7.67 12.75 12.71

   The first three columns are year, month and day.  The
   remaining 12 columns are average windspeeds in knots at 12
   locations in Ireland on that day.

   Use the 'loadtxt' function from numpy to read the data into
   an array.

2. Calculate the min, max and mean windspeeds and standard deviation of the
   windspeeds over all the locations and all the times (a single set of numbers
   for the entire dataset).

3. Calculate the min, max and mean windspeeds and standard deviations of the
   windspeeds at each location over all the days (a different set of numbers
   for each location)

4. Calculate the min, max and mean windspeed and standard deviations of the
   windspeeds across all the locations at each day (a different set of numbers
   for each day)

5. Find the location which has the greatest windspeed on each day (an integer
   column number for each day).

6. Find the year, month and day on which the greatest windspeed was recorded.

7. Find the average windspeed in January for each location.

You should be able to perform all of these operations without using a for
loop or other looping construct.

Bonus
~~~~~

1. Calculate the mean windspeed for each month in the dataset.  Treat
   January 1961 and January 1962 as *different* months. (hint: first find a
   way to create an identifier unique for each month. The second step might
   require a for loop.)

2. Calculate the min, max and mean windspeeds and standard deviations of the
   windspeeds across all locations for each week (assume that the first week
   starts on January 1 1961) for the first 52 weeks. This can be done without
   any for loop.

Bonus Bonus
~~~~~~~~~~~

Calculate the mean windspeed for each month without using a for loop.
(Hint: look at `searchsorted` and `add.reduceat`.)

Notes
~~~~~

These data were analyzed in detail in the following article:

   Haslett, J. and Raftery, A. E. (1989). Space-time Modelling with
   Long-memory Dependence: Assessing Ireland's Wind Power Resource
   (with Discussion). Applied Statistics 38, 1-50.


See :ref:`wind-statistics-solution`.
"""
import numpy as np
from numpy import loadtxt
wind_data = loadtxt('wind.data', dtype=np.float)
# 2.
print '2:'
data = wind_data[:, 3:]
# print data
print data.min(), data.max(), data.mean(), data.std()

# 3.
print '3:'
# axis = 0: compute by column
print data.min(axis=0)
print data.max(axis=0)
print data.mean(axis=0)
print data.std(axis=0)

# axis=(0, 1): compute by whole
# print data.mean(axis=(0, 1))
# 4
print '4:'
# axis = 1: compute by row
print data.min(axis=1)
print data.max(axis=1)
print data.mean(axis=1)
print data.std(axis=1)

print '5:'
print data.argmax(axis=1)

print '6:'
daily_max = data.argmax(axis=1)
row_max = daily_max.argmax()
print 'Day of max reading: %s-%s-%s' % (wind_data[row_max, 0], wind_data[row_max, 1], wind_data[row_max, 2])

print '7:'
jan_indices = wind_data[:, 1] == 1
jan_data = data[jan_indices]
print jan_data.mean(axis=0)

print 'Bonus 1:'
months = wind_data[:, 0] * 100 + wind_data[:, 1]
month_values = set(months)
month_means = np.zeros(len(month_values))

for month in month_values:
    daily_indices = months == month
    month_means[month] =  data[daily_indices].mean()

print 'Bonus 2: '
weekly_data = data[: 52 * 7].reshape(-1, 12 * 7)
print weekly_data.min(axis=1)
print weekly_data.max(axis=1)
print weekly_data.mean(axis=1)
print weekly_data.std(axis=1)

print 'Bonus Bonus: '
