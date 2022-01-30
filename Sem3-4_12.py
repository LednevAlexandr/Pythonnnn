#Для натурального числа N создать словарь индекс-значение,состоящих из элементов последовательности 3k+1

def new_dict(n):
    a={}
    k=1
    for i in range(0,n):
        a[k]=3*k+1
        k+=1
    return a

g=new_dict(10)
print(g)
print(g[7])