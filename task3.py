import json
lst =[]
with open("values.json", "r") as f:
    data = json.loads(f.read())
    for i in data['values']:
        lst.append(i['value'])

#for el in lst: TODO!
   # lst.append({'value': el})

with open('tests.json', 'w') as f:
    json.dump(lst, f)