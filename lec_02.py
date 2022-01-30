#colors = ['red','green','blue']
#a = open('xtx.txt','a')
#a.write('\nline231\n')
#a.write('line32\n')
#a.close()

#a = open('xtx.txt','r')
#for i in a:
 #   print(i)
#a.close()

#функции и модули

#import Task_04 as f
#print(f.max_from_three(3,7,9))
#def fer(symbol,count=3):
 #   return symbol*count

#print(fer(4))

#def con(*arg):
 #   s = ''
  #  for i in arg:
   #     s = s+str(i)
   # return s
#print(con(1,4,2,7))

#рекурсия
#def fib(n):
 #   if n in [1,2]:
  #      return 1
  #  else:
  #      return fib(n-1)+fib(n-2)

#list =[]
#for i in range(1,10):
 #   list.append(fib(i))

#print(list)

#кортежи

#a = (4,7)
#print(type(a))
#print(a[0])
#for i in a:
 #   print(i)

dictor ={}
dictor={'up': 'k','left':'i'}
print(type(dictor))
print(dictor['up'])

for i in dictor:
    print(i)