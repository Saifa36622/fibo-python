def easyIndex2(l1,l2):
    sum = 0
    time = 1
    for i in range (len(l1)):
        if i in l2:
            time *= l1[i]
        else :
            sum += l1[i]
    return [time,sum]