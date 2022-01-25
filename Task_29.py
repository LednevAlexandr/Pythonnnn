# написать программу вычисления произведения чисел от 1 до n



def a(n):
    result=1
    for i in range(1,n+1):
        result = result * i
    return result

print(a(3))