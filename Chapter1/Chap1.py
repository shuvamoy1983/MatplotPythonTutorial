"""Spyder Editor

This is a Simple plot graph """

import numpy as np
import matplotlib.pyplot as plt

# Data for plotting
t = np.arange(4)
s = 1 + np.sin(2 * t)
print(t)
print(s)

# Note that using plt.subplots below is equivalent to using
# fig = plt.figure and then ax = fig.add_subplot(111)
fig, ax = plt.subplots()
ax.plot(t,s)

ax.set(xlabel='time (s)', ylabel='voltage (mV)',
       title='About as simple as it gets, folks')
ax.grid()

fig.savefig("test.png")
plt.show()