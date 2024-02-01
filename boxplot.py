import numpy as np
import matplotlib.pyplot as plt

# Box plots are often used as a tool to visualize the data distribution of a certain query
# Showing the median, the ranges, extremes and outliers
# Now, the following example represents how weight is distributed

weights = np.random.normal(70, 10.5, 1000)

plt.boxplot(weights)
plt.show()