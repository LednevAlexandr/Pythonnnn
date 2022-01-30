#написать программу получающую набор произведений чисел от 1 до N.для 4 - 1.2.6.26

def reg(n):
    a = []
    x=1
    for i in range(1,n+1):
        x=x*i
        a.append(x)
    return a

a = reg(4)
print(a)