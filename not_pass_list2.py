def LiLit2(ls):
    low = 0
    big = 0
    count = 0
    newls = []
    x = 0
    finalls= []
    if ls == []:
        return "Error"
    for i in range (len(ls)):
        if ls[i].islower():
            low += 1
            count += 1
        elif ls[i].isupper():
            big += 1
            count += 1
        elif ls[i].isdigit():
            break
    if low < big :
        for u in range(count,len(ls)):
            x = int(ls[u]) +1
            newls.append(x)
    elif low > big :
        for j in range(count,len(ls)):
            x = int(ls[j]) - 1
            newls.append(x)
    elif low == big :
        for z in range(count, len(ls)):
            x = int(ls[z])
            newls.append(x)
    for f in range (len(newls)):
        if len(newls) == 0:
            break
        if len(newls) == 1:
            finalls.append(newls[0])
            break
        finalls.append(newls[-1])
        finalls.append(newls[0])
        newls.pop(-1)
        newls.pop(0)
    return finalls
print(LiLit2(['a','b','C','1', '2', '3', '4','5']))
print(LiLit2(['a','A','A','A','0', '1', '2', '3']))
print(LiLit2([]))
