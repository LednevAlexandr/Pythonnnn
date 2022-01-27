# Определить , присутствует ли в заданном масиве некоторое число

import random
def completion_array(array):
  s=''
  for i in range(len(array)):
    array[i]=random.randint(-9,9)
    s=s+str(array[i])+"  "
  return s

a = list(range(0,10))
b = int(input())
print(completion_array(a))

print(b in a)
