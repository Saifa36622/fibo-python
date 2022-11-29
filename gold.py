def maxmin(x):
    ans = x
    ls_ans = []
    str_x = str(x)
    ls_try = []
    wow = []
    for i in range(len(str_x)):
        ls_try.append(str_x[i])

    wow = ls_try.copy()

    for u in range(len(str_x)):
        ls_try = wow.copy()
        # print(ls_try)
        for z in range(len(ls_try)):
            ls_try = wow.copy()
            temp = ls_try[u]
            ls_try[u] = ls_try[z]
            ls_try[z] = temp

            str_join = ''.join(map(str,ls_try))
            ls_ans.append(str_join)
            zz = min(ls_ans)
            if zz[0] == "0":
                ls_ans.remove(min(ls_ans))
    # print(wow)
    return int(max(ls_ans)),int(min(ls_ans))
# print(maxmin(9876543210))
# print(maxmin(1234567890))