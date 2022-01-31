#24 в заданном списке вещественных чисел найдите разницу между максимальным
#и минимальным значением дробной части элементов. Пример [1.1,1.2,3.1,5,10.01]=>0.19
from random import * 
a = [3.15,5.26,54.34,5.3]
print(a)
def max_min(a):
  b = [i - int(i) for i in a]
  max_n=max(b)
  print(max_n)
  min_n=min(b)
  print(min_n)
  return max_n-min_n
print(max_min(a))    
