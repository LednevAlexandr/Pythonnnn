#20 Определить , присутствует ли в заданном списке строк, некоторое число

b = 5
s = 'ывфаывпыва'
def this_is_number(b,s):
  a = s.count(str(b))
  if a == 0: return -1
  else: return a

a=this_is_number(b,s)
print(a)
