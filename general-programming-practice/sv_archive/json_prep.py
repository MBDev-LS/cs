
import json

with open('/Users/louisstevens/Documents/cs/general-programming-practice/_ignore__sv_archive/people_parameters.json', 'r') as f:
    parametersList = json.loads(f.read())

print(parametersList)

with open('/Users/louisstevens/Documents/cs/general-programming-practice/_ignore__sv_archive/people_names.json', 'r') as f:
    namesList = json.loads(f.read())

peopleDictList = []

for i, name in enumerate(namesList):
    peopleDictList.append({
        'name': name,
        'params': parametersList[i]
    })

print(peopleDictList)
