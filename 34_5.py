import json

with open('api-result.json') as f:
    file = json.load(f)

a = file['query']['pages']['13801']['extract']
print(a[:(a.index('—'))])
print(a[(a.index('—')+2):])