# on represente les images d'un meme cercle par plusieurs transformations de joukovski
# transfo. de joukovski de parametre c: Z->z=Z+c**2/Z 
from math import *
from pylab import *
import numpy as np
import random
import matplotlib.pyplot as plt

# Mon code :




# liste des valeurs de c
c0=np.arange(0.,1.6,0.1)
nc=len(c0)
# choix aleatoire d'une couleur
la_liste=['b','r','g','k','y','m']
couleur=[]
for i in range(0,nc):
    couleur.append(random.choice(la_liste))
xz=[]
yz=[]
# R rayon du cercle
R=2.
# preparation de la figure
figure=plt.figure()
axes=plt.gca()
axes.set_xlim(-4.,4)
axes.set_ylim(-3.,3.)
plt.gca().set_aspect('equal', 'box')
for c in c0:
    xz1=[]
    yz1=[]
    for i in np.arange(0.,2*pi,.05):
        Z=R*(cos(i)+1j*sin(i))
        z=Z+c**2/Z
        xz1.append(z.real)
        yz1.append(z.imag)
    xz.append(xz1)
    yz.append(yz1)
# xz[k] et yz[k] sont les listes d'abscisses et d'ordonnees pour l'image
# par la k-eme transformation
for k in range(0,nc):
    plt.plot(xz[k],yz[k],linewidth=3,color=couleur[k])
    plt.pause(0.5)
plt.show()
# l'utilisation de pause(tau) avec tau en seconde permet une animation basique
