from matplotlib import pyplot as plt
from numpy import *

q = 1.6021766208e-19
qe = -q
me = 9.109e-31

# renvoie la valeur du champs electrique au point x, prenant en parametre la longueur su segment L
# fonction utilisee : E_0(x) = sin(2*pi*x/L)*(me/qe)
def electric_field(x,L):
	return sin((2*pi/L)*x)*(me/qe)

# renvoie le vecteur contenant les nouvelle vitesse des particules
def calc_vit (h, nbr_particules, pos_old, vit_old, L):
	vit_new = zeros(nbr_particules)
	for i in range(nbr_particules):
		vit_new[i] = vit_old[i] - h*(qe/me)*electric_field(pos_old[i],L)
	return vit_new

# affiche l'espace des phases des particules en faisant les calculs par la methode d'euler explicite
def phases_euler_explicite(T, N, L, nbr_particules):
	h = T/N
	pos = zeros((N, nbr_particules))
	vit = zeros((N, nbr_particules))

	for i in range(nbr_particules):
		pos[0,i] = random.randint(0,L)
	for i in range(nbr_particules):
		vit[0,i] = random.uniform(0,5)

	pos_old = pos[0]
	vit_old = vit[0]
	fig = plt.figure('particules_1D')
	ax = fig.add_subplot(111)

	for i in range(N):
		pos_next = (pos_old + h * vit_old) % L
		vit_next = calc_vit(h,nbr_particules,pos_old,vit_old,L)
		pos[i] = pos_next
		vit[i] = vit_next
		pos_old = pos_next
		vit_old = vit_next

	for i in range(nbr_particules):
		p = pos[:N,i]
		v = vit[:N,i]	
		plt.plot(p, v, '-')

	plt.show()

# affiche la simulation du mouvement des particules avec euler explicite
def particules_anime_euler_explicite(T, N, L, nbr_particules):
	h = T/N
	pos_old = zeros(nbr_particules)
	
	for i in range(nbr_particules):
		pos_old[i] = random.randint(0,L)

	vit_old = zeros(nbr_particules)
	for i in range(nbr_particules):
		vit_old[i] = random.uniform(2,5)

	fig = plt.figure('particule_1D')
	ax = fig.add_subplot(111)
	ax.set_xlim([-3.,L+3])
	ax.set_ylim([-2.,2.])

	t = linspace(0,L,2)
	zeros_tab = zeros(2)
	plt.plot(t,zeros_tab,'-', color='blue')
    
	pts = []
    
	for i in range(nbr_particules):
		pts += ax.plot([], [], marker="o")

	for n in range(1, N):
		for pt,i in zip(pts,range(nbr_particules)):
			pt.set_data(pos_old[i],0)
		pos_next = (pos_old + h * vit_old) % L
		vit_next = calc_vit(h,nbr_particules,pos_old,vit_old,L)
		pos_old = pos_next
		vit_old = vit_next
		plt.pause(0.001)

	plt.show()

# affiche en même temps l'animation et l'espace des phases des particules en utilisant euler explicite
def phases_particules_anime_euler_explicite(T, N, L, nbr_particules):
	h = T/N
	pos = zeros((N, nbr_particules))
	vit = zeros((N, nbr_particules))

	for i in range(nbr_particules):
		pos[0,i] = random.randint(0,L)
	for i in range(nbr_particules):
		vit[0,i] = random.uniform(2,5)

	pos_old = pos[0]
	vit_old = vit[0]
	fig = plt.figure('particules_1D')
	ax = fig.add_subplot(121)

	for i in range(N):
		pos_next = (pos_old + h * vit_old) % L
		vit_next = calc_vit(h,nbr_particules,pos_old,vit_old,L)
		pos[i] = pos_next
		vit[i] = vit_next
		pos_old = pos_next
		vit_old = vit_next
	
	for i in range(nbr_particules):
		p = pos[:N,i]
		v = vit[:N,i]	
		plt.plot(p, v, '-')

	ax = fig.add_subplot(122)
	ax.set_xlim([-3.,L+3])
	ax.set_ylim([-2.,2.])

	t = linspace(0,L,2)
	zeros_tab = zeros(2)
	plt.plot(t,zeros_tab,'-', color='blue')

	pts = []

	for i in range(nbr_particules):
		pts += ax.plot([], [], marker="o")

	pos_old = pos[0]
	vit_old = vit[0]
	for n in range(1, N):
		for pt,i in zip(pts,range(nbr_particules)):
			pt.set_data(pos_old[i],0)
		pos_next = pos[n]
		vit_next = vit[n]
		pos_old = pos_next
		vit_old = vit_next
		plt.pause(0.001)

	plt.show()

