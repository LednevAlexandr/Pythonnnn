#23 найти произведение пар чисел в списке.
#Парой считаем первый и последний элемент,
#второй и предпоследний и т.д.пример: [2,3,4,5,6,] => [12,15,16];[2,3,5,6]=>[12,15]
import math 
a = [2,5,5,7,6]

def sum_two(a):
  b=[]
  for i in range(len(a)):
     if i >= math.ceil(len(a)/2):break 
     b.append(a[i]*a[-i-1])
  return b

print(sum_two(a))
print(len(a))
