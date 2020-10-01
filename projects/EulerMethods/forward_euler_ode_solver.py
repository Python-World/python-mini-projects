
import matplotlib.pyplot as plt
import math

def feval(funcName, *args):

    return eval(funcName)(*args)


def forwardEuler(func, yinit, x_range, h):
    numOfODEs = len(yinit) # Number of ODEs
    sub_intervals = int((x_range[-1] - x_range[0])/h) # Number of sub-intervals

    x = x_range[0] # Initializes variables x
    y = yinit # Initializes variables y

    # Creates arrays for solutions
    xsol = [x]
    ysol = [y[0]]

    for i in range(sub_intervals):
        yprime = feval(func, x, y) # Evaluates dy/dx

        for j in range(numOfODEs):
            y[j] = y[j] + h * yprime[j] # Eq. (8.2)

        x += h # Increases the x-step
        xsol.append(x) # Saves it in the xsol array

        for r in range(len(y)):
            ysol.append(y[r]) # Saves all new y's

    return [xsol, ysol]


def myFunc(x, y):
    dy = [0] * len(y)
    dy[0] = 3 * (1 + x) - y[0]
    return dy


# Parameters
h = 0.5
x = [1.0, 2.0]
yinit = [4.0]


[ts, ys] = forwardEuler('myFunc', yinit, x, h)


# Exact solution, for comparison
dt = int((x[-1] - x[0]) / h)
t = [x[0]+i*h for i in range(dt+1)]
yexact = []
for i in range(dt+1):
    ye = 3 * t[i] + math.exp(1 - t[i])
    yexact.append(ye)


plt.plot(ts, ys, 'r')
plt.plot(t, yexact, 'b')
plt.xlim(x[0], x[1])
plt.legend(["Forward Euler method",
            "Exact solution manually computed"], loc = 2)
plt.xlabel('x', fontsize = 10)
plt.ylabel('y', fontsize = 10)
plt.tight_layout()
plt.show()
