import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

x = np.linspace(-3, 3, 200)
y = x

x, y = np.meshgrid(x, y)

z1 = x * y
z2 = (x**2) + (y**2)
z3 = np.sin(3*x) * y

fig, axs = plt.subplots(2, 2, figsize=(8, 6), subplot_kw={'projection': '3d'})

axs[0, 0].plot_surface(x, y, z1)
axs[0, 1].plot_surface(x, y, z2)
axs[1, 0].plot_surface(x, y, z3)
axs[1, 1].set_axis_off()

plt.show()

