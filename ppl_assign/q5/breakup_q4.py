import happify
import json
from random import randint

happify.happ()
happify.compat()

def antiromeo():
    with open("boydata.json") as ba:
        boyd = json.load(ba)
    with open("girldata.json") as ba:
        girld = json.load(ba)

    for i in range(0,len(happify.couples)):
        guy = happify.couples[i][0]
        girl = happify.couples[i][1]
        boyd[guy]['commited'] = "false"
        boyd[guy]['girl'] = " "
        girld[girl]['commited'] = "true"
    with open('boydata.json', 'w') as f:
        json.dump(boyd, f)
        print("done")

def romeo():
    with open("boydata.json") as ba:
        boyd = json.load(ba)
    with open("girldata.json") as ba:
        girld = json.load(ba)
    for keyg, valueg in girld.items():
        if(valueg['commited']=='true'):
            count = 1
            while(count):
                bno = 'b' + str(randint(0,20))
                if(boyd[bno]['min_req']<valueg['attractiveness'] and boyd[bno]['budget']>valueg['maintainanace']):
                    count = 0
                    valueg['boy'] = bno
                    boyd[bno]['girl'] = keyg
                    boyd[bno]['commited'] = "true"
                    break
    with open('boydata.json', 'w') as f:
        json.dump(boyd, f)
        print("done")
    with open('girldata.json', 'w') as f:
        json.dump(girld, f)
        print("done")

antiromeo()