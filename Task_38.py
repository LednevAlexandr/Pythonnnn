def how_many(arr):
  result = 0
  for i in range(len(arr)):
    if (i+1)%2!=0:result+=arr[i]
  return result
print(how_many(a))
