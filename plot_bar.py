import numpy as np
import matplotlib.pyplot as plt
from numpy import genfromtxt


value_for_bar = genfromtxt('data/values_for_bars.csv', delimiter=',')

unique, counts = np.unique(value_for_bar, return_counts=True)

plt.bar(unique, counts)
plt.show()