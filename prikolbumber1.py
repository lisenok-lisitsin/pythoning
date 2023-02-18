import random as rnd
import itertools as it
a = int(input("Сколько чисел в пуле: "))
meow = list()
count = 0
for i in range(a):
    g = rnd.randint(-1000, 1000)
    if (g == 0):
        break
    meow.append(g)
print(meow)
sac = len(list(it.groupby(meow, lambda meow: meow > 0)))
print("Знак меняется: " + str(sac-1) + " раз")