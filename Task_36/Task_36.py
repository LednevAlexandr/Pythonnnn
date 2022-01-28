# задать масив, заполнить случайными положительными трехзначными числами.Показать количество четных чисел.
import random
def completion_arr(arr):
  s=''
  for i in range(len(arr)):
    arr[i] = random.randint(100,999)
    s=s+str(arr[i])+' '
  return s

a = list(range(0,10))
print(completion_arr(a))
print(a)
print(a)

def how_many_even(arr):
  result = 0
  for i in arr:
    if i%2!=0:result+=1
  return result
print(how_many_even(a))

  
