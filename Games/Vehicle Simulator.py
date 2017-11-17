__author__ = 'naperkins'
#Text based Vehicle Game
import easygui

class Boat:
    def __init__(self):
        self.money = 47000
        self.name = 'Boat'
        self.mpg = 1
        self.weight = 1
        self.tank_size = 1
        self.drag = 50
        self.engine_power = 1
    def store(self):
        self.items = ['Frame', 'Fuel Tank', 'Engine', 'Paint']
        self.rank = ['Crude' , 'Normal', 'Sweet', 'Super', 'Ultra']
        self.price = [[[15000, 17053, 21034, 28539, 35910],["Weight:1532lbs\tDrag:-07","Weight:1622lbs\tDrag:-14","Weight:1670lbs\tDrag:-17","Weight:1697lbs\tDrag:-25","Weight:1686lbs\tDrag:-32"]],
                      [[9542, 11582, 14859, 17021, 21930],["Weight:23lbs\tCapacity:5\t","Weight:29lbs\tCapacity:8\t","Weight:38lbs\tCapacity:12\t","Weight:47lbs\tCapacity:16\t","Weight:56lbs\tCapacity:20\t"]],
                      [[13067, 15730, 19265, 23586, 28462],["Weight:425lbs\tPower:215\tMPG:10\t","Weight:425lbs\tPower:350\tMPG:13\t","Weight:425lbs\tPower:500\tMPG:16\t","Weight:425lbs\tPower:675\tMPG:21\t","Weight:425lbs\tPower:721\tMPG:26\t"]],
                      [[302, 497, 654, 867, 1135], ["Drag:-1","Drag:-1","Drag:-2","Drag:-2","Drag:-3"]]]

class Plane:
    def __init__(self):
        self.money = 1096782
        self.name = 'Plane'
        self.mpg = 1
        self.weight = 1
        self.tank_size = 1
        self.drag = 50
        self.engine_power = 1
    def store(self):
        self.items = ['Frame', 'Fuel Tank', 'Engine', 'Paint']
        self.rank = ['Crude' , 'Normal', 'Sweet', 'Super', 'Ultra']
        self.price = [[[459382, 464810, 471480, 487310, 495130],["Weight:1532lbs\tDrag:-07","Weight:1622lbs\tDrag:-14","Weight:1670lbs\tDrag:-17","Weight:1697lbs\tDrag:-25","Weight:1686lbs\tDrag:-32"]],
                      [[168210, 183150, 194160, 214907, 228390],["Weight:23lbs\tCapacity:5\t","Weight:29lbs\tCapacity:8\t","Weight:38lbs\tCapacity:12\t","Weight:47lbs\tCapacity:16\t","Weight:56lbs\tCapacity:20\t"]],
                      [[187205, 195851, 224280, 232601, 259305],["Weight:425lbs\tPower:215\tMPG:10\t","Weight:425lbs\tPower:350\tMPG:13\t","Weight:425lbs\tPower:500\tMPG:16\t","Weight:425lbs\tPower:675\tMPG:21\t","Weight:425lbs\tPower:721\tMPG:26\t"]],
                      [[302, 497, 654, 867, 1135], ["Drag:-1","Drag:-1","Drag:-2","Drag:-2","Drag:-3"]]]

class Car:
    def __init__(self):
        self.money = 107000
        self.name = 'Car'
        self.mpg = 1
        self.weight = 1
        self.tank_size = 1
        self.drag = 50
        self.engine_power = 1
    def store(self):
        self.items = ['Frame', 'Fuel Tank', 'Engine', 'Paint']
        self.rank = ['Crude' , 'Normal', 'Sweet', 'Super', 'Ultra']
        self.price = [[[15259, 25892, 35283, 45739, 55836],["Weight:1532lbs\tDrag:-07","Weight:1622lbs\tDrag:-14","Weight:1670lbs\tDrag:-17","Weight:1697lbs\tDrag:-25","Weight:1686lbs\tDrag:-32"]],
                      [[6218, 11980, 14289, 24394, 37293],["Weight:23lbs\tCapacity:5\t","Weight:29lbs\tCapacity:8\t","Weight:38lbs\tCapacity:12\t","Weight:47lbs\tCapacity:16\t","Weight:56lbs\tCapacity:20\t"]],
                      [[9240, 14650, 25023, 36320, 43750],["Weight:425lbs\tPower:215\tMPG:10\t","Weight:425lbs\tPower:350\tMPG:13\t","Weight:425lbs\tPower:500\tMPG:16\t","Weight:425lbs\tPower:675\tMPG:21\t","Weight:425lbs\tPower:721\tMPG:26\t"]],
                      [[302, 497, 654, 867, 1135], ["Drag:-1","Drag:-1","Drag:-2","Drag:-2","Drag:-3"]]]

