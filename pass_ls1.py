def easyIndex2(ls1,ls2):
    # ls1 = ls[0]
    # ls2 = ls[1]
    total = []
    num = 1
    num2 = 0
    x = 0
    if ls1 == [] or ls2 == []:
        return "Error"
    for i in range (len(ls2)):
        x = ls2[i]
        num *= ls1[x]
    total.append(num)
    for u in range(len(ls2)):
        x = ls2[u]
        ls1[x] = 0
    for j in range(len(ls1)):
        num2 += ls1[j]
    total.append(num2)
    return total
print(easyIndex2([4, 8, 1, 5], [3, 1, 0]))
# print(easyIndex2([5, 3, 10, 8], [2,1]))
