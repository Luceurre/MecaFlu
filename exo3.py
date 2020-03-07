import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import matplotlib.patches
import matplotlib; matplotlib.use("TkAgg")
c = 10
R = 10
delta_x = 0.2
x_min = -1
x_max = 0
i = complex(0, 1)
n = 1000

colors=['b','r','g','k','y','m']

def contour(b:complex, c:float, n):
    rayon = ((b.real - c) ** 2 + b.imag ** 2) ** 0.5
    thetas = np.linspace(0, 2 * np.pi, n)

    C = b + rayon * np.exp(complex(0, 1) * thetas)

    return C

def joukovski(arc, c):
    return arc + (c ** 2) / arc


# Question 4a)
_, ax = plt.subplots()

arc = joukovski(contour(complex(-1, 0), c, n), c)
ax.scatter(arc.real, arc.imag, color=np.random.rand(3, ), label="(-1, 0)")
arc = joukovski(contour(complex(0, 0), c, n), c)
ax.scatter(arc.real, arc.imag, color=np.random.rand(3, ), label="(0, 0)")
arc = joukovski(contour(i, c, n), c)
ax.scatter(arc.real, arc.imag, color=np.random.rand(3, ), label="(0, 1)")

ax.legend()
ax.grid(True)
ax.set_title("Question 4a)")

plt.show()

# Question 4b)
_, bx = plt.subplots()

x = np.arange(x_min, x_max, delta_x)
centres = x + i

for centre in centres:
    arc = joukovski(contour(centre, c, n), c)
    bx.scatter(arc.real, arc.imag, color=np.random.rand(3, ), label="x = %.1f" % centre.real)

bx.legend()
bx.grid(True)
bx.set_title("Question 4b)")

plt.show()

# Question 5)

_, cx = plt.subplots()

def delta(b, delta_x):
    return 4 * (b.real ** 2) * (1 + np.exp(2 * delta_x * i)) - 4 * (1 - np.exp(2 * i * delta_x)) * (b ** 2 - (b.imag ** 2) * np.exp(2 * i * delta_x))

for centre in centres:
    c = (2 * centre.real * (1 + np.exp(2 * i * delta_x)) + delta(centre, delta_x) ** 0.5) / (2 * (1 - np.exp(2 * i * delta_x)))

    arc = joukovski(contour(centre, c, n), c)
    cx.scatter(arc.real, arc.imag, color=np.random.rand(3, ), label="x = %.1f" % centre.real)

cx.legend()
cx.grid(True)
cx.set_title("Question 5")

plt.show()

# Question 6)

U_inf = 1
R = 1
m = 0
delta_t = 0.1
T_max = 10

plot, dx = plt.subplots()

def f_prime(Z:complex):
    return U_inf * (1 - R**2 / Z**2) - i * m / (2 * np.pi) / Z

# L'équation différentielle à résoudre
def equa_diff(x, t):
    Z = f_prime(complex(x[0], x[1]))
    return [Z.real, -Z.imag]

def animation(xs):
    plt.xlim([np.min(xs[:, :, 0]), np.max(xs[:, :, 0])])
    plt.ylim([np.min(xs[:, :, 1]), np.max(xs[:, :, 1])])

    for k in range(len(xs[0])):
        x = xs[:, 0:(k+1), 0]
        y = xs[:, 0:(k+1), 1]

        dx.scatter(x, y, color = 'r')
        circle = plt.Circle((0, 0), R, color='black')
        dx.add_artist(circle)
        plt.pause(0.01)

t = np.arange(0, T_max, delta_t) # Pas de temps choisis
x0 = -5
y0_min = -1
y0_max = 1
nb_x0 = 10

x0s = np.linspace([x0, y0_min], [x0, y0_max], nb_x0)
results = []
for x0 in x0s:
    results.append(odeint(equa_diff, x0, t))

results = np.array(results)
animation(results)

plot.show()
