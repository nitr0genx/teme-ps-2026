import numpy as np
import matplotlib.pyplot as plt

def x(t):
    return np.cos(520 * np.pi * t + np.pi / 3)

def y(t):
    return np.cos(280 * np.pi * t - np.pi / 3)

def z(t):
    return np.cos(120 * np.pi * t + np.pi / 3)

a = np.arange(0, 0.03, 0.0005)


fig, axs = plt.subplots(3)
axs[0].plot(a, x(a))
axs[1].plot(a, y(a))
axs[2].plot(a, z(a))
plt.show()
