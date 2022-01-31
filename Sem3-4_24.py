#24 в заданном списке вещественных чисел найдите разницу между максимальным
#и минимальным значением дробной части элементов. Пример [1.1,1.2,3.1,5,10.01]=>0.19
from random import * 
a = [3.4,5,54.34,5.3]
print(a)
def max_min(a):
  max=a[0]
  for i in range(len(a)):
    if a[i]>max: max = a[i]
  return max
print(max_min(a))    

