# Найти корни квадратного уравнения Ax² + Bx + C = 0
# -Математикой
# -Используя дополнительные библиотеки*


def f(a,b,c):
  d = b**2 - 4*a*c
  if d==0:
     return -b/2*a
  elif d>0:
    x1= (-b+(d**0.5))/2*a
    x2= (-b-(d**0.5))/2*a
    return x1,x2
  else:
     return -1

k=list(f(1,-5,6))
print(type(k))
