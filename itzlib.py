import math

# So itz my lib bruuh

    #itz about ballz

#2 same colour ballz

def Cof2(jel, sum):
    return (math.factorial(jel) / (math.factorial(2) * math.factorial(jel-2))) / (math.factorial(sum) / (math.factorial(2) * math.factorial(sum-2)))

#Herez example prog
# gh = True
# a = int(input("Белых шаров: "))
# b = int(input("Черных шаров: "))
# c = a+b
#
# while (gh == True):
#     d = input("Мы найдём вероятность взятия двух шаров цвета.. ")
#     if (d == "Белого"):
#         print(Cof2(a, c))
#         gh = False
#     if (d == "Черного"):
#         print(Cof2(a, c))
#         gh = False

#2 dif colour ballz

def CofTwo(one, two, sum):
    return (one*two) / (math.factorial(sum) / (math.factorial(2) * math.factorial(sum-2)))

#Herez an example
# a = int(input("Кол-во белых шаров: "))
# b = int(input("Черных шаров: "))
# c = a+b
#
# print(CofTwo(a, b, c))