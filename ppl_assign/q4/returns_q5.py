import json
from log import who_got_fooled

class commitstatus(object):
    def __init__(self):
        with open("girldata.json") as da:
            self.datag = json.load(da)
        with open("boydata.json") as ba:
            self.datab = json.load(ba)
        ke = self.datab.keys()
        sort_key = sorted(ke, key=lambda ip: self.datab[ip]['attractiveness'], reverse=False)
        ke = self.datag.keys()
        sort_key = sorted(ke, key=lambda ip: self.datag[ip]['maintainanace'], reverse=False)
      #  print(self.datab,self.datag)
#logic goes here
        i=0
        while(i<20):
            toggle = True
            if(i%2==0):
                print("one")
                for keyg, valueg in self.datag.items():
                    for keyb,valueb in self.datab.items():
                #        print('Y')
                        if(valueb['commited']=="false" and valueb['min_req']<valueg['attractiveness'] and valueb['budget']>valueg['maintainanace']):
                            toggle = False
                            valueg['commited']="true"
                            valueb['commited']="true"
                            valueg['boy'] = keyb
                            valueb['girl'] = keyg
                       #     print('Poor ' + keyb +' will have to bear with '+ keyg)
                            who_got_fooled('Poor ' + keyb +' will have to bear with '+ keyg)
                            print('Yayy1')
                            break
                    else:
                        continue
                    break
            else:
                print("two")
                for keyb, valueb in self.datab.items():
                    for keyg,valueg in self.datag.items():
                        if(valueg['commited']=="false" and valueb['min_req']<valueg['attractiveness'] and valueb['budget']>valueg['maintainanace']):
                            toggle = False
                            valueg['commited']="true"
                            valueb['commited']="true"
                            valueg['boy'] = keyb
                            valueb['girl'] = keyg
                       #     print('Poor ' + keyb +' will have to bear with '+ keyg)
                            who_got_fooled('Poor ' + keyb +' will have to bear with '+ keyg)
                            print('Yayy2')
                            break
                    else:
                        continue
                    break
            i+=1

com = commitstatus()