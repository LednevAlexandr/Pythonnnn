# реализовать алгоритм перемешивания списка
from random import *
a =[i for i in range(1,10)]
def ser(a):
    for i in range(len(a)-1):
       temp = a[i]
       index = randint(i+1,len(a)-1)
       a[i]=a[index]
       a[index]=temp
    return a
        
print(a)
b=ser(a)
print(b)