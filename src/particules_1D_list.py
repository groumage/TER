from matplotlib import pyplot as plt
from numpy import *

def particule_anime(dt, N, L, nb_particules):
	pos = []
	for i in range(nb_particules):
		pos.append(random.randint(0,L))

	vit = []
	for i in range(nb_particules):
		vit.append(random.uniform(0.1,1))

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
			pos[i] = (pos[i] + dt * vit[i]) % L
			pt.set_data(pos[i],0)

		plt.pause(0.001)

particule_anime(1,1000,100,10)