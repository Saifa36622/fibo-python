def f(n):
  x = 2
  y = ""
  y2 = ""
  for i in range(n):
    y += str(x)
    x += 2
    y2 = y + y2
  return y2
print (f(4))