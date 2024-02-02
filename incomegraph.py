import numpy as np
import matplotlib.pyplot as plt

# This is a file made for testing basic customization options in a line chart, representing an income graph

years = [2010 + x for x in range(14)]

sec1 = np.linspace(40, 60, 4)
sec2 = 60 + np.random.random(5) * 30
sec3 = [70 + np.log(x+1) for x in range(5)]

income = np.concatenate((sec1, sec2, sec3))

incomeTicks = list(range(40, 105, 5))
tickFormatY = [f"{x}k €" for x in incomeTicks]

plt.plot(years, income)

# Title and axis labels
plt.title("Company's Yearly Income", fontsize=22, fontname="Arial")
plt.xlabel("Years")
plt.ylabel("EUR")

# Custom additional string attached as a label for each point in the axis
plt.yticks(incomeTicks, tickFormatY)

plt.show()