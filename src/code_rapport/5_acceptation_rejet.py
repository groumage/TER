from matplotlib import pyplot as plt
import random as random
import numpy as np
import time as time

loop = 5
N = 100000

# utiliser python 3.6 et non des version d'avant car les arrondis sont incorrectes

total_time = 0
for l in range(loop):
	tmp1 = time.clock()
	x = []
	y = []
	for i in range(N):
		alpha = random.uniform(0,1)
		c = float((1**2)+1+1/6)
		beta = random.uniform(0,1) * c
		if (beta <= float((alpha**2)+alpha+1/6)):
			x.append(alpha)
			y.append(beta)
	tmp2 = time.clock()
	total_time += tmp2 - tmp1
	'''X = np.linspace(0,1,len(x))
	Y = [float((x**2)+x+1/6) for x in X]
	plt.plot(X,Y)
	plt.plot(x,y,'x')
	plt.show()'''
print("Méthode 1 : " + str(total_time/loop) + " sec")

total_time = 0
for l in range(loop):
	tmp1 = time.clock()
	x_pts = []
	y_pts = []
	c = float((1**2)+1+1/6)
	for i in range(N):
		x_pts.append(random.uniform(0,1))
		y_pts.append(random.uniform(0,1) * c)

	x_true_points = []
	y_true_points = []
	for i in range(N):
		if (y_pts[i] <= float((x_pts[i]**2)+x_pts[i]+1/6)):
			x_true_points.append(x_pts[i])
			y_true_points.append(y_pts[i])
	tmp2 = time.clock()
	total_time += tmp2 - tmp1
	'''
	l = (int)(len(y_true_points))
	X = np.linspace(0,1,l)
	Y = [float((x**2)+x+1/6) for x in X]
	plt.plot(X,Y)
	plt.plot(x_true_points,y_true_points,'x')
	plt.show()'''
print("Méthode 2 : " + str(total_time/loop) + " sec")

x = []
y = []
for i in range(N):
	alpha = random.uniform(0,1)
	c = float((1*1)+1+1/6)
	beta = random.uniform(0,1) * c
	if (beta <= float((alpha**2)+alpha+1/6)):
		x.append(alpha)
		y.append(beta)
X = np.linspace(0,1,len(x))
Y = [float((x**2)+x+1/6) for x in X]
plt.plot(X,Y)
plt.plot(x,y,'x')
plt.show()