def LoyKrathong(ls):
    ans = ""
    ls_of_ans = []
    for i in range(len(ls)):
        ans = ""
        while ls[i] > 0:
            if ls[i] >= 10 :
                ans += "10"
                ls[i] -= 10
            elif ls[i] >= 5:
                ans += "5"
                ls[i] -= 5
            else :
                ans += "1"
                ls[i] -= 1
        ls_of_ans.append(ans)
    return ls_of_ans
print(LoyKrathong ([6,1,13]))