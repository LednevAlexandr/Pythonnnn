# Задать список из N элементов,заполненных числами от [-N,N].Найти произведение элементовна указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
from random import* 
f = open('file.txt','w')
f.write('1\n')
f.write('2\n')
f.write('4\n')
f.close()

f = open('file.txt','r')
    
n = int(input())
a = [i for i in range(-n,n+1)]
print(a)

def composition_pos(a,f):
    result=1
    for i in f:
        result = result*a[int(i)]
    return result
       
        
print(composition_pos(a,f))
        



