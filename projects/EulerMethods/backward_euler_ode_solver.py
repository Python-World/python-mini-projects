import matplotlib.pyplot as plt
import numpy as np

def feval(funcName, *args):
    return eval(funcName)(*args)


def backwardEuler(func, yinit, x_range, h):
    m = len(yinit)
    n = int((x_range[-1] - x_range[0])/h)

    x = x_range[0]
    y = yinit

    xsol = np.empty(0)
    xsol = np.append(xsol, x)

    ysol = np.empty(0)
    ysol = np.append(ysol, y)

    for i in range(n):
        yprime = feval(func, x+h, y)/(1+h)

        for j in range(m):
            y[j] = y[j] + h*yprime[j]

        x += h
        xsol = np.append(xsol, x)

        for r in range(len(y)):
            ysol = np.append(ysol, y[r])  # Saves all new y's

    return [xsol, ysol]


def myFunc(x, y):
    '''
    We define our ODEs in this function.
    '''
    dy = np.zeros((len(y)))
    dy[0] = 3*(1+x) - y[0]
    return dy


h = 0.2
x = np.array([1.0, 2.0])
yinit = np.array([4.0])


[ts, ys] = backwardEuler('myFunc', yinit, x, h)


# Calculates the exact solution, for comparison
dt = int((x[-1] - x[0]) / h)
t = [x[0]+i*h for i in range(dt+1)]
yexact = []
for i in range(dt+1):
    ye = 3 * t[i] + np.exp(1 - t[i])
    yexact.append(ye)


plt.plot(ts, ys, 'r')
plt.plot(t, yexact, 'b')
plt.xlim(x[0], x[1])
plt.legend(["Backward Euler method",
            "Exact solution manually computed"], loc = 2)
plt.xlabel('x', fontsize = 10)
plt.ylabel('y', fontsize = 10)
plt.tight_layout()
plt.show()
