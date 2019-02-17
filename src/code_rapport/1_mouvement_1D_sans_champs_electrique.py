from matplotlib import pyplot as plt
import numpy as np
import random as random

T = 1000
N = 1000
L = 100
nbr_particules = 10

h = T/N

pos = np.zeros((N,nbr_particules))
vit = np.zeros((N,nbr_particules))

for i in range(nbr_particules):
	pos[0,i] = random.randint(0,L)
for i in range(nbr_particules):
	vit[0,i] = random.uniform(0.1,1)

pos_old = pos[0]
vit_old = vit[0]
for i in range(1,N):
	pos_next = (pos_old + h * vit_old) % L
	pos[i] = pos_next
	vit[i] = vit_old
	pos_old = pos_next

fig = plt.figure('Simulation')
fig.suptitle('Mouvements de ' + str(nbr_particules) + ' particules en 1D sans champs électrique \n(T=' + str(T) + ', N=' + str(N) + ', L=' + str(L) + ')',style='italic')

ax = fig.add_subplot(121)
plt.ylabel('Vitesse')
plt.xlabel('Position')
for i in range(nbr_particules):
	p = pos[:N,i]
	v = vit[:N,i]
	plt.plot(p, v, '-')

ax = fig.add_subplot(122)
plt.ylabel('Vitesse')
plt.xlabel('Position')
ax.set_xlim([-3.,L+3])
ax.set_ylim([-2.,2.])

t = np.linspace(0,L,2)
zeros_tab = np.zeros(2)
plt.plot(t,zeros_tab,'-', color='blue')

plt.subplots_adjust(wspace=0.5)

pts = []

for i in range(nbr_particules):
	pts += ax.plot([], [], marker="o")
    
for n in range(N):
	for pt,i in zip(pts,range(nbr_particules)):
		pt.set_data(pos[n,i],0)

	plt.pause(0.001)
