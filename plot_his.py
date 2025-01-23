import numpy as np
import matplotlib.pyplot as plt
from numpy import genfromtxt


value_for_hist = genfromtxt('data/values_for_hist.csv', delimiter=',')

plt.hist(value_for_hist, bins=80)
plt.show()