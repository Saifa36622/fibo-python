def insert(x):
    z=""
    x2 = x.split()
    if x2 == []:
        return "Error"
    for i in range (len(x2)):
        z += x2[i][-1] + x2[i] + str(len(x2[i]))
    return z
print (insert("I love code"))
print (insert("  "))