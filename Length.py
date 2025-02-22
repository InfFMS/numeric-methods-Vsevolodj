# cos(x)
# cos(x) + 0.1*x2
# -tanh(x-π/2)
# -0.2*(x- π)3 + 0.5*(x- π)2 +1
import matplotlib.pyplot as plt
import numpy as np
pi = np.pi
fig, ax = plt.subplots() #create graph
x = np.linspace(0, pi, 1000)  # 1000 scatters in [0;π]
def f1(x):
    y = []
    for i in range(0,len(x)):
        y = y+[np.cos(x[i])]
    return y
def f1l(x):
    return np.cos(x)
def f2(x):
    y = []
    for i in range(0,len(x)):
        y = y+[np.cos(x[i])+ 0.1*x[i]**2]
    return y
def f2l(x):
    return np.cos(x)+ 0.1*x**2
def f3(x):
    y = []
    for i in range(0,len(x)):
        y = y+[-np.tanh(x[i]-pi/2)]
    return y
def f3l(x):
    return -np.tanh(x-pi/2)
def f4(x):
    y = []
    for i in range(0,len(x)):
        y = y+[-0.2*(x[i]- pi)**3 + 0.5*(x[i]- pi)**2 +1]
    return y
def f4l(x):
    return -0.2*(x-pi)**3 + 0.5*(x- pi)**2 +1
ax.plot(x, f1(x), label="Graph1")# create graphs
ax.plot(x, f2(x), label="Graph2")
ax.plot(x, f3(x), label="Graph3")
ax.plot(x, f4(x), label="Graph4")
ax.set_title("Hills")
ax.set_ylabel("Y", fontsize=10, color='black', labelpad=0)
ax.set_xlabel("X", fontsize=10, color='black', labelpad=0)
def length(f,x):
    length = 0
    for i in range(1, len(x)):
        length += ((pi/1000)**2+(f(x[i])-f(x[i-1]))**2)**0.5
    return length
print("length1:",length(f1l,x))
print("length2:",length(f2l,x))
print("length3:",length(f3l,x))
print("length4:",length(f4l,x))
plt.show()
