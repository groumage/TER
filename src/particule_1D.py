from matplotlib import pyplot as plt
from numpy import *

pos_ini = array([5])

vit_ini = array([0.1])

def particule_anime(dt, N):
    length = (int)(math.floor(N/dt))
    pos_old = pos_ini
    vit_old = vit_ini
    x = zeros(length)
    y = zeros(length)

    x[0] = array([pos_ini[0]])
    y[0] = array([0])
    
    fig = plt.figure('particule_1D')
    ax = fig.add_subplot(111)
    ax.set_xlim([-10.,100.])
    ax.set_ylim([-5.,5.])
    
    pts = []
    
    for i in range(1):
        pts += ax.plot([], [], marker="o",color='blue')
        
    for n in range(1, length):
        pos_next = pos_old + dt * vit_old
        
        x[n] = array([pos_next[0]])
        
        pos_old = pos_next
        
        for pt,i in zip(pts,range(6)):
            pt.set_data(x[n],0)
            
        plt.pause(0.00001)
    
particule_anime(1,100)