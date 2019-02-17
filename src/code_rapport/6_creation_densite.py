from matplotlib import pyplot as plt
import random as random
import numpy as np
import time as time

N = 10
nbr_pts = 100

fig = plt.figure('Densité')
fig.suptitle("Détermination d'une densité à partir d'un nuage de points")
ax = fig.add_subplot(121)

pts = []
for i in range(nbr_pts):
	alpha = random.uniform(0,1)
	c = float((1*1)+1+1/6)
	beta = random.uniform(0,1) * c
	if (beta <= float((alpha**2)+alpha+1/6)):
		pts.append([alpha,beta])
X_densite = np.linspace(0,1,N)
Y_densite = [float((x**2)+x+1/6) for x in X_densite]
plt.plot(X_densite,Y_densite)
X_pts = [pts[x][0] for x in range(len(pts))]
Y_pts = [pts[x][1] for x in range(len(pts))]
plt.plot(X_pts, Y_pts, 'x')

pts.sort()

ax = fig.add_subplot(122)

start_list = 0
l = len(pts)
x = np.linspace(0,1,N)
y = np.zeros(N)
tmp1 = time.clock()
for i in range(N-1):
	nbr_particules = 0
	for j in range(start_list,l):
		if (i/N <= pts[j][0] <= (i+1)/N):
			nbr_particules += 1
		else:
			y[i] = nbr_particules
			start_list = j
			break

nbr_particules = 0
for i in range(start_list,l):
	if(((N+(N-1))/2)/N <= pts[i][0] <= 1):
		nbr_particules += 1
y[N-1] = 2 * nbr_particules

tmp2 = time.clock()

print("Temps : " + str(tmp2-tmp1) + " sec")

plt.plot(x,y,'-')
plt.show()

'''
x = []
y = []
for i in range(nbr_pts):
	alpha = random.uniform(0,1)
	c = float((1*1)+1+1/6)
	beta = random.uniform(0,1) * c
	if (beta <= float((alpha**2)+alpha+1/6)):
		x.append(alpha)
		y.append(beta)
X = np.linspace(0,1,len(x))
Y = [float((x**2)+x+1/6) for x in X]
plt.plot(x,y,'x')
plt.plot(X,Y)

ax = fig.add_subplot(122)
l = len(x)
x_densite = np.linspace(0,1,N)
y_densite = np.zeros(N)
x.sort()
'''

'''
tmp1 = time.clock()
for i in range(N-1):
	nbr_particules = 0
	for j in range(l):
		if (i/N <= x[j] <= (i+1)/N):
			nbr_particules += 1
	y_densite[i] = nbr_particules

nbr_particules = 0
for i in range(l):
	if(((N+(N-1))/2)/N <= x[i] <= 1):
		nbr_particules += 1
y_densite[N-1] = 2 * nbr_particules
tmp2 = time.clock()

print("Temps : " + str(tmp2-tmp1) + " sec")

plt.subplots_adjust(wspace=0.5)

plt.plot(x_densite,y_densite,'-')
plt.show()'''