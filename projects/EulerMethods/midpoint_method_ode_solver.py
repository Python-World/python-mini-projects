import matplotlib.pyplot as plt
import math


def feval(funcName, *args):
    return eval(funcName)(*args)


def mult(vector, scalar):
    newvector = [0]*len(vector)
    for i in range(len(vector)):
        newvector[i] = vector[i]*scalar
    return newvector


def midpoint(func, yinit, x_range, h):
    numOfODEs = len(yinit)
    sub_intervals = int((x_range[-1] - x_range[0])/h)

    x = x_range[0]
    y = yinit

    xsol = [x]
    ysol = [y[0]]

    for i in range(sub_intervals):
        y0prime = feval(func, x, y)

        k1 = mult(y0prime, h/2)

        ypredictor = [u + v for u, v in zip(y, k1)]

        y1prime = feval(func, x+h/2, ypredictor)

        for j in range(numOfODEs):
            y[j] = y[j] + h*y1prime[j]

        x = x + h
        xsol.append(x)

        for r in range(len(y)):
            ysol.append(y[r])

    return [xsol, ysol]


def myFunc(x, y):
    dy = [0] * len(y)
    dy[0] = 3 * (1 + x) - y[0]
    return dy

# -----------------------

h = 0.2
x = [1.0, 2.0]
yinit = [4.0]


[ts, ys] = midpoint('myFunc', yinit, x, h)

# For a system of ODEs
#numOfODEs = len(yinit)
#ys1 = ys[0::numOfODEs]
#ys2 = ys[1::numOfODEs]
#etc

# Calculates the exact solution, for comparison
dt = int((x[-1] - x[0]) / h)
t = [x[0]+i*h for i in range(dt+1)]
yexact = []
for i in range(dt+1):
    ye = 3 * t[i] + math.exp(1 - t[i])
    yexact.append(ye)


plt.plot(ts, ys, 'r')
plt.plot(t, yexact, 'b')
plt.xlim(x[0], x[1])
plt.legend(["Midpoint method", "Exact solution"], loc=2)
plt.xlabel('x', fontsize=17)
plt.ylabel('y', fontsize=17)
plt.tight_layout()
plt.show()
