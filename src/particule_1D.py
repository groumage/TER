from matplotlib import pyplot as plt
from numpy import *

def particule_anime(dt, N, L, nb_particules):
	pos_ini = zeros(nb_particules)
	for i in range(nb_particules):
		pos_ini[i] = random.randint(0,L)

	vit_ini = zeros(nb_particules)
	for i in range(nb_particules):
		vit_ini[i] = random.uniform(0.1,1)

	length = (int)(math.floor(N/dt))
	pos_old = pos_ini
	vit_old = vit_ini
	
	x = zeros((length, nb_particules))
	x[0] = array([pos_ini[0] for _ in range(nb_particules)])
    
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
		x[n] = array([pos_next[i] for i in range(nb_particules)])
		pos_old = pos_next
        
		for pt,i in zip(pts,range(nb_particules)):
			pt.set_data(x[n,i],0)
            
		plt.pause(0.001)

particule_anime(1,1000,100,10)