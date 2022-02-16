# Реализовать RLE алгоритм. реализовать модуль сжатия и восстановления данных.
# входные и выходные данные хранятся в отдельных текстовых файлах
f = open('text_42_1.txt','r')
st=''
for i in f:
    st=st+i

def rle(s):
    count = 0
    saved=s[0]
    b=''
    for i in range(len(s)):
        if s[i]==saved:
            count+=1
        else:
            b=b+str(count)+saved
            count=1
            saved=s[i]
    b=b+str(count)+saved
    return b
d = open('text_42_2.txt','w')
d.write(rle(st))
d.close()