def stringSum(ls1,ls2):
    st_ls1 = "".join(map(str,ls1))
    st_ls2 = "".join(map(str,ls2))
    in_ls1 = int(st_ls1)
    in_ls2 = int(st_ls2)
    su = in_ls1 + in_ls2
    ans = []
    st_su = str(su)
    # for i in range(len(st_su)):
    #     ans.append(st_su[i])
    return st_su
print(stringSum([9, 8, 7, 6], [1, 2]))