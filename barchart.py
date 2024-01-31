import numpy as np
import matplotlib.pyplot as plt

# Bar charts are normally used to represent biases associated to specific objects/options
# Example given: average grades of each college subject

subjects = ["Algorithms and Data Structures", "Electronic Systems", "Introduction to Programming", "Economy", "Linear Algebra and Graph Theory"]
grades = [7, 6, 5, 8, 2]

plt.bar(subjects, grades, color="b", edgecolor="r", lw=2)
plt.show()