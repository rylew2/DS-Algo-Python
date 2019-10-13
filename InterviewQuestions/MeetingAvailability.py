# can alsoe use chain.from_iterable to flatten
# from itertools import chain
# combinedpersons = list(chain.from_iterable(p))


def findtime(p):
    sched = sorted([x for person in p for x in person])
    print(sched)
    opentimes, personptr = [], 0

    availstart = float('-inf')
    for i in range(0, 2359):
        if i == sched[personptr]:
            avalstart = i
        



p1 = [(830, 930), (1030, 1100), (1300,1500)]
p2 = [(0, 30), (200, 400), (1000, 1130)]
personTimes = [p1, p2]
findtime(personTimes)  # (30,200), (400,830), (930, 1000), (1130, 1300), (1500-2359)




def isAvailable(m, checkTime):
    checkStart, checkEnd = checkTime
    m.sort() # mlgm
    for mtgStart, mtgEnd in m: #m
        for i in range(mtgStart, mtgEnd): #r
            minutes = int(str(i)[-2:])
            if 60<=minutes<=99: continue
            if i == checkStart or i==checkEnd-1: return False
    return True

m = [ (1300,1500), (830, 845), (1000,1100) ]
print(isAvailable(m, (930,1000))) #True
print(isAvailable(m, (846,1030))) #False
print(isAvailable(m, (1200,1300))) #True
print(isAvailable(m, (1100,1130))) #True
# print(isAvailable(m, (930,1030))) #True




# assert(isAvailable(isAvailable(m, (930,1030))) == True)