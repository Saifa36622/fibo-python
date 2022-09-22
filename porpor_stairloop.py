
def stair_num(n):
    z = []
    u = ""
    for x in range (1,n+1):
        for y in range(n - x):
            z.append(' ')
        for y in range(1,x+1):
            z.append(y)
        for y in range(2,x+1):
            z.append(x-y+1)
        if x != n:
            z.append("\n")
    u += "".join(map(str,z))
    return u

print(stair_num(4))