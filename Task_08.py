# Показать четные числа от 1 до N
def pov(n):
    s=''
    for i in range(1,n,1):
        if i%2==0: s=s+str(i)+'\n'
    return s

print(pov(10))