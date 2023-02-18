import random as rnd
a = int(input("Сколько чисел в пуле: "))
meow = list()
g = rnd.randint(-1000, 1000)
for i in range(a):
    g = (round(rnd.uniform(-1000, 1000), 2))
    meow.append(g)
print(meow)
if (len(set(meow)) == len(meow)):
    print("Мать в шоколаде! - Все числа уникальны")
else:
    print("Шоколад в мате! - Числа не уникальны")