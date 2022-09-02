def LoopAfterMidTerm(n):
    x = 1
    st = []
    total = ""
    y = []
    z = 1
    if n == 0 :
        return 0
    while x <= n :
        y.append(x)
        y_re = y[::-1]
        if z % 2 == 0 :
            st.append("".join(map(str,y_re)))
            st.append("".join(map(str,y)))
        else:
            st.append("".join(map(str,y)))
            st.append("".join(map(str,y_re)))
        x = x+1
        z = z+1
    total += "".join(map(str,st))
    return (total)