class Motorcycle:
    def __init__(self):
        self.money = 13000
        self.name = 'Motorcycle'
        self.mpg = 1
        self.weight = 1
        self.tank_size = 1
        self.drag = 50
        self.engine_power = 1
    def store(self):
        self.items = ['Frame', 'Fuel Tank', 'Engine', 'Paint']
        self.rank = ['Crude' , 'Normal', 'Sweet', 'Super', 'Ultra']
        self.price = [[[1532, 2500, 3523, 4520, 5590],["Weight:1532lbs\tDrag:-07","Weight:1622lbs\tDrag:-14","Weight:1670lbs\tDrag:-17","Weight:1697lbs\tDrag:-25","Weight:1686lbs\tDrag:-32"]],
                      [[634, 1131, 1493, 2470, 3714],["Weight:23lbs\tCapacity:5\t","Weight:29lbs\tCapacity:8\t","Weight:38lbs\tCapacity:12\t","Weight:47lbs\tCapacity:16\t","Weight:56lbs\tCapacity:20\t"]],
                      [[939, 1423, 2567, 3674, 4322],["Weight:425lbs\tPower:215\tMPG:10\t","Weight:425lbs\tPower:350\tMPG:13\t","Weight:425lbs\tPower:500\tMPG:16\t","Weight:425lbs\tPower:675\tMPG:21\t","Weight:425lbs\tPower:721\tMPG:26\t"]],
                      [[302, 497, 654, 867, 1135], ["Drag:-1","Drag:-1","Drag:-2","Drag:-2","Drag:-3"]]]

class SpaceShip:
    def __init__(self):
        self.money = 4679348
        self.name = 'Space Ship'
        self.mpg = 1
        self.weight = 1
        self.tank_size = 1
        self.drag = 50
        self.engine_power = 1
    def store(self):
        self.items = ['Frame', 'Fuel Tank', 'Engine', 'Paint']
        self.rank = ['Crude' , 'Normal', 'Sweet', 'Super', 'Ultra']
        self.price = [[[1959201, 2279535, 2592509, 2606942, 2819592],["Weight:153275lbs\tDrag:-07","Weight:162275lbs\tDrag:-14","Weight:167075lbs\tDrag:-17","Weight:169775lbs\tDrag:-25","Weight:168675lbs\tDrag:-32"]],
                      [[123894, 135293, 147135, 1953267, 2257392],["Weight:2375lbs\tCapacity:575\t","Weight:2975lbs\tCapacity:875\t","Weight:3875lbs\tCapacity:1275\t","Weight:4775lbs\tCapacity:1675\t","Weight:5675lbs\tCapacity:2075\t"]],
                      [[149023, 153279, 15965, 164876, 167385],["Weight:42575lbs\tPower:21575\tMPG:10\t","Weight:42575lbs\tPower:35075\tMPG:13\t","Weight:42575lbs\tPower:50075\tMPG:16\t","Weight:42575lbs\tPower:67575\tMPG:21\t","Weight:42575lbs\tPower:72175\tMPG:26\t"]],
                      [[302, 497, 654, 867, 1135], ["Drag:-1","Drag:-1","Drag:-2","Drag:-2","Drag:-3"]]]

class UAV:
    def __init__(self):
        self.money = 4794689
        self.name = 'UAV'
        self.mpg = 1
        self.weight = 1
        self.tank_size = 1
        self.drag = 50
        self.engine_power = 1
    def store(self):
        self.items = ['Frame', 'Fuel Tank', 'Engine', 'Paint']
        self.rank = ['Crude' , 'Normal', 'Sweet', 'Super', 'Ultra']
        self.price = [[[1959201, 2279535, 2592509, 2606942, 2819592],["Weight:15327lbs\tDrag:-07","Weight:16227lbs\tDrag:-14","Weight:16707lbs\tDrag:-17","Weight:16977lbs\tDrag:-25","Weight:16867lbs\tDrag:-32"]],
                      [[123894, 135293, 147135, 1953267, 2257392],["Weight:2375lbs\tCapacity:575\t","Weight:2975lbs\tCapacity:875\t","Weight:3875lbs\tCapacity:1275\t","Weight:4775lbs\tCapacity:1675\t","Weight:5675lbs\tCapacity:2075\t"]],
                      [[149023, 153279, 15965, 164876, 167385],["Weight:4257lbs\tPower:21575\tMPG:10\t","Weight:4257lbs\tPower:35075\tMPG:13\t","Weight:4257lbs\tPower:50075\tMPG:16\t","Weight:4257lbs\tPower:67575\tMPG:21\t","Weight:4257lbs\tPower:72175\tMPG:26\t"]],
                      [[302, 497, 654, 867, 1135], ["Drag:-1","Drag:-1","Drag:-2","Drag:-2","Drag:-3"]]]

