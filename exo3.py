import numpy as np
import matplotlib.pyplot as plt

c = 10

def contour(b:complex, c:float, n):
    rayon = ((b.real - c) ** 2 + b.imag ** 2) ** 0.5
    thetas = np.linspace(0, 2 * np.pi, n)

    C = b + rayon * np.exp(complex(0, 1) * thetas)

    return C

def joukovski(arc, c):
    return arc + (c ** 2) / arc


C = contour(complex(1, 1), 5, 1000)
T = joukovski(C, 3)

plt.scatter(T.real, T.imag)
plt.show()