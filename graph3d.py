import numpy as np
import matplotlib.pyplot as plt

# This file contains code that generates a three dimensional scatter plot graph
# Note that implementing an auto-save might not be ideal because of the initial angle, which can be conveniently modified on runtime

# Example with a scatter

fig1 = plt.figure(1)
ax1 = fig1.add_subplot(projection="3d")

x = np.random.random(10)
y = np.random.random(10)
z = np.random.random(10)

ax1.scatter(x, y, z, color="purple")

ax1.set_title("3D Scatter")
ax1.set_xlabel("X")
ax1.set_ylabel("Y")
ax1.set_zlabel("Z")

# Example with a periodic function

fig2 = plt.figure(2)
ax2= fig2.add_subplot(projection="3d")

x = np.arange(0, 100, 1)
y = np.sin(x)
z = np.cos(x)

ax2.plot(x, y, z, color="red")

ax2.set_title("Sin to Cos")
ax2.set_xlabel("X")
ax2.set_ylabel("sine(X)")
ax2.set_zlabel("cosine(X)")

# Mesh example

fig3 = plt.figure(3)
ax3 = fig3.add_subplot(projection="3d")

a = np.arange(0, 4, 0.1)
b = np.arange(-2, 2, 0.1)

X, Y = np.meshgrid(a, b)
Z = np.sin(X) * np.cos(Y)

ax3.plot_surface(X, Y, Z, cmap="viridis") #Sidenote: There are many possible color maps, such as: viridis, plasma, inferno, magma, cividis, jet, coolwarm, rainbow, terrain, copper

ax3.set_title("Surface Plot")
ax3.view_init(azim=0, elev=90)

plt.show()