# Программа проверяет пятизначное число на палиндромом

a = 14541
b = str(a)
if b[0] == b[-1] and b[1] == b[-2]:
  print('полиндром')
else:
  print('не полиндром')
