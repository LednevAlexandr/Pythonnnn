# Задать масив из 12 элементов, заполненных в диапозоне [0,9].Найти сумму положительных элементов.
import random
def completion_array(array):
  s=''
  for i in range(len(array)):
    array[i]=random.randint(-9,9)
    s=s+str(array[i])+"  "
  return s

def positive_sum(array):
  sum=0
  for i in range(len(array)):
    if array[i]>0:sum=sum+array[i]
  return sum
a = list(range(0,12))
print(completion_array(a))
print(positive_sum(a))
