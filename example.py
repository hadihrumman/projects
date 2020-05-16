from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

data = np.array([[0,0,0,10,0,0,0],
                 [0,0,0,10,0,0,0],
                 [0,0,0,10,0,0,0],
                 [0,0,0,10,0,0,0],
                 [0,0,1,10,0,0,0],
                 [0,0,0,10,10,0,0],
                 [0,0,0,10,0,0,0], ])
fig = plt.figure()
ax = Axes3D(fig)

lx= len(data[0])           
ly= len(data[:,0])
xpos = np.arange(0,lx,1)    
ypos = np.arange(0,ly,1)
xpos, ypos = np.meshgrid(xpos+0.5, ypos+0.5)

xpos = xpos.flatten()
ypos = ypos.flatten()
zpos = np.ones(lx*ly)*1e-10

dx = 1. * np.ones_like(zpos)
dy = dx.copy()
dz = data.flatten()

ax.bar3d(xpos,ypos,zpos, dx, dy, dz,  color='b', alpha=1., zsort='max')
plt.ion()
plt.show()
