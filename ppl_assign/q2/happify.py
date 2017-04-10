import random
from commit import commitstatus
import json
from random import randint
from log import who_got_fooled
import math
from operator import itemgetter

couples = []


def happ():
    k=0
    initdata = commitstatus()
    with open("boydata.json") as ba:
        boyd = json.load(ba)
    with open("giftdata.json") as ba:
        giftd = json.load(ba)
    with open("girldata.json") as ba:
        girld = json.load(ba)
    #print(boyd, girld,giftd)

    for keyb, valueb in boyd.items():
        if(valueb['commited']=='true'):
            mygirl = valueb['girl']
            for keyg, valueg in girld.items():
                if(keyg == mygirl):
                    mygtyp = valueg['type']
                    mygmain = valueg['maintainanace']
                    mygintel = valueg['intel']
            bh=1
            gh=1
            if(valueb['type']=='miser'):
                bh = valueb['budget']-valueb['total']
                if(mygtyp =='choosey'):
                    gh = math.log10(valueb['total']-mygmain)
                elif(mygtyp=='normal'):
                    gh = valueb['total']-mygmain
                elif(mygtyp=='desperate'):
                    gh = math.exp(valueb['total'] - mygmain)
                happ = bh + gh
                couples.append([keyb,mygirl,bh,gh,happ])

            if (valueb['type'] == 'generous'):
                if (mygtyp == 'choosey'):
                    gh = math.log10(valueb['total'] - mygmain)
                elif (mygtyp == 'normal'):
                    gh = valueb['total'] - mygmain
                elif (mygtyp == 'desperate'):
                    gh = math.exp(valueb['total'] - mygmain)
                bh=gh
                happ = bh + gh
                couples.append([keyb, mygirl, bh, gh, happ])

            if (valueb['type'] == 'geek'):
                bh = mygintel
                if (mygtyp == 'choosey'):
                    gh = math.log10(valueb['total'] - mygmain)
                elif (mygtyp == 'normal'):
                    gh = valueb['total'] - mygmain
                elif (mygtyp == 'desperate'):
                    gh = math.exp(valueb['total'] - mygmain)
                happ = bh + gh
                couples.append([keyb, mygirl, bh, gh, happ])
    coupless = sorted(couples, key=itemgetter(4), reverse=True)
    print('Top 5 happy couples')
    for i in range(0,len(coupless)):
        print(coupless[i][0])

def compat():
    initdata = commitstatus()
    with open("boydata.json") as ba:
        boyd = json.load(ba)
    with open("giftdata.json") as ba:
        giftd = json.load(ba)
    with open("girldata.json") as ba:
        girld = json.load(ba)

    couples2 = []
    for i in range(0,len(couples)):
        boy = couples[i][0]
        girl = couples[i][1]
        for keyb, valueb in boyd.items():
            if(boy==keyb):
                bint = valueb['intel']
                batt = valueb['attractiveness']
                bbud = valueb['budget']
                break

        for keyg, valueg in girld.items():
            if(girl==keyg):
                gint = valueg['intel']
                gatt = valueg['attractiveness']
                gmain = valueg['maintainanace']
                break
        compat = (bbud-gmain)+ abs(batt-gatt) +abs(bint-gint)
        couples2.append([boy, girl, compat])
    couplesss = sorted(couples2, key=itemgetter(2), reverse=True)
    print('Top 5 compat couples')
    for i in range(0,len(couplesss)):
        print(couplesss[i][0])