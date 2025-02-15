import matplotlib.pyplot as plt
import numpy as np

# Данные
x = np.linspace(-2, 2, 100)  # 100 точек от -10 до 10
y1 = x**3-x+1
y2 = x**3-x**2-9*x+9
# Построение графиков
plt.plot(x, y1, label="y1", color="blue")
plt.plot(x, y2, label="y2", color="green")
# Настройка
plt.title("Графики sin(x) и cos(x)")
plt.xlabel("Значения X")
plt.ylabel("Значения Y")
plt.legend()
plt.grid(True)  # Сетка на графике
plt.show()
def y1(x)
    return x**3-x+1
def soluion(f, a, b):
    c = (a+b) / 2
    x = f(y)

soluion(y1, 1,3)