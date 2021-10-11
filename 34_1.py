import json

data = {"Model" : "Malibu", "Color" : "Black", "Year":2020, "Price":40000}

with open('data.json', 'w') as f:
    json.dump(data, f)
    
data_json = json.dumps(data)
    
print(data_json)
print(type(data_json))
