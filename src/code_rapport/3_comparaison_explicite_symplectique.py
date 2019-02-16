from matplotlib import pyplot as plt
import numpy as np
import random as random

q = 1.6021766208e-19
qe = -q
me = 9.109e-31
T = 100
N = 1000
L = 100
nbr_particules = 2

h = T/N
pos = np.zeros((N, nbr_particules))
vit = np.zeros((N, nbr_particules))

for i in range(nbr_particules):
	pos[0,i] = random.randint(0,L)

for i in range(nbr_particules):
	vit[0,i] = random.uniform(0,5)

pos_old = pos[0]
vit_old = vit[0]
fig = plt.figure('Espace des phases')
fig.suptitle("Comparaison d'euler explicite et euler symplectique\navec " + str(nbr_particules) + ' particules en 1D avec champs électrique\n(T=' + str(T) + ', N=' + str(N) + ', L=' + str(L) + ')')

ax = fig.add_subplot(121)
plt.ylabel('Vitesse')
plt.xlabel('Position')

for i in range(N):
	pos_next = (pos_old + h * vit_old) % L
	vit_next = np.zeros(nbr_particules)
	for j in range(nbr_particules):
		vit_next[j] = vit_old[j] - h*(qe/me)*np.sin((2*np.pi/L)*pos_old[j])*(me/qe)
	pos[i] = pos_next
	vit[i] = vit_next
	pos_old = pos_next
	vit_old = vit_next

for i in range(nbr_particules):
	p = pos[:N,i]
	v = vit[:N,i]	
	plt.plot(p, v, '-')

ax = fig.add_subplot(122)
plt.ylabel('Vitesse')
plt.xlabel('Position')

for i in range(N):
	pos_next = (pos_old + h * vit_old) % L
	vit_next = np.zeros(nbr_particules)
	for j in range(nbr_particules):
		vit_next[j] = vit_old[j] - h*(qe/me)*np.sin((2*np.pi/L)*pos_next[j])*(me/qe)
	pos[i] = pos_next
	vit[i] = vit_next
	pos_old = pos_next
	vit_old = vit_next

for i in range(nbr_particules):
	p = pos[:N,i]
	v = vit[:N,i]	
	plt.plot(p, v, '-')

plt.subplots_adjust(top=0.8,wspace=0.5)
plt.show()