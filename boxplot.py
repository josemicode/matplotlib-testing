import numpy as np
import matplotlib.pyplot as plt

# Box plots are often used as a tool to visualize the data distribution of a certain query
# Showing the median, the ranges, extremes and outliers
# Now, the following example represents how weight is distributed

weights = np.random.normal(70, 10.5, 1000)

plt.figure(1)

plt.boxplot(weights)

# This next figure is an example of a data collection with no outliers and ranges closer to its extremes

sec1 = np.linspace(0, 20, 50)
sec2 = np.linspace(21, 60, 50)
sec3 = np.linspace(61, 70, 50)

ages = np.concatenate((sec1, sec2, sec3))

plt.figure(2)

plt.boxplot(ages)
plt.show()