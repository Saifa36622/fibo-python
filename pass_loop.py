def number_and_hashtag2(x):
    a = ""
    z = 1
    a2 = ""
    a3 =[]
    a4 = []
    total = ""
    for i in range (x):
        a = str(z) + a
        a = "#" + a
        z += 1
        a2 = a2 + a
    return a2
print(number_and_hashtag2(10))