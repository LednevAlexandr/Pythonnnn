# Определить , присутствует ли в заданном масиве некоторое число

import random
a = [random.randint(-9,9) for i in range(10)]
b = int(input())
print(a)
print(b in a)
