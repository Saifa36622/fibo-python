def NamingRPG (name, weapon, mons):
    level_name = 0
    level_weapon = 0
    level_mons = 0
    num = 0
    name2 = name.replace(" ","")
    weapon2 = weapon.replace(" ","")
    level_name = (len(name2) + ord(name[0])) * (name.count(" ")+1)
    level_weapon = (len(weapon2) + ord(weapon[0])) * (weapon.count(" ") + 1)
    total = level_name + level_weapon
    for i in range(len(mons)):
        level_mons = 0
        mons2 = mons[i].replace(" ","")
        level_mons = ((len(mons2) + ord(mons[i][0])) * (mons[i].count(" ") + 1))
        if total > level_mons:
            num += 1
    return [level_name,num]
# print(NamingRPG("P Phun", "Murasame Maru", ["Rimur The Slime", "DragonBall Z" , "Pikachu"]))
# print(NamingRPG("Fang The Vegan", "Mushroom", ["Beef Steak", "Japanese curry with pork" , "Pork Chop", "Kentaky FriesChicken","Mr Donald The Duck"]))