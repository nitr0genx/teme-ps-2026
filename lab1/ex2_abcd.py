import numpy as np
import matplotlib.pyplot as plt

def a(t):
    return np.sin(400 * 2 * np.pi * t)

def b(t):
    return np.sin(800 * 2 * np.pi * t)

def c(t):
    return np.mod(t, 1/240)

def d(t):
    return np.sign(np.sin(300 * 2 * np.pi * t))

x1 = np.arange(0, 0.08, 0.00005)
x2 = np.linspace(0, 3, 1000)
x3 = np.linspace(0, 0.03, 1000)
x4 = np.linspace(0, 0.03, 1000)

fig, axs = plt.subplots(4)
axs[0].plot(x1, a(x1))
axs[1].plot(x2, b(x2))
axs[2].plot(x3, c(x3))
axs[3].plot(x4, d(x4))


plt.show()