# Найти сумму чисел списка стоящих на нечетных позициях
from random import*
a =[randint(0,10) for i in range(0,6)]
print(a)
def find_sum(a):
  sum=0
  for i in range(len(a)):
    if i%2 != 0:
      sum = sum+a[i]
  return sum

print(find_sum(a))
