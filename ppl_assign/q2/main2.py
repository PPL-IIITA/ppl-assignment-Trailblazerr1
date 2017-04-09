import json
from commit import commitstatus
from happify import happ

def main2def():
    initdata = commitstatus()
    boyd = initdata.datab
    with open("giftdata.json") as ba:
        datat = json.load(ba)
    girld = initdata.datag
    ke = datat.keys()
    sort_key = sorted(ke, key=lambda ip: datat[ip]['price'], reverse=False)
    #print(datat[sort_key[0]])
    i = 0
    for keyg, valueg in boyd.items():
        if(valueg['commited']=="true"):
            if(valueg['type']=="miser"):
                girl = valueg['girl']
                i = 0
                sum = 0
                while(sum<=girld[girl]['maintainanace'] and i<40):
                    if (datat[sort_key[i]]['from'] == " "):
                        sum = sum + datat[sort_key[i]]['price']
                        if(sum<girld[girl]['maintainanace']):
                            datat[sort_key[i]]['from']=keyg
                            datat[sort_key[i]]['to']=girl
                          #  print(keyg+' has to give '+ sort_key[i]+" to "+girl)
                         #   print("O guy! ask for a return gift")
                            i+=1
                        else:
                            break
                    else:
                        i+=1
                valueg['total']=sum
  #              print(valueg['total'])
            elif(valueg['type']=="geek"):
                girl = valueg['girl']
                i = 0
                sum=0
                while(sum<=girld[girl]['maintainanace'] and i<40):
                    if (datat[sort_key[i]]['from'] == " "):
                        sum = sum + datat[sort_key[i]]['price']
                        if(sum<girld[girl]['maintainanace']):
                            datat[sort_key[i]]['from']=keyg
                            datat[sort_key[i]]['to']=girl
                            i+=1
                        else:
                            break
                    else:
                        i+=1
                valueg['total']=sum
            elif(valueg['type']=="generous"):
                girl = valueg['girl']
                i = 0
                sum=0
                while(sum<=valueg["budget"] and i<40):
                    if (datat[sort_key[i]]['from'] == " "):
                        sum = sum + datat[sort_key[i]]['price']
                        if(sum<valueg["budget"]):
                            datat[sort_key[i]]['from']=keyg
                            datat[sort_key[i]]['to']=girl
                          #  print(keyg+' has to give '+ sort_key[i]+" to "+girl)
                           # print("O guy! ask for a return gift")
                            i+=1
                        else:
                            break
                    else:
                        i+=1
                valueg['total']=sum
#                print(datat[sort_key[11]]['to'])
    with open('boydata.json', 'w') as f:
        json.dump(boyd, f)
        print("done")

happ()
