from matplotlib import pyplot as plt
from numpy import *

q = -1.6021766208e-19
qe = -q
me = 9.109e-31

#fct p-periodique : sin((2*pi/p)*x)
# il ne faut pas que la valeur soit 0 sinon la vitesse est nulle ==> la particule ne bouge plus
def electric_field(x, L):
	return (sin(pi/L*x)+0.1)*(-me/qe)

def calc_vit(nb_particules, pos, L):
	vit = zeros(nb_particules)
	for i in range(nb_particules):
		vit[i] = (-qe/me)*electric_field(pos[i],L)
	return vit

# faire avec euler symplectique
def particules_euler_explicite(dt, N, L, nb_particules):
	length = (int)(math.floor(N/dt))
	pos = zeros((length, nb_particules))
	vit = zeros((length, nb_particules))

	for i in range(nb_particules):
		pos[0,i] = random.randint(0,L)

	for i in range(nb_particules):
		vit[0,i] = random.uniform(0.1,1)

	pos_old = pos[0]
	vit_old = vit[0]
	fig = plt.figure('particules_1D')
	ax = fig.add_subplot(111)

	for i in range(length):
		pos_next = (pos_old + dt * vit_old) % L
		vit_next = calc_vit(nb_particules,pos_old,L)
		pos[i] = pos_next
		vit[i] = vit_next
		pos_old = pos_next
		vit_old = vit_next

	for i in range(nb_particules):
		p = pos[:length,i]
		v = vit[:length,i]	
		plt.plot(p, v, '-')
	plt.show()

def particules_anime_euler_explicite(dt, N, L, nb_particules):
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
		for pt,i in zip(pts,range(nb_particules)):
			pt.set_data(pos_old[i],0)
		pos_next = (pos_old + dt * vit_old) % L
		vit_next = calc_vit(nb_particules,pos_old,L)
		pos_old = pos_next
		vit_old = vit_next

		plt.pause(0.001)

particules_euler_explicite(1,200,100,10)
#particules_anime_euler_explicite(1,200,100,10)