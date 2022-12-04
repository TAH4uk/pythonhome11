# Задача 1. Постройте график функции f(x) = 5*x^2 + 10*x - 30.
# По графику определите, при каких значения x значение функции отрицательно.

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-5, 4.01, 0.01)
y = 5*x*x + 10*x - 30
s = np.sign(y)
zero = []
for i in range(len(y)):
        if s[i-1] + s[i] == 0:
            zero.append(i)
plt.title("График функции")
ax = plt.gca()
ax.grid(which='major', color = 'k')
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.annotate("1.65", xy=(1.65, 0),  xycoords='data',
            xytext=(0.8, 0.8), textcoords='axes fraction',
            arrowprops=dict(arrowstyle = "->"),
            horizontalalignment='right', verticalalignment='top',
            )
ax.annotate("-3.64", xy=(-3.64, 0),  xycoords='data',
            xytext=(0.2, 0.8), textcoords='axes fraction',
            arrowprops=dict(arrowstyle = "->"),
            horizontalalignment='left', verticalalignment='bottom',
            )

plt.plot(x, y)
plt.plot([x[i] for i in zero], [y[i] for i in zero], "ro")

znach = []
for i in zero:
    znach.append(x[i])

min = round(znach[0], 2)
max = round(znach[1], 2)
print(f"Значение функции отрицательно при значениях х в промежутке от {min} до {max} (отмечены красными точками на графике функции).")
plt.show()

