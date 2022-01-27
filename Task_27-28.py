# определить кол-во цифр в числе

def num_in_num(b):
  sum = 0
  while b > 0 or b <0:
    b = b//10
    sum=sum+1
  return sum

print(num_in_num(125))
  
