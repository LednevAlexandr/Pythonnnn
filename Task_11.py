# дано число из отрезка 10,99. Показать наибольшую цифру числа

import random
a = random.randint(10,99)
print(a)

if a%10>a//10: print(a%10)
else: print(a//10)
