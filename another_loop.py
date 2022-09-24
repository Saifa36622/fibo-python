def f(x):
    z = []
    z.append(1)
    loop = 2
    total = ""
    plus = 3
    mid_total = 1
    for y in range (1,x):
        for i in range (y):
            z.append(loop)
            loop -= 2
        loop += 2
        mid_total = mid_total + plus
        plus += 2
        z.append(mid_total)
        for o in range (y):
            z.append(loop)
            loop += 2

    total += "".join(map(str,z))
    return total
print(f(4))