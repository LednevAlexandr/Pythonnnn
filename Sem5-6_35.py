# В файле находится N натуральных чисел, записанных через пробел.
#  Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найти его.
from random import*
N=int(input())
a =[i for i in range(1,N)]
b =" ".join(map(str,a))
f = open('text_35.txt','w')
f.write(b)

