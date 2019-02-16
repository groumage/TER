from matplotlib import pyplot as plt
import random as random
import numpy as np

N = 100
nbr_pts = 2000000

fig = plt.figure('Densité')
fig.suptitle("Détermination d'une densité à partir d'un nuage de points")
ax = fig.add_subplot(121)

x = []
y = []
for i in range(nbr_pts):
	alpha = random.uniform(0,1)
	c = float((1*1)+1+1/6)
	beta = random.uniform(0,1) * c
	if (beta <= float((alpha**2)+alpha+1/6)):
		x.append(alpha)
		y.append(beta)
X = np.linspace(0,1,len(x))
Y = [float((x**2)+x+1/6) for x in X]
plt.plot(x,y,'x')
plt.plot(X,Y)


ax = fig.add_subplot(122)
l = len(x)
x_densite = np.linspace(0,1,N+1)
y_densite = np.zeros(N+1)

for i in range(N):
	nbr_particules = 0
	for j in range(l):
		if (i/N <= x[j] <= (i+1)/N):
			nbr_particules += 1
	y_densite[i] = nbr_particules
y_densite[N] = y_densite[N-1]

plt.subplots_adjust(wspace=0.5)

plt.plot(x_densite,y_densite,'-')
plt.show()