def lcm(x,y):
    x_list = []
    y_list = []
    if x % y == 0:
        return x
    if y % x == 0:
        return y
    for i in range(100):
        x_list.append(x*i)
        y_list.append(y*i)
    for u in range(1,len(x_list)-1):
        if x_list[u] in y_list:
            return x_list[u]
# print(lcm(36, 72))
# print(lcm(8, 12))