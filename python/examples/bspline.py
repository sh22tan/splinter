# This file is part of the SPLINTER library.
# Copyright (C) 2012 Bjarne Grimstad (bjarne.grimstad@gmail.com).
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.


# Add the SPLINTER directory to the search path, so we can include it
import numpy as np
import matplotlib.pyplot as plt
from os import sys, path, remove
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))


##### Start of the example #####
import splinter

splinter.load("/home/bjarne/Code/C++/splinter4/splinter/bin/Release/libsplinter-2-0.so")
#splinter.load("/home/anders/SPLINTER/build/debug/libsplinter-2-0.so")


# Example with one variable
def f1(x):
    return -1. + 2*x + 0.1*(x**2) + 10*np.random.rand(1)[0]

x = np.arange(0, 11, 1)
y = np.zeros((len(x),))
for i in range(len(x)):
    y[i] = f1(x[i])
d1 = list(zip(x, y))

# Linear B-spline that interpolates the data
b1 = splinter.BSplineBuilder(d1, degree=1).build()

# Quadratic B-spline that interpolates the data
b2 = splinter.BSplineBuilder(d1, degree=2).build()

# Cubic P-spline that interpolates the data
b3 = splinter.BSplineBuilder(d1, degree=3).build()

xd = np.arange(0, 10, .01)
yd1 = b1.eval(list(xd))
yd2 = b2.eval(list(xd))
yd3 = b3.eval(list(xd))

plt.plot(x, y, '*', label='Data points')
plt.plot(xd, yd1, label='Linear B-spline')
plt.plot(xd, yd2, '--', label='Quadratic B-spline')
plt.plot(xd, yd3, '-.', label='Cubic B-spline')
plt.legend(loc='upper left')
plt.show()
