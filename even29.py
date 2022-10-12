def even(x):
    total = ""
    for i in range (len(x)):
        if  i % 2 == 0 and int(x[i]) % 2 == 0:
            total += str(int(x[i])-1)
        elif i % 2 != 0 and int(x[i]) % 2 == 0:
            total += str(int(x[i])-2)
        else :
            total += x[i]
    return total
print (even("2457"))