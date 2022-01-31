# дано число.Составить список чисел фибоначчи,в том числе для отрицательных индексов. для 5 [5,-3,2,-1,1,0,1,1,2,3,5]
def fibonacci(n):
  if n in (1, 2): return 1
  return fibonacci(n - 1) + fibonacci(n - 2)
  
print(fibonacci(10))
