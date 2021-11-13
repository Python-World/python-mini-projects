import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

print('The 3 equations are entered individually, each value of the equation is entered separated by a space, for example: \ninput = 6 5 -3 4 \nThis will be equal to 6x + 5y- 3z = 4')

print('Enter values for equation 1: ')
a, b, c, d = map(float, input().split()) 

print('Enter values for equation 2: ')
e, f, g, h = map(float, input().split())

print('Enter values for equation 3: ')
i, j, k, l = map(float, input().split())
#solve the linear equation
A = np.array([[a,b,c],[e,f,g],[i,j,k]])
b_a = np.array([d,h,l])
sol = np.linalg.solve(A,b_a)
print(sol)


x,y = np.linspace(0,10,10), np.linspace(0,10,10)
X,Y = np.meshgrid(x,y)

Z1 = (d-a*X-b*Y)/c
Z2 =(h-e*X-f*Y)/g
Z3 =(l+X-Y)/k

#create 3d graphics

fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')
ax.plot_surface(X,Y,Z1,alpha=0.5,cmap=cm.Accent,rstride=100,cstride=100)
ax.plot_surface(X,Y,Z2,alpha=0.5,cmap=cm.Paired,rstride=100,cstride=100)
ax.plot_surface(X,Y,Z3,alpha=0.5,cmap=cm.Pastel1,rstride=100,cstride=100)
ax.plot((sol[0],),(sol[1],),(sol[2],),lw=2,c='k', marker='o', markersize=7, markeredgecolor='g', markerfacecolor='white')
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')

plt.show()