easygui.msgbox('This is a simulation game.  In this game you have to make the best vehicle that you have chosen.  Once you spend all of your money your vehicle will instantly be tested.', title="Simulator")
def game():
    specs = []
    place = 0
    place1 = 0
    v_type = easygui.buttonbox('Choose a vehicle : ', title="Simulator", choices=["Boat", "Plane", "Car", "Motorcycle", "Space Ship", "UAV"])
    v_type = v_type.lower().title()
    if v_type.lower() == 'boat':
        chosen = Boat()
    if v_type.lower() == 'plane':
        chosen = Plane()
    if v_type.lower() == 'car':
        chosen = Car()
    if v_type.lower() == 'motorcycle':
        chosen = Motorcycle()
    if v_type.lower() == 'space ship':
        chosen = SpaceShip()
    if v_type.lower() == 'uav':
        chosen = UAV()
    gotten = ""
    chosen.store()
    use = chosen.items[:]
    botten = False
    dont = []
    alt = []
    weird = False
    while 1:
        messed = chosen.items
        count = 0
        if chosen.money >= chosen.price[3][0][0]:
            if use == ["Paint"]:
                use = chosen.items
                botten = True
            if botten:
                    b = easygui.ynbox("You have bought everything but paint, do you want to upgrade anything?",title="Simulator")
                    if b:
                        weird = True
                        use = chosen.items[:]
                        count = 0
                        for ii in dont:
                            for i in use:
                                if i == ii:
                                    a = use.pop(count)
                                count += 1
                            count = 0
                        while True:
                            if use == ["Paint"]:
                                chosen.money = 0
                                break
                            easygui.msgbox(("You have $%s dallars left."% chosen.money),title="Simulator")
                            item = easygui.buttonbox(("Choose an item to Upgrade:"), title="Simulator",choices=use)
                            place = 0
                            for i in chosen.items:
                                if item == i:
                                    break
                                place += 1
                            for i in alt:
                                if i[1] == item:
                                    index = i[0]
                            rank = easygui.buttonbox("Choose a quality for the %s: " % (chosen.items[place]), title="Simulator",choices=chosen.rank[index+1:])
                            place1 = 0
                            for i in chosen.rank:
                                if rank == i:
                                    break
                                place1 += 1
                            cost = chosen.price[place][0][place1]-(chosen.price[place][0][index+1])*3/4
                            choice = easygui.ynbox(("It would cost $%s to buy a %s %s %s. Do you want to but it?" % (str(cost),rank,chosen.name,item)), title="Simulator")
                            if choice:
                                specs.append('%s %s' % (chosen.rank[place1], chosen.items[place]))
                                chosen.money -= cost
                                if chosen.items[place] == ('Frame' or 'Paint'):
                                    placs = chosen.price[place][1][place1].find("Drag:")
                                    if chosen.items[place] == "Frame":
                                        chosen.drag = 50
                                        chosen.drag += int(chosen.price[place][1][place1][placs+5:placs+8])
                                    else:
                                        chosen.drag = 50
                                        chosen.drag += int(chosen.price[place][1][place1][placs+5:placs+7])
                                if chosen.items[place] == "Engine":
                                    placs = chosen.price[place][1][place1].find("Power:")
                                    pald = chosen.price[place][1][place1].find("\t", placs)
                                    chosen.engine_power = 1
                                    chosen.engine_power += int(chosen.price[place][1][place1][placs+6:pald])
                                    placs = chosen.price[place][1][place1].find("MPG:")
                                    pald = chosen.price[place][1][place1].find("\t",placs)
                                    chosen.mpg = 1
                                    chosen.mpg += int(chosen.price[place][1][place1][placs+4:pald])
                                if chosen.items[place] != "Paint":
                                    placs = chosen.price[place][1][place1].find("Weight:")
                                    pald = chosen.price[place][1][place1].find("\t",placs)
                                    placs1 = chosen.price[place][1][alt[index][0]].find("Weight:")
                                    pald1 = chosen.price[place][1][alt[index][0]].find("\t",placs1)
                                    chosen.weight -= int(chosen.price[place][1][place1][placs1+7:pald1-3])
                                    chosen.weight += int(chosen.price[place][1][place1][placs+7:pald-3])
                                if chosen.items[place] == "Fuel Tank":
                                    placs = chosen.price[place][1][place1].find("Capacity:")
                                    pald = chosen.price[place][1][place1].find("\t", placs)
                                    chosen.tank_size = 1
                                    chosen.tank_size += int(chosen.price[place][1][place1][placs+9:pald])
                                count = 0
                                for i in use:
                                    if i == item:
                                        a = use.pop(count)
                                        break
                                    count += 1
                                if gotten == "":
                                    gotten += "%s %s %s" % (rank, chosen.rank[place1], chosen.items[place])
                                else:
                                    gotten += " and %s %s %s" % (rank, chosen.rank[place1], chosen.items[place])
                    else:
                        chosen.money = 0
                    gotten = ""
                    for i in dont:
                        if gotten == "":
                            gotten += "an Ultra " + dont[0]
                        else:
                            gotten += "and a Ultra " + dont[0]
                    for i in alt:
                        for ii in i:
                            if gotten == "":
                                gotten += "an %s %s, " % (chosen.rank[i[0]],i[1])
                            else:
                                gotten += "and a %s %s, " % (chosen.rank[i[0]],i[1])

            else:
                if gotten == "":
                    easygui.msgbox("You have %s and have not bought anything." % chosen.money, title="Simulator")
                    gotten += " "
                else:
                    easygui.msgbox("\n\nSo far you have %s. You also have $%s left."% (gotten, str(chosen.money)), title="Simulator")
                if use == []:
                    use = chosen.items
                    item = easygui.buttonbox(("Choose an item to Purchase:"), title="Simulator",choices=use)
                    item = item.lower().title()
                else:
                    item = easygui.buttonbox(("Choose an item to Purchase:"), title="Simulator",choices=use)
                    item = item.lower().title()
                if item in chosen.items:
                    for a in chosen.items:
                        if item == a:
                            break
                        place += 1
                    rank = easygui.buttonbox("Choose a quality for the %s: " % (chosen.items[place]), title="Simulator",choices=chosen.rank)
                    rank = rank.lower().title()
                    if rank in chosen.rank:
                        for a in chosen.rank:
                            if rank == a:
                                break
                            place1 += 1
                        test = easygui.ynbox(("Do you what to compare the %s %s's stats to the ones above and below it?" % (rank, item)), title="Simulator")
                        if test:
                            if rank == "Ultra":
                                message = "An %s %s would have stats of %s\nWheras a Ultra %s would have stats of %s" % (chosen.rank[place1-1], chosen.items[place], chosen.price[place][1][place1-1], chosen.items[place], chosen.price[place][1][place1])
                                change = easygui.buttonbox(message,title="Simulator",choices=["%s %s"% (chosen.rank[place1-1],chosen.items[place]),"%s %s"% (chosen.rank[place1],chosen.items[place])])
                            elif rank == "Crude":
                                message = "An %s %s would have stats of %s\nWheras a Crude %s would have stats of %s" % (chosen.rank[place+1], chosen.items[place1-1], chosen.price[place][1][place1], chosen.items[place], chosen.price[place][1][place1-1])
                                change = easygui.buttonbox(message,title="Simulator",choices=["%s %s"% (chosen.rank[place1-1],chosen.items[place]),"%s %s"% (chosen.rank[place1],chosen.items[place])])
                            else:
                                message = "An %s %s would have stats of %s\nAlso a %s %s would have stats of %s\nWheras a %s %s would have stats of %s" % (chosen.rank[place1-1], chosen.items[place],chosen.price[place][1][place1-1], chosen.rank[place], chosen.items[place1], chosen.price[place][1][place1], chosen.rank[place1+1], chosen.items[place], chosen.price[place][1][place1+1])
                                change = easygui.buttonbox(message,title="Simulator",choices=["%s %s"% (chosen.rank[place1-1],chosen.items[place]),"%s %s"% (chosen.rank[place1],chosen.items[place]),"%s %s"% (chosen.rank[place1+1],chosen.items[place])])
                            place1, place = 0,0
                            for b in chosen.rank:
                                if b in change:
                                    rank = b
                                    break
                            for b in chosen.items:
                                if b in change:
                                    item = b
                                    break
                            for a in chosen.rank:
                                if rank == a:
                                    break
                                place1 += 1
                            for a in chosen.items:
                                if item == a:
                                    break
                                place += 1
                        easygui.msgbox('This %s %s %s has stats of \n\t%s ' % (chosen.rank[place1], chosen.name, chosen.items[place], chosen.price[place][1][place1]), title="Simulator")
                        confirmed = easygui.ccbox('This %s %s %s will cost %s dollars.  You have %s dollars.  Do you want to confirm this purchase? ' % (chosen.rank[place1], chosen.name, chosen.items[place], chosen.price[place][0][place1], chosen.money), title="Simulator")
                        if chosen.rank[place1][0] == 'U':
                            an = 'an'
                        if chosen.rank[place1][0] != 'U':
                            an = 'a'
                        if confirmed:
                            chosen.money -= chosen.price[place][0][place1]
                            if chosen.money < 0:
                                easygui.msgbox('You do not have enough money to buy %s %s %s' % (an, chosen.rank[place1], chosen.items[place]), title="Simulator")
                                chosen.money += chosen.price[place][0][place1]
                            else:
                                count = 0
                                for i in use:
                                    if i == item:
                                        a = use.pop(count)
                                        break
                                    count += 1
                                if rank == "Ultra":
                                    dont.append(chosen.items[place])
                                alt.append([place1,item])
                                specs.append('%s %s' % (chosen.rank[place1], chosen.items[place]))
                                if chosen.items[place] == ('Frame' or 'Paint'):
                                    placs = chosen.price[place][1][place1].find("Drag:")
                                    if chosen.items[place] == "Frame":
                                        chosen.drag += int(chosen.price[place][1][place1][placs+5:placs+8])
                                    else:
                                        chosen.drag += int(chosen.price[place][1][place1][placs+5:placs+7])
                                if chosen.items[place] == "Engine":
                                    placs = chosen.price[place][1][place1].find("Power:")
                                    pald = chosen.price[place][1][place1].find("\t", placs)
                                    try:
                                        chosen.engine_power += int(chosen.price[place][1][place1][placs+6:pald])
                                    except ValueError:
                                        chosen.engine_power += int(chosen.price[place+1][1][place1][placs+21:pald])
                                    placs = chosen.price[place][1][place1].find("MPG:")
                                    pald = chosen.price[place][1][place1].find("\t",placs)
                                    try:
                                        chosen.mpg += int(chosen.price[place][1][place1][placs+4:pald])
                                    except ValueError:
                                        chosen.mpg += int(chosen.price[place+1][1][place1][placs+21:pald])
                                if chosen.items[place] != "Paint":
                                    placs = chosen.price[place][1][place1].find("Weight:")
                                    pald = chosen.price[place][1][place1].find("\t",placs)
                                    try:
                                        chosen.weight += int(chosen.price[place][1][place1][placs+7:pald-3])
                                    except ValueError:
                                        chosen.weight += int(chosen.price[place][1][place1][placs+21:pald-3])
                                if chosen.items[place] == "Fuel Tank":
                                    placs = chosen.price[place][1][place1].find("Capacity:")
                                    pald = chosen.price[place][1][place1].find("\t", placs)
                                    try:
                                        chosen.tank_size += int(chosen.price[place][1][place1][placs+9:pald])
                                    except ValueError:
                                        chosen.tank_size += int(chosen.price[place][1][place1][placs+21:pald])
                                if gotten == " ":
                                    gotten.strip()
                                    gotten += "%s %s %s" % (an, chosen.rank[place1], chosen.items[place])
                                else:
                                    gotten.strip()
                                    gotten += " and %s %s %s" % (an, chosen.rank[place1], chosen.items[place])
                            gotten.strip()
                        easygui.msgbox(('Your total is %s dollars.' % chosen.money), title="Simulator")
                if chosen.money<=int(chosen.price[place+3][0][place1-4]):
                    easygui.msgbox(('Simulation over you have %s.' % gotten), title="Simulator")
                    easygui.msgbox(("With your combonation of parts, you went ", str(int((chosen.weight/8 + chosen.tank_size + chosen.drag + (chosen.mpg*chosen.tank_size)/8 + 26 + chosen.engine_power/15) - 113)), "miles."), title="Simulator")
                    break
                place = 0
                place1 = 0
        else:
            easygui.msgbox(('Simulation over you have %s.' % gotten), title="Simulator")
            easygui.msgbox(("With your combonation of parts, you went %s on one tank of gas" % str(int((chosen.weight/8 + chosen.tank_size + chosen.drag + (chosen.mpg*chosen.tank_size)/8 + 26 + chosen.engine_power/15) - 113)), "miles."), title="Simulator")
            break
tr = True
while tr:
    game()
    re = easygui.ccbox('Do you want to play again', title="Replay")
    if not re:
        tr = False