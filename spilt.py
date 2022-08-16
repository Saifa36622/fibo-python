s = '123456789'
o = []
y = 0
x = 0
z = int (len(s) / 2)
while s:
  if len (s) % 2 == 0 :
    o.append(s[:2])
    s = s[2:]
  else :
    if x < z :
      o.append(s[:2])
      s = s[2:]
      x = x + 1
    else :
      o.append(s[:1] + "_")
      s = s[1:]
    

      
print (o,z,x)