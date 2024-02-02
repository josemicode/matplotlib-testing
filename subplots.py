import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

# This program is meant to show the representation of multiple graphs in one window (figure) as subplots

x = np.arange(100) # Mutable sequence of numbers from 0 to 99

fig, axis = plt.subplots(2, 2) # These two parameters being the dimensions of the grid that will contain the plots

# Now we can design each graph individually by accessing their grid positions

axis[0, 0].plot(x, np.log(x+1))
axis[0, 0].set_title("log(x)")

axis[0, 1].scatter(x, np.random.random(100) * 30, color="green", alpha=0.7)
axis[0, 1].set_title("random scatter")

axis[1, 0].plot(x, np.power(x, 3), color="red")
axis[1, 0].set_title("x^3")

axis[1, 1].hist(x, cumulative=True, color="yellow", alpha=0.7)
axis[1, 1].set_title("cumulative")

# This will affect the whole figure

fig.suptitle("4 Graphs", fontsize=16)

# Instead of just showing the graph, the program will automatically save it as an image wherever this file is executed

cwd = os.getcwd()
file = cwd + "/subplot.png"
plt.savefig(file, dpi=320)