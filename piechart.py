import numpy as np
import matplotlib.pyplot as plt

# Pie charts show information as percentage pieces of a circular set
# This example references a poll that recollects the voter's favorite sports

votes = [50, 36, 28, 46, 61]
sports = ["Swimming", "Basketball", "Football", "Running", "Tennis"]

# This array will later be introducuced as a parameter to indicate each of the pieces' distances from the center
pull = [0, 0.5, 0, 0, 0]

# This is the standard format used so that the graph will show percentages up to 2 digits behind the floating point
percentageFormat = "%.2f%%"

plt.pie(votes, labels=sports, explode=pull, autopct=percentageFormat, pctdistance=0.6, startangle=90)
plt.show()