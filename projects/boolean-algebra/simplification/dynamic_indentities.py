
import itertools
from pprint import pprint

from identities import identitiesDict

operatorsDict = {
	'~': {'precedence': 4, 'operandCount': 1},
	'.': {'precedence': 3, 'operandCount': 2},
	'+': {'precedence': 2, 'operandCount': 2},
}

expression = 'A+B+A'

variables = tuple(set([char for char in expression if char not in list(operatorsDict.keys()) + ['(', ')']]))

dynamicIdentitiesList = []

for identity in identitiesDict['identities']:
    if identity['varCount'] > len(variables):
        continue

    varPermutations = list(itertools.permutations(variables, identity['varCount']))
    
    for perm in varPermutations:
        for subIdentity in identity['versions']:
            ident1 = {
                'name': identity['name'],
                'startRegex': identity['versions'][subIdentity]['regex1'],
                'resultRegex': identity['versions'][subIdentity]['regex2'],
            }
            

            ident2 = {
                'name': identity['name'],
                'startRegex': identity['versions'][subIdentity]['regex2'],
                'resultRegex': identity['versions'][subIdentity]['regex1'],
            }
            
            for i in range(0, identity['varCount']):
                ident1['startRegex'] = ident1['startRegex'].replace(identitiesDict['metadata']['vars'][i], perm[i])
                ident1['resultRegex'] = ident1['resultRegex'].replace(identitiesDict['metadata']['vars'][i], perm[i])

                ident2['startRegex'] = ident2['startRegex'].replace(identitiesDict['metadata']['vars'][i], perm[i])
                ident2['resultRegex'] = ident2['resultRegex'].replace(identitiesDict['metadata']['vars'][i], perm[i])

            dynamicIdentitiesList.append(ident1)
            dynamicIdentitiesList.append(ident2)

print(dynamicIdentitiesList)
pprint(dynamicIdentitiesList)