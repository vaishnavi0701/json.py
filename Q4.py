import json

dict={'4': 5,'6': 7,'1': 3,'2': 4}
data=json.dumps(dict)
print(data)

data1 = json. dumps(dict, sort_keys=True)
print(data1)


# dict={"1": 3,"2": 4,"4": 5,"6": 7}