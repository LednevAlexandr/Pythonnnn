# задать список из n чисел последовательности (1+1/n)^2 и вывести на экран их сумму.
from random import*
from math import*
def ran(n):
    a =[round((1+1/i)**2) for i in range(1,n+1)]
    print(a)
    result = sum(a)
    return result

a = ran(5)
print(a)