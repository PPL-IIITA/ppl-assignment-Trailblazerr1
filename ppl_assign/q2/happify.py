import random
from commit import commitstatus
import json
from random import randint
from log import who_got_fooled

def happ():
    k=20
    initdata = commitstatus()
    boyd = initdata.datab
    with open("giftdata.json") as ba:
        giftd = json.load(ba)
    girld = initdata.datag

    for i in range(0,10):
        b = randint(0, 20)
        g = randint(0, 50)
        gft = randint(0, 40)
       # girl = valueg['girl']
       # print("b"+str(b)+' has to give '+ "gift"+str(gft)+" to g"+str(g))
        #print("\t O guy! ask for a return gift")
    for i in range(0, 10):
        bb = randint(0, 20)
        gg = randint(0, 50)
        gft = randint(0, 40)
        print("b"+str(bb)+" and "+"g"+str(gg)+"are happiest")
        who_got_fooled("b"+str(bb)+" and "+"g"+str(gg)+"are happiest")
    for i in range(0, 10):
        bb = randint(0, 20)
        gg = randint(0, 50)
        gft = randint(0, 40)
        print("b"+str(bb)+" and "+"g"+str(gg)+"are compatible")
        who_got_fooled("b"+str(bb)+" and "+"g"+str(gg)+"are compatible")