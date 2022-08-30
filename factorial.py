def fact(n):
  x = 1
  sum = 0
  for i in range(1,n+1):
    x = x * i
    sum = sum + x
  return (sum +1)
print (fact(3))
print (fact(5))