import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

style.use("ggplot")

applStock = 10 + np.random.random(10) * 90
micrStock = 10 + np.random.random(10) * 90
googStock = 10 + np.random.random(10) * 90

years = [2012 + x for x in range(10)]

stockTicks = list(range(0, 110, 10))
tickFormatY = [f"${x}M" for x in stockTicks]

plt.plot(years, applStock, label="Apple")
plt.plot(years, micrStock, label="Microsoft")
plt.plot(years, googStock, label="Google")

plt.legend(loc="lower right")

plt.yticks(stockTicks, tickFormatY)

plt.show()
