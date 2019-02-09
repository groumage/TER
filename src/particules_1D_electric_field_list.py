from matplotlib import pyplot as plt
from numpy import *

q = -1.6021766208e-19
qe = -q
me = 9.109e-31

#fct p-periodique : sin((2*pi/p)*x)
#il ne faut pas que la valeur soit 0 sinon la vitesse est nulle ==> la particule ne bouge plus
# fonction degre 2 : f(x) = ax^2 + bx + c = a(x-x1)(x-x2)
def electric_field(x, L):
	#return (sin(pi/L*x)+0.1)*(-me/qe)
	return ((-pow(10,-3)*x*(x-L)) + 0.1) * (-me/qe)

def particule_anime_euler_explicite(dt, N, L, nb_particules):
	pos_old = []
	for i in range(nb_particules):
		pos_old.append(random.randint(0,L))

	vit_old = []
	for i in range(nb_particules):
		vit_old.append(random.uniform(0.1,1))

	length = (int)(math.floor(N/dt))

	pos_ini = pos_old
	vit_ini = vit_old

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
			pos_next = (pos_old[i] + dt * vit_old[i]) % L
			vit_next = (-qe/me)*electric_field(pos_old[i],L)
			pos_old[i] = pos_next
			vit_old[i] = vit_next
			
		plt.pause(0.001)

particule_anime_euler_explicite(1,1000,100,100)