#Для натурального числа N создать словарь индекс-значение,состоящих из элементов последовательности 3k+1

def new_dict(n):
    a={k:3*k+1 for k in range(1,n+1)}
    return a

print(new_dict(5))