import json
import random
from random import randint


class test_data(object):

    def __init__(self,path1,path2,path3):
        for i in range(1,20):
            with open(path1) as da:
                data = json.load(da)
            add_data = {}
            girl_type=["choosy","normal","desperate"]
            add_data['g'+str(i)] = {
                "attractiveness": randint(0,9),
                "maintainanace": randint(0,500),
                "intel": randint(0,100),
                "commited": "false",
                "boy": " ",
                "type": random.choice(girl_type)
            }
            print(add_data)
            data.update(add_data)
            with open(path1, 'w') as f:
                json.dump(data, f)

        for i in range(1,50):
            with open(path2) as da:
                data = json.load(da)
            add_data = {}
            boy_type=["miser","generous","geek"]
            add_data['b'+str(i)] = {
                "attractiveness": randint(0,9),
                "budget": randint(0,500),
                "intel": randint(0,100),
                "commited": "false",
                "girl": " ",
                "type": random.choice(boy_type),
                "min_req": randint(0,10),
                "total": " "
            }
            print(add_data)
            data.update(add_data)
            with open(path2, 'w') as f:
                json.dump(data, f)

        for i in range(1,40):
            with open(path3) as da:
                data = json.load(da)
            add_data = {}
            type_list = ['essential','utility','luxury']
            add_data['gift'+str(i)] = {
                "type": random.choice(type_list),
                "price": randint(0,100),
                "value": " ",
                "from": " ",
                "to": " "
            }
            print(add_data)
            data.update(add_data)
            with open(path3, 'w') as f:
                json.dump(data, f)

data = test_data("girldata.json","boydata.json","giftdata.json")