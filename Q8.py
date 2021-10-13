import json

w=["neelam","programer","24","2400"]
x=["komal","trainer","24","20000"]
y=["anuradha","HR","25","40000"]
z=["Abhishek","manager","29","63000"] 

h=["name","designation","age","salary"]

b={}
c={}
f={}
e={}

d={"emp1":b,"emp2":c,"emp3":f,"emp4":e}

for i in range(len(w)):
     b.update({h[i]:w[i]})
for i in range(len(x)):
     c.update({h[i]:x[i]})
for i in range(len(y)):
     f.update({h[i]:y[i]})
for i in range(len(z)):
     e.update({h[i]:z[i]})
t=open("vaishu.json","w")
json.dump(d,t,indent=3)

