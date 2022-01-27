# Найти сумму чисел от 1 до A

def summ_number(a):
  sum=0
  for i in range(1,a+1):
    sum=sum+i
  return sum

print(summ_number(5))