# affiche en même temps l'animation et l'espace des phases des particules en utilisant euler symplectique
def phases_particules_anime_euler_symplectique(T, N, L, nbr_particules):
	h = T/N
	pos = zeros((N, nbr_particules))
	vit = zeros((N, nbr_particules))

	for i in range(nbr_particules):
		pos[0,i] = random.randint(0,L)
	for i in range(nbr_particules):
		vit[0,i] = random.uniform(2,5)

	pos_old = pos[0]
	vit_old = vit[0]
	fig = plt.figure('particules_1D')
	ax = fig.add_subplot(121)

	for i in range(N):
		pos_next = (pos_old + h * vit_old) % L
		vit_next = calc_vit(h,nbr_particules,pos_next,vit_old,L)
		pos[i] = pos_next
		vit[i] = vit_next
		pos_old = pos_next
		vit_old = vit_next

	for i in range(nbr_particules):
		p = pos[:N,i]
		v = vit[:N,i]	
		plt.plot(p, v, '-')

	ax = fig.add_subplot(122)
	ax.set_xlim([-3.,L+3])
	ax.set_ylim([-2.,2.])

	t = linspace(0,L,2)
	zeros_tab = zeros(2)
	plt.plot(t,zeros_tab,'-', color='blue')

	pts = []

	for i in range(nbr_particules):
		pts += ax.plot([], [], marker="o")

	pos_old = pos[0]
	vit_old = vit[0]
	for n in range(1, N):
		for pt,i in zip(pts,range(nbr_particules)):
			pt.set_data(pos_old[i],0)
		pos_next = pos[n]
		vit_next = vit[n]
		pos_old = pos_next
		vit_old = vit_next
		plt.pause(0.001)

	plt.show()

# affiche l'espace des phases des particules en faisant les calculs par la methode d'euler symplectique
def phases_explicite_symplectique(T, N, L, nbr_particules):
	h = T/N
	pos = zeros((N, nbr_particules))
	vit = zeros((N, nbr_particules))

	for i in range(nbr_particules):
		pos[0,i] = random.randint(0,L)

	for i in range(nbr_particules):
		vit[0,i] = random.uniform(0,5)

	pos_old = pos[0]
	vit_old = vit[0]
	fig = plt.figure('particules_1D')
	ax = fig.add_subplot(121)

	for i in range(N):
		pos_next = (pos_old + h * vit_old) % L
		vit_next = calc_vit(h,nbr_particules,pos_old,vit_old,L)
		pos[i] = pos_next
		vit[i] = vit_next
		pos_old = pos_next
		vit_old = vit_next

	for i in range(nbr_particules):
		p = pos[:N,i]
		v = vit[:N,i]	
		plt.plot(p, v, '-')

	ax = fig.add_subplot(122)

	for i in range(N):
		pos_next = (pos_old + h * vit_old) % L
		vit_next = calc_vit(h,nbr_particules,pos_next,vit_old,L)
		pos[i] = pos_next
		vit[i] = vit_next
		pos_old = pos_next
		vit_old = vit_next

	for i in range(nbr_particules):
		p = pos[:N,i]
		v = vit[:N,i]	
		plt.plot(p, v, '-')

	plt.show()

T = 100
N = 1000
L = 100
nbr_particules = 2

#phases_euler_explicite(T,N,L,nbr_particules)
#particules_anime_euler_explicite(T,N,L,nbr_particules)
#phases_particules_anime_euler_explicite(T,N,L,nbr_particules)
#phases_particules_anime_euler_symplectique(T,N,L,nbr_particules)
phases_explicite_symplectique(T,N,L,nbr_particules)