def f (n):
        x = 1
        y = 0
        st_x = []
        total =""
        y2 = 0
        while y < n + 1:
            st_x.append(x)
            x = x +2
            y = y + 1
        while y2 < n + 1:
            if y2 == 0 :
                total += "".join(map(str, st_x))
            elif y2 == n +1:
                total += "".join(map(str,st_x))
            elif y2 % 2 != 0:
                st_x = st_x[:len(st_x)-1]
                total += "".join(map(str,st_x[::-1]))
            elif y2 % 2 == 0:
                st_x = st_x[:len(st_x)-1 ]
                total += "".join(map(str, st_x))
            y2 += 1

        return(total)
print(f(2))