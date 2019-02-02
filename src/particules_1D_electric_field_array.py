from matplotlib import pyplot as plt
from numpy import *

q = 1.6021766208e-19
me = 9.109e-31

#fct p-periodique : sin((2*pi/p)*x)
# il ne faut pas que la valeur soit 0 sinon la vitesse est nulle ==> la particule ne bouge plus
def electric_field(x, L):
	return sin(pi/L*x)+0.1

def calc_vit(nb_particules, pos, L):
	vit = zeros(nb_particules)
	for i in range(nb_particules):
		#vit[i] = (-q/me)*electric_field(pos[i],L)
		vit[i] = electric_field(pos[i],L)
	return vit

def particule_anime(dt, N, L, nb_particules):
	pos_old = zeros(nb_particules)
	for i in range(nb_particules):
		pos_old[i] = random.randint(0,L)

	vit_old = zeros(nb_particules)
	for i in range(nb_particules):
		vit_old[i] = random.uniform(0.1,1)

	length = (int)(math.floor(N/dt))

	fig = plt.figure('particule_1D')
	ax = fig.add_subplot(111)
	ax.set_xlim([-3.,L+3])
	ax.set_ylim([-2.,2.])

	t = linspace(0,L,length)
	zeros_tab = zeros(length)
	plt.plot(t,zeros_tab,'-', color='blue')
    
	pts = []
    
	for i in range(nb_particules):
		pts += ax.plot([], [], marker="o",color='red')
        
	for n in range(1, length):
		pos_next = (pos_old + dt * vit_old) % L
		vit_next = calc_vit(nb_particules,pos_old,L)
		for pt,i in zip(pts,range(nb_particules)):
			pt.set_data(pos_next[i],0)
		pos_old = pos_next
		vit_old = vit_next
			#pos_old[i] = (pos_old[i] + dt * vit_old[i]) % L
		#pos_old = pos_next

		plt.pause(0.001)

particule_anime(1,1000,100,1)