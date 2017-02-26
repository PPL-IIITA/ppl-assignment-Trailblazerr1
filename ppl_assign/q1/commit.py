import json
from log import who_got_fooled

class commitstatus(object):
    def __init__(self):
        with open("girldata.json") as da:
            datag = json.load(da)
        with open("boydata.json") as ba:
            datab = json.load(ba)
      #  for girl in datag:
        for keyg, valueg in datag.items():
            for keyb,valueb in datab.items():
                if(valueb['commited']=="false" and valueb['min_req']<valueg['attractiveness'] and valueb['budget']>valueg['maintainanace']):
                    valueg['commited']="true"
                    valueb['commited']="true"
                    valueg['boy'] = keyb
                    valueb['girl'] = keyg
                    print('Poor ' + keyb +' will have to bear with '+ keyg)
                    who_got_fooled('Poor ' + keyb +' will have to bear with '+ keyg)
                    break

com = commitstatus()