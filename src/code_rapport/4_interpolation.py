from matplotlib import pyplot as plt
import numpy as np
import random as random
import math as math

q = 1.6021766208e-19
qe = -q
me = 9.109e-31

T = 100
N = 100000
L = 1000
I = 10
nbr_particules = 3

dt = T/N
dx = L/I
pos = np.zeros((N, nbr_particules))
vit = np.zeros((N, nbr_particules))

for i in range(nbr_particules):
	pos[0,i] = random.uniform(0,L)
for i in range(nbr_particules):
	vit[0,i] = random.uniform(0.1,15)
mem_pos_ini = np.zeros(nbr_particules)
mem_vit_ini = np.zeros(nbr_particules)	
for i in range(nbr_particules):
	mem_pos_ini[i] = pos[0,i]
	mem_vit_ini[i] = vit[0,i]

fig = plt.figure('Simulation')
fig.suptitle("Discrétisation du champs électrique\navec " + str(nbr_particules) + ' particules (T=' + str(T) + ', N=' + str(N) + ', L=' + str(L) + ')',style='italic')
ax = fig.add_subplot(131)
plt.title("I=" + str(I))
plt.ylabel('Vitesse')
plt.xlabel('Position')
pos_old = pos[0]
vit_old = vit[0]
field = np.zeros(I+1)
for i in range(I+1):
	field[i] = math.sin(((2*np.pi)/L)*i*dx)
	#print("L:"+str(L)+"   i:"+str(i*(L/I)))
field[I] = 0
for i in range(N):
	pos_next = (pos_old + dt * vit_old) % L
	vit_next = np.zeros(nbr_particules)
	for j in range(nbr_particules):
		n = math.floor((I/L)*pos_next[j])
		inf = n
		sup = n+1
		alpha = pos_next[j] - n * dx
		apply_field = alpha * field[sup] + (1-alpha) * field[inf]
		vit_next[j] = vit_old[j] - dt*apply_field
	pos[i] = pos_next
	vit[i] = vit_next
	pos_old = pos_next
	vit_old = vit_next
for i in range(nbr_particules):
	p = pos[:N,i]
	v = vit[:N,i]
	plt.plot(p, v, '-')

ax = fig.add_subplot(132)
plt.title("I=" + str(I*10))
plt.ylabel('Vitesse')
plt.xlabel('Position')
pos = np.zeros((N, nbr_particules))
vit = np.zeros((N, nbr_particules))
for i in range(nbr_particules):
	pos[0,i] = mem_pos_ini[i]
	vit[0,i] = mem_vit_ini[i]
pos_old = pos[0]
vit_old = vit[0]
field = np.zeros(I*10+1)
for i in range(I*10+1):
	field[i] = math.sin(((2*np.pi)/L)*i*(dx/10))
	#print("L:"+str(L)+"   i:"+str(i*(L/(I*10))))
field[I*10] = 0

for i in range(N):
	pos_next = (pos_old + dt * vit_old) % L
	vit_next = np.zeros(nbr_particules)
	for j in range(nbr_particules):
		n = math.floor(((I*10)/L)*pos_next[j])
		inf = n
		sup = n+1
		alpha = pos_next[j] - n * dx/10
		apply_field = alpha * field[sup] + (1-alpha) * field[inf]
		vit_next[j] = vit_old[j] - dt*apply_field
	pos[i] = pos_next
	vit[i] = vit_next
	pos_old = pos_next
	vit_old = vit_next
for i in range(nbr_particules):
	p = pos[:N,i]
	v = vit[:N,i]
	plt.plot(p, v, '-')

ax = fig.add_subplot(133)
plt.title("Champs continue")
plt.ylabel('Vitesse')
plt.xlabel('Position')
pos = np.zeros((N, nbr_particules))
vit = np.zeros((N, nbr_particules))
for i in range(nbr_particules):
	pos[0,i] = mem_pos_ini[i]
	vit[0,i] = mem_vit_ini[i]
pos_old = pos[0]
vit_old = vit[0]
for i in range(N):
	pos_next = (pos_old + dt * vit_old) % L
	vit_next = np.zeros(nbr_particules)
	for j in range(nbr_particules):
		vit_next[j] = vit_old[j] - dt * math.sin((2*np.pi/L) * pos_next[j])
	pos[i] = pos_next
	vit[i] = vit_next
	pos_old = pos_next
	vit_old = vit_next
for i in range(nbr_particules):
	p = pos[:N,i]
	v = vit[:N,i]	
	plt.plot(p, v, '-')

plt.subplots_adjust(top=0.8,wspace=0.6)
plt.show()


# 1er graphe : I
# 2e graphe : I * 10
# 3e graphe : sans discrétisation champs continue