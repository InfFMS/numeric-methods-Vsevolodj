import matplotlib.pyplot as plt
import numpy as np
# Data
e = 2.718281828
x = np.linspace(-2, 2, 1000)  # 1000 scatters in [-2;2]
x1 =  np.linspace(0.0001, 2, 500)  # 1000 scatters in [-2;2]
def f1(x):
    return x**3-x+1
def f2(x):
    return x**3-x**2-9*x+9
def f3(x):
    return x**2-e**x
def f4(x):
    # i = 0
    # while x[i]!=0:
    #     i+=1
    # x = x[i:]
    return 5*x-6*np.log(x)-7
def f5(x):
    return np.cos(x)+2*x-3
def f1(x):
    return x**3-x+1
def f2(x):
    return x**3-x**2-9*x+9
def f3(x):
    return x**2-e**x
def f4(x):
    return 5*x-6*np.log(x)-7
def f5(x):
    return np.cos(x)+2*x-3
def soluion(f, b1, b2):
    eps = 10**(-2)
    while b2-b1>2*eps:
        c = (b1+b2) / 2
        if f(b1)*f(c)<=0:
            b2=c
        else: b1=c
    return c
print("first",soluion(f1,-2,-1))
print("second",soluion(f2,0.5,1.5))
print("third",soluion(f3,-2,-1))
print("fourth",soluion(f4,0.001,0.5))
print("fifth",soluion(f5,0,1.8))
# Create graph
plt.plot(x, f1(x), label="y1")
plt.plot(x, f2(x), label="y2")
plt.plot(x, f3(x), label="y3")
plt.plot(x1, f4(x1), label="y4")
plt.plot(x, f5(x), label="y5")
# Setings
plt.title("Graphs")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.grid(True)  # grid graphics
plt.show()
