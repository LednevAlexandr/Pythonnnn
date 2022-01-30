# пользователь задает две строки.определить количество вхождений одной строки в другой
arg1=str(input())
arg2=str(input())

def function(arg1,arg2):
    count = 0
    s=''
    for i in range(len(arg2)):
        for j in range(len(arg1)):
            if arg1[j]==arg2[i] : s=s+arg2[j]
        if s==arg1:
            count=count+1
            s=''
    return count

print(function(arg1,arg2))