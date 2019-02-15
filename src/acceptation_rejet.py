from random import random
from matplotlib import pyplot as plt
from numpy import *

# utiliser python 3.6 et non des version d'avant car les arrondis sont incorrectes

# la fonction de densite utilise est f(x)=x*x+x+1/6 sur [0;1]
def densite(x):
	return float((x*x)+x+1/6)

def uniforme(a,b):
	return (a+(b-a)*random.random())

def tirage():
	x = []
	y = []
	for i in range(1000):
		alpha = uniforme(0,1)
		c = densite(1)
		beta = uniforme(0,1) * c
		if (beta <= densite(alpha)):
			x.append(alpha)
			y.append(beta)
	X = linspace(0,1,len(x))
	Y = [densite(x) for x in X]
	plt.plot(X,Y)
	plt.plot(x,y,'x')
	plt.show()

tirage()