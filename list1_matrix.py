def plus(matrix1,matrix2):
    n = []
    if len(matrix1) != len(matrix2[0]):
        return ("Error")
    if len(matrix1) == 0 or len(matrix2) == 0:
        return ("Error")
    for i in range(len(matrix1)):
        c = []
        for u in range (len(matrix1[i])):
            c.append(matrix1[i][u]+matrix2[u][i])
        n.append(c)


    return n
print(plus([[7, 8], [9, 10], [11, 12]], [[1, 2, 3], [4, 5, 6]]))
print(plus([[1, 2, 3, 4], [1, 2, 3, 4]],[[5, 6], [5, 6], [5, 6], [5, 6]]))