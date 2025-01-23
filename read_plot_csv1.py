import numpy as np
import matplotlib.pyplot as plt
from numpy import genfromtxt


points = genfromtxt('data/points.csv', delimiter=',')           # [x y]
distances = genfromtxt('data/distances.csv', delimiter=",")     # [distance]


plt.scatter(points[:, 0], points[:, 1], c=distances, cmap='winter')

plt.colorbar(label='Distance')

plt.show()