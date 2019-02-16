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

'''
# affiche l'espace des phases des particules en faisant les calculs par la methode d'euler explicite avec un champs electrique pondere
def phases_euler_explicite_pond(T, N, L, I, nbr_particules):
	h = T/N
	pos = zeros((N, nbr_particules))
	vit = zeros((N, nbr_particules))

	for i in range(nbr_particules):
		pos[0,i] = random.randint(0,L)

	for i in range(nbr_particules):
		vit[0,i] = random.uniform(10,15)

	pos_old = pos[0]
	vit_old = vit[0]
	fig = plt.figure('particules_1D')
	ax = fig.add_subplot(111)
	
	field = zeros(I+1)
	for i in range(I+1):
		field[i] = sin(((2*pi)/L)*i) * (me/qe)

	for i in range(N):
		pos_next = (pos_old + h * vit_old) % L
		vit_next = calc_vit_pond(h,nbr_particules,pos_old,vit_old,L,field)
		pos[i] = pos_next
		vit[i] = vit_next
		pos_old = pos_next
		vit_old = vit_next

	for i in range(nbr_particules):
		p = pos[:N,i]
		v = vit[:N,i]	
		plt.plot(p, v, '-')

	plt.show()

# affiche la simulation du mouvement des particules avec euler explicite avec un champ electrique pondere
def particules_anime_euler_explicite_pond(T, N, L, I, nbr_particules):
	h = T/N
	pos_old = zeros(nbr_particules)
	for i in range(nbr_particules):
		pos_old[i] = random.randint(0,L)

	vit_old = zeros(nbr_particules)
	for i in range(nbr_particules):
		vit_old[i] = random.uniform(2,4)

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
    
	field = zeros(I+1)
	for i in range(I+1):
		field[i] = sin(((2*pi)/L)*i) * (me/qe)

	for n in range(1, N):
		for pt,i in zip(pts,range(nbr_particules)):
			pt.set_data(pos_old[i],0)
		pos_next = (pos_old + h * vit_old) % L
		vit_next = calc_vit_pond(h,nbr_particules,pos_old,vit_old,L,field)
		pos_old = pos_next
		vit_old = vit_next
		plt.pause(0.001)

	plt.show()

# affiche en même temps l'animation et l'espace des phases des particules en utilisant euler explicite avec un champs electrique pondere
def phases_particules_anime_euler_explicite_pond(T, N, L, I, nbr_particules):
	h = T/N
	pos = zeros((N, nbr_particules))
	vit = zeros((N, nbr_particules))

	for i in range(nbr_particules):
		pos[0,i] = random.randint(0,L)

	for i in range(nbr_particules):
		vit[0,i] = random.uniform(2,4)

	pos_old = pos[0]
	vit_old = vit[0]
	fig = plt.figure('particules_1D')
	ax = fig.add_subplot(121)
	
	field = zeros(I+1)
	for i in range(I+1):
		field[i] = sin(((2*pi)/L)*i) * (me/qe)

	for i in range(N):
		pos_next = (pos_old + h * vit_old) % L
		vit_next = calc_vit_pond(h,nbr_particules,pos_old,vit_old,L,field)
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

# affiche en même temps l'animation et l'espace des phases des particules en utilisant euler symplectique avec un champs electrique pondere
def phases_particules_anime_euler_symplectique_pond(T, N, L, I, nbr_particules):
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

	field = zeros(I+1)
	for i in range(I+1):
		field[i] = sin(((2*pi)/L)*i) * (me/qe)

	for i in range(N):
		pos_next = (pos_old + h * vit_old) % L
		vit_next = calc_vit_pond(h,nbr_particules,pos_next,vit_old,L,field)
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

# affiche l'espace des phases des particules en faisant les calculs par la methode d'euler symplectique avec un champs electrique pondere
def phases_explicite_symplectique_pond(T, N, L, I, nbr_particules):
	h = T/N
	pos = zeros((N, nbr_particules))
	vit = zeros((N, nbr_particules))

	for i in range(nbr_particules):
		pos[0,i] = (float)(random.randint(0,L))

	for i in range(nbr_particules):
		vit[0,i] = random.uniform(0,5)

	pos_old = pos[0]
	vit_old = vit[0]
	fig = plt.figure('particules_1D')
	ax = fig.add_subplot(121)

	field = zeros(I+1)
	for i in range(I+1):
		field[i] = sin(((2*pi)/L)*i) * (me/qe)

	for i in range(N):
		pos_next = (pos_old + h * vit_old) % L
		vit_next = calc_vit_pond(h,nbr_particules,pos_old,vit_old,L,field)
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
		vit_next = calc_vit_pond(h,nbr_particules,pos_next,vit_old,L,field)
		pos[i] = pos_next
		vit[i] = vit_next
		pos_old = pos_next
		vit_old = vit_next

	for i in range(nbr_particules):
		p = pos[:N,i]
		v = vit[:N,i]	
		plt.plot(p, v, '-')

	plt.show()
'''

# renvoie la valeur du champs electrique au point x, prenant en parametre la longueur du segment L
# le calcul est fait en faisant une ponderation sur les deux points connus du champs les plus proche
def electric_field_pond(field, x, L, I):
	n = math.floor((I/L)*x)
	inf = n
	sup = n+1
	alpha = x - n * L/I
	#print(str(inf)+" < "+str(x)+" < "+str(sup)+"    alpha:"+str(alpha))
	return alpha * field[sup] + (1-alpha) * field[inf]

# renvoie le vecteur contenant les nouvelle vitesse des particules
def calc_vit_pond(h, nbr_particules, pos_old, vit_old, L, field, I):
	vit_new = zeros(nbr_particules)
	for i in range(nbr_particules):
		vit_new[i] = vit_old[i] - h*(qe/me)*electric_field_pond(field,pos_old[i],L,I)
	return vit_new

def compare_symplectique_pond(T, N, L, I, nbr_particules):
	h = T/N
	pos = zeros((N, nbr_particules))
	vit = zeros((N, nbr_particules))

	for i in range(nbr_particules):
		pos[0,i] = random.uniform(0,L)
	for i in range(nbr_particules):
		vit[0,i] = random.uniform(0.1,15)
	mem_pos_ini = zeros(nbr_particules)
	mem_vit_ini = zeros(nbr_particules)	
	for i in range(nbr_particules):
		mem_pos_ini[i] = pos[0,i]
		mem_vit_ini[i] = vit[0,i]
	
	fig = plt.figure('particules_1D')
	'''ax = fig.add_subplot(131)
	pos_old = pos[0]
	vit_old = vit[0]
	field = zeros(L+1)
	for i in range(L+1):
		field[i] = sin(((2*pi)/L)*i) * (me/qe)
		#print("L:"+str(L)+"   i:"+str(i))
	field[L] = 0
	for i in range(N):
		pos_next = (pos_old + h * vit_old) % L
		vit_next = calc_vit_pond(h,nbr_particules,pos_next,vit_old,L,field,L)
		pos[i] = pos_next
		vit[i] = vit_next
		pos_old = pos_next
		vit_old = vit_next
	for i in range(nbr_particules):
		p = pos[:N,i]
		v = vit[:N,i]
		plt.plot(p, v, '-')
	print()'''
	ax = fig.add_subplot(131)
	pos_old = pos[0]
	vit_old = vit[0]
	field = zeros(I+1)
	for i in range(I+1):
		# formule a ameliorer : on peut certainement la simplifier
		field[i] = sin(((2*pi)/L)*i*(L/I)) * (me/qe)
		#print("L:"+str(L)+"   i:"+str(i*(L/I)))
	# la derniere valeur duc champs est saisie a la main car si on calcule sin(2*pi) on ne trouve pas 0
	# je pense que c'est du a une trop faible precision de calcul
	field[I] = 0
	for i in range(N):
		pos_next = (pos_old + h * vit_old) % L
		vit_next = calc_vit_pond(h,nbr_particules,pos_next,vit_old,L,field,I)
		pos[i] = pos_next
		vit[i] = vit_next
		pos_old = pos_next
		vit_old = vit_next
	for i in range(nbr_particules):
		p = pos[:N,i]
		v = vit[:N,i]
		plt.plot(p, v, '-')

	ax = fig.add_subplot(132)
	pos = zeros((N, nbr_particules))
	vit = zeros((N, nbr_particules))
	for i in range(nbr_particules):
		pos[0,i] = mem_pos_ini[i]
		vit[0,i] = mem_vit_ini[i]
	pos_old = pos[0]
	vit_old = vit[0]
	field = zeros(I*10+1)
	for i in range(I*10+1):
		# formule a ameliorer : on peut certainement la simplifier
		field[i] = sin(((2*pi)/L)*i*(L/(I*10))) * (me/qe)
		#print("L:"+str(L)+"   i:"+str(i*(L/(I*10))))
	# la derniere valeur duc champs est saisie a la main car si on calcule sin(2*pi) on ne trouve pas 0
	# je pense que c'est du a une trop faible precision de calcul
	field[I*10] = 0

	for i in range(N):
		pos_next = (pos_old + h * vit_old) % L
		vit_next = calc_vit_pond(h,nbr_particules,pos_next,vit_old,L,field,I*10)
		pos[i] = pos_next
		vit[i] = vit_next
		pos_old = pos_next
		vit_old = vit_next
	for i in range(nbr_particules):
		p = pos[:N,i]
		v = vit[:N,i]
		plt.plot(p, v, '-')

	ax = fig.add_subplot(133)
	pos = zeros((N, nbr_particules))
	vit = zeros((N, nbr_particules))
	for i in range(nbr_particules):
		pos[0,i] = mem_pos_ini[i]
		vit[0,i] = mem_vit_ini[i]
	pos_old = pos[0]
	vit_old = vit[0]
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
N = 100000
L = 1000
I = 10
nbr_particules = 3
# 1er graphe : I
# 2e graphe : I * 10
# 3e graphe : sans discrétisation champs continue

#phases_euler_explicite_pond(T,N,L,I,nbr_particules)
#particules_anime_euler_explicite_pond(T,N,L,I,nbr_particules)
#phases_particules_anime_euler_explicite_pond(T,N,L,I,nbr_particules)
#phases_particules_anime_euler_symplectique_pond(T,N,L,I,nbr_particules)
#phases_explicite_symplectique_pond(T,N,L,I,nbr_particules)
compare_symplectique_pond(T,N,L,I,nbr_particules)