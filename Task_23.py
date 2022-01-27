# показать таблицу квадратов чисел от 1 до N
def squares_table(N):
  for j in range(1,N):
    print(f'{j}  :  {j**2}')


squares_table(10)
