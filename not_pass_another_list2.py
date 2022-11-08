def SmallthenBig(l1,l2):
    total = []
    if len(l1) != len(l2):
        return ("'Oh! no")
    if l1 == [] or l2 == []:
        return ("'Oh! no")
    for i in range (len(l1)):
        l1_small = 0
        l2_big = 0
        l1lofsmall = []
        l2lofbig = []
        newstr= ""
        newstr2 = ""
        for u in range(len(l1[i])):
            if l1[i][u].islower():
                l1_small += 1
                l1lofsmall.append(l1[i][u])
        for z in range(len(l2[i])):
            for p in range(len(l2[i][z])):
                if l2[i][z].isupper():
                    l2_big += 1
                    l2lofbig.append(l2[i][z])
        if l1_small == l2_big:
            newstr += "".join(map(str,l1lofsmall))
            newstr += "".join(map(str,l2lofbig))
            newstr2 = newstr.upper()
            total.append(newstr2)
        if l1_small != l2_big:
            newstr = ""
            newstr3 = ""
            newstr4 = []
            newstr5 = []
            newstr6 = []
            newstr += "".join(map(str,l1[i]))
            newstr += "".join(map(str,l2[i]))
            newstr3 = newstr.lower()
            newstr4= sorted(newstr3)
            newstr5 = sorted(list(set(newstr4)))
            newstr6 ="".join(map(str,newstr5))
            total.append(newstr6)



    return total
    # if l1_small == l2_big:
print(SmallthenBig(['MonDay', 'TuESDay', 'WEDnesDAY', 'ThUrSdAy', 'fridaY'],['mONdAY', 'TUESDAY', 'wEDneSday', 'THUrSdAY', 'FridaY']))
print(SmallthenBig(['ABc','dEF','g','hIj'],['K','lMN','op','qRsTuv']))
