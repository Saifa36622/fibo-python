def count_bits(n):
    z = bin(n)
    z = z[2:]
    y = z.split("0")
    x = 0
    x2 = 0
    while (x < len(y)):
        if y[x] == '1':
            x2 = x2 + 1
            x = x + 1
        elif y[x] =='11':
            x2 = x2 + 2
            x = x+1
        elif y[x] =='111':
            x2 = x2 + 3
            x = x+1
        elif y[x] =='1111':
            x2 = x2 + 4
            x = x+1
        elif y[x] =='11111':
            x2 = x2 + 5
            x = x+1
        elif y[x] =='111111':
            x2 = x2 + 6
            x = x+1
        elif y[x] =='1111111':
            x2 = x2 + 7
            x = x+1
        elif y[x] =='11111111':
            x2 = x2 + 8
            x = x+1    
        else :
             x = x +1
    return x2