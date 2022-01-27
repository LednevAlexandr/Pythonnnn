# Найти кубы чисел от 1 до N
import math
def cub_number(N):
  for i in range(1,N+1):
    print(f'{pow(i,3)}')

cub_number(5)
