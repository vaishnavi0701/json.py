
# {"a":  1,"a":  2,"a":  3,"a": 4,"b": 1, "b": 2}

# {'a': 4, 'b': 2}





import json

dict='{"a":  1,"a":  2,"a":  3,"a": 4,"b": 1,"b": 2}'

print(dict)

data1=json.loads(dict)
print(data1)
