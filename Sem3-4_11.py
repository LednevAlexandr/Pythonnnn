#для натурального N создать список: 1,-3,9,-27,81

def new_list(n):
    list1=[]
    list1.append(1)
    for i in range(1,n+1):
        s = list1[i-1]*(-3)
        list1.append(s)
    return list1

a = new_list(5)
print(a)


