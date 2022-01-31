# написать программу преобразования десятичного числа в двоичное.

def conversion(n):
  s=''
  while n!=0:
    s=s+str(n%2)
    n=n//2 
  return s[::-1]

print(conversion(36545))
