# Задача 2. Имеются данные о площади и стоимости 15 домов.
# Риелтору требуется узнать в каких домах стоимость квадратного метра меньше 50000 рублей.
# Предоставьте ему графические данные о стоимости квадратного метра каждого дома и список подходящих ему домов, отсортированных по площади.
# Данные о домах сформируйте случайным образом. Площади от 100 до 300 кв. метров, цены от 3 до 20 млн.


import matplotlib.pyplot as plt
import numpy as np
import random

home = 15
square = [random.randint(100, 300) for i in range(15)]
price = [random.randint(3000000, 20000000) for i in range(15)]

x = np.arange(1, 16)

sm = []
for i in range(len(price)):
    f = round(price[i] / square[i])
    sm.append(f)

s_price = []
numb = []
for i in range(len(sm)):
    if sm[i] < 50000:
        a = sm[i]
        s_price.append(a)
        b = i + 1
        numb.append(b)
print()
print(f"Стоимость подходящих домов: {s_price}")
print()
print(f"Подходящие дома: {numb}")

plt.title("Стоимость квадратного метра, руб.")
plt.text
plt.bar(x, sm)
plt.show()
