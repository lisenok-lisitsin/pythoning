import random as rnd
from statistics import mean
a = int(input("Сколько чисел в пуле: "))
meow = list()
moor = list()
g = rnd.randint(-1000, 1000)
for i in range(a):
    g = (round(rnd.uniform(-1000, 1000), 2))
    if (g == -1000):
        break
    if (g > 0):
        meow.append(g)
    if (g < 0):
        moor.append(g)
kek = mean(meow) # +
lol = mean(moor) # -
print("Положительные числа: " + str(meow))
print("Отрицательные числа: " + str(moor))
print("Ср. положительное число: " + str(kek))
print("Ср. отрицательное число: " + str(lol))