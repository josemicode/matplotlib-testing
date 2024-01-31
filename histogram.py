import numpy as np
import matplotlib.pyplot as plt

# Histograms are commonly used to represent averages and to better perceive the standard deviation of a query
# This one, specifically, shows a normal distribution where the mean value is 80 and the std dev is 4.4 (there will be 1000 values)

data = np.random.normal(80, 4.4, 1000)

# bin sizes can also be customized to represent specific portions
# eg: from the minimun value to 20, to 30, to the maximum

binSize = [data.min(), 75, 85, data.max()]

# Though in this case we are going to specify the number rather than the ranges

binSize = 10

plt.hist(data, bins=binSize)

# By activting the cumulative attribute we will also be shown the amount of values below each level
plt.hist(data, bins=binSize, cumulative=True, color="y", alpha=0.4)
plt.show()