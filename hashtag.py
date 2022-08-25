def generate_hashtag(s):
    if not s or len(s) > 140:
        return False
    x = s.split(" ")
    y = len(x)
    y2 = 0
    x2 =[]
    z = ""
    i = 0
    print (x)
    while y2 < y:
      if (x[y2][0].islower()):
       p = x[y2][0].upper()
       x[y2] = x[y2].replace(x[y2][0],p)
       #x[y2] = x[y2].replace(x[y2][0],x[y2][0].upper())
      x2.append(x[y2])
      print(x[y2])
      y2 = y2 + 1

    while i < len(x2) :
        z = z + x2[i]
        i = i + 1
    return("#" + z)
print(generate_hashtag("hello there"))
print(generate_hashtag(""))
#print(generate_hashtag("Codewars      "))

