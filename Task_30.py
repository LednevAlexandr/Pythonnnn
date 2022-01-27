# показать кубы чисел, заканчивающихся на четную цифру

def cub_number(a,b):
  for i in range(a,b+1):
    c = pow(i,3)
    if c%2==0:
      print(c)

cub_number(1,100)
