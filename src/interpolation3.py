from matplotlib import pyplot as plt
import numpy as np
import random as random
import math as math

# constantes
q = 1.6021766208e-19
qe = -q
me = 9.109e-31

# paramètres
T = 100
N = 100000
L = 1000
I = 10
nbr_particules = 3

h = T/N
pos = np.zeros((N, nbr_particules))
vit = np.zeros((N, nbr_particules))

# initialisation des valeurs initiales de position et de vitesse
for i in range(nbr_particules):
	pos[0,i] = random.uniform(0,L)
for i in range(nbr_particules):
	vit[0,i] = random.uniform(0.1,15)
mem_pos_ini = np.zeros(nbr_particules)
mem_vit_ini = np.zeros(nbr_particules)	
for i in range(nbr_particules):
	mem_pos_ini[i] = pos[0,i]
	mem_vit_ini[i] = vit[0,i]

fig = plt.figure('particules_1D')

# graphique 1 : discretisation du champs en I points
ax = fig.add_subplot(131)
pos_old = pos[0]
vit_old = vit[0]
field = np.zeros(I+1)
for i in range(I+1):
	# formule a ameliorer ?
	field[i] = np.sin(((2*np.pi)/L)*i*(L/I)) * (me/qe)
	#print("L:"+str(L)+"   i:"+str(i*(L/I)))
# la derniere valeur du champs est saisie a la main car si on calcule sin(2*pi) on ne trouve pas 0 (trop faible precision ?)
field[I] = 0
for i in range(N):
	pos_next = (pos_old + h * vit_old) % L
	vit_next = np.zeros(nbr_particules)
	for j in range(nbr_particules):
		x = pos_old[j]
		n = math.floor((I/L) * x)
		inf = n
		sup = n + 1
		alpha = x - n * L/I
		apply_field = alpha * field[sup] + (1-alpha) * field[inf]
		vit_next[j] = vit_old[j] - h * (qe/me) * apply_field
	pos[i] = pos_next
	vit[i] = vit_next
	pos_old = pos_next
	vit_old = vit_next
for i in range(nbr_particules):
	p = pos[:N,i]
	v = vit[:N,i]

# graphique 2 : discretisation du champs en I*10 points
ax = fig.add_subplot(132)
pos = np.zeros((N, nbr_particules))
vit = np.zeros((N, nbr_particules))
for i in range(nbr_particules):
	pos[0,i] = mem_pos_ini[i]
	vit[0,i] = mem_vit_ini[i]
pos_old = pos[0]
vit_old = vit[0]
field = np.zeros(I*10+1)
for i in range(I*10+1):
	# formule a ameliorer ?
	field[i] = np.sin(((2*np.pi)/L)*i*(L/(I*10))) * (me/qe)
	#print("L:"+str(L)+"   i:"+str(i*(L/(I*10))))
# la derniere valeur du champs est saisie a la main car si on calcule sin(2*pi) on ne trouve pas 0 (trop faible precision ?)
field[I*10] = 0
for i in range(N):
	pos_next = (pos_old + h * vit_old) % L
	vit_next = np.zeros(nbr_particules)
	for j in range(nbr_particules):
		x = pos_old[j]
		n = math.floor((I*10/L) * x)
		inf = n
		sup = n + 1
		alpha = x - n * L/(I*10)
		apply_field = alpha * field[sup] + (1-alpha) * field[inf]
		vit_next[j] = vit_old[j] - h * (qe/me) * apply_field
	pos[i] = pos_next
	vit[i] = vit_next
	pos_old = pos_next
	vit_old = vit_next
for i in range(nbr_particules):
	p = pos[:N,i]
	v = vit[:N,i]

# graphique 3 : utilisation du champs continu
ax = fig.add_subplot(133)
pos = np.zeros((N, nbr_particules))
vit = np.zeros((N, nbr_particules))
for i in range(nbr_particules):
	pos[0,i] = mem_pos_ini[i]
	vit[0,i] = mem_vit_ini[i]
pos_old = pos[0]
vit_old = vit[0]
for i in range(N):
	pos_next = (pos_old + h * vit_old) % L
	vit_next = np.zeros(nbr_particules)
	for j in range(nbr_particules):
		vit_next[j] = vit_old[j] - h*(qe/me)*(np.sin((2*np.pi/L)*pos_old[j])*(me/qe))
	pos[i] = pos_next
	vit[i] = vit_next
	pos_old = pos_next
	vit_old = vit_next
for i in range(nbr_particules):
	p = pos[:N,i]
	v = vit[:N,i]

fig.suptitle("Graphiques représentant la vitesse de particules en fonction de leur position")

plt.show()