def IsElements(l):
    final = []
    checker = ['earth', 'fire' ,'wind', 'water']
    earth = 0
    fire = 0
    wind = 0
    water = 0
    num =[]
    for i in range(len(l)):
        if type(l[i]) is list:
            for x in l[i]:
                final.append(x)
        else :
            final.append(l[i])
    for u in final:
        if u not in checker:
            return ("None")
    for z in final:
        if z == 'earth':
            earth += 1
        elif z == 'fire':
            fire += 1
        elif z == "wind":
            wind += 1
        elif z == "water":
            water += 1
    num.append(earth)
    num.append(fire)
    num.append(water)
    num.append(wind)
    return min(num)
# print(IsElements([['fire'],'wind',['water', 'earth'],['wind']]))
# print(IsElements([['fire','water','hot'],'earth','wind']))