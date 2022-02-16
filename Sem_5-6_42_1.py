# Реализовать RLE алгоритм. реализовать модуль сжатия и восстановления данных.
# входные и выходные данные хранятся в отдельных текстовых файлах
from itertools import count


f = open('text_42_2.txt','r')
st=''
for i in f:
    st=st+i
print(st)

def rle(s):
    count=''
    d=''
    for i in s:
        if i.isdigit():
            count = count+i
        else:
            d=d+int(count)*i
            count=''
    return d
g = open('text_42_3.txt','w')
g.write(rle(st))
g.close()