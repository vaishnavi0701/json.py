import json


a={"shopping_list":
        { "chaco":"15",
            "Biscuits":"50",
            "Diary_milk":"30",
            "ice_cream":"20",}}

print(type(a))
f=open("shopping.json","w")
json.dump(a,f,indent=4)
name=input("which thing u wants to buy:")
items=int(input("how many items u wants to buy:"))

for key in a:
    for value in a:
        for i ,k in a[key].items():
            if i==name:
                t=int(k)-items
                print("remaining items",t)





