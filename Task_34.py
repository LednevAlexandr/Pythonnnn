# написать программу замену элементов масива на противоположные

import random
def completion_array(array):
  s=''
  for i in range(len(array)):
    array[i]=random.randint(-9,9)
    s=s+str(array[i])+"  "
  return s

def opposite_elements(array):
  s=''
  for i in range(len(array)):
    array[i]=-array[i]
    s=s+str(array[i])+'  '
  return s

array = list(range(0,9))
print(completion_array(array))
print(opposite_elements(array))
