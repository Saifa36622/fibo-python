def reverse_avoidN(x,N):
    ans = ""
    y = 0
    re_ans = ""
    if x == " " or x == '':
        return "Error"
    while y < len(x):
        if y % N != 0:
            ans = ans[::-1]
            ans += x[y]
            re_ans = ans[::-1]
        y += 1
    return re_ans
print(reverse_avoidN("abcdefgh",2))
print(reverse_avoidN("",2))