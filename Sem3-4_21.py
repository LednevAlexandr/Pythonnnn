#21 определить позицию второго вхождения строки в списке либо сообщить, что его нет
import random
a = ['5', 'sdf', '6','5']
print(a)
s = '5'
def line_is_list(a,s):
  count = 0
  for i in range(len(a)):
    if a[i]==s: count+=1
    if count == 2:return i 

print(line_is_list(a,s))
