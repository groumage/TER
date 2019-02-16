from matplotlib import pyplot as plt
import numpy as np

q = 1.6021766208e-19
qe = -q
me = 9.109e-31

N = 101
L = 100

params = {'mathtext.default': 'regular' }
plt.rcParams.update(params)

plt.title("Représentation de la fonction $E_0$ sur [0;+" + str(L) + "]")
plt.ylabel('Champs électrique')
plt.xlabel('Position')

x = np.linspace(0,L,N)
y = [np.sin((2*np.pi/L)*i)*(me/qe) for i in range(N)]
plt.plot(x,y,'-',color='orange')

x = np.linspace(0,L,2)
y = np.zeros(2)
plt.plot(x,y,'-',color='blue')

plt.show()