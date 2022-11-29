def CoinCalculator(x):
    ans = ""
    Royal = 0
    plat = 0
    gold = 0
    silver = 0
    bronze = 0
    tin = 0
    while x > 0 :

        if x >= 9999:
            Royal += 1
            x -= 9999
        elif x >= 1777 :
            plat += 1
            x -= 1777
        elif x >= 117 :
            gold += 1 
            x -= 117
        elif x >= 77:
            silver += 1
            x -= 77
        elif x >= 7 :
            bronze += 1
            x -= 7
        else :
            tin += 1
            x -=1
    print(Royal,plat,gold,silver,bronze,tin)
print(CoinCalculator(1000))