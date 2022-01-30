# реализовать алгоритм задания случайных чисел.Без использования встроенного генератора случайных чисел.
from datetime import datetime
import random
import datetime
#a = [random.randint(1,100) for i in range(1,10)]
def get_rand():
    return datetime.datetime.now().microsecond%10
    
print(get_rand())    
