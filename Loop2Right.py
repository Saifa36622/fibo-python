def Loop2Right(n):
  st = []
  total = ""
  st2 = []
  y = 0
  for i in range(0,n):
    st.append("0")
  while n > 0 or y < n:
    st2 = list(st)
    st2[y] = n-1
    total += "".join(map(str,st2))
    n -= 1
    y = y + 1
  return (total)
print (Loop2Right(5))