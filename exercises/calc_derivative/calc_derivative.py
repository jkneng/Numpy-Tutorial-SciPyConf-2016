# Copyright 2016 Enthought, Inc. All Rights Reserved
"""
Calculate Derivative
--------------------

Topics: NumPy array indexing and array math.

Use array slicing and math operations to calculate the
numerical derivative of ``sin`` from 0 to ``2*pi``.  There is no
need to use a 'for' loop for this.

Plot the resulting values and compare to ``cos``.

Bonus
~~~~~

Implement integration of the same function using Riemann sums or the
trapezoidal rule.

See :ref:`calc-derivative-solution`.
"""
from numpy import linspace, pi, sin, cos, cumsum
from matplotlib.pyplot import plot, show, subplot, legend, title

# calculate the sin() function on evenly spaced data.
x = linspace(0,2*pi,101)
y = sin(x)

dx = x[1:] - x[:-1]
dy = y[1:] - y[:-1]
dy_dx = dy/dx

centers_x = (x[1:] + x[:-1]) / 2
subplot(1, 2, 1)
plot(centers_x, dy_dx, 'rx', centers_x, cos(centers_x), 'b-')
title(r"$\rm{Derivative\ of}\ sin(x)$")

# Bonus: integration of sinx: Riemann sums or the trapezoidal rule
avg_height = (y[1:] + y[:-1]) / 2
integral_sin = cumsum(avg_height * dx)

close_form = -cos(x) + 1
subplot(1, 2, 2)

plot(x[1:], integral_sin, 'rx', x, close_form, 'b-')
legend(('numerical', 'actual'))
title(r"$\int \, \sin(x) \, dx$")

show()
