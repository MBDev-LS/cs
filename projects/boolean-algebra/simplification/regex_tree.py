
import copy
import re
from pprint import pprint
import random

from identities import identitiesDict
import dynamic_indentities

expression = 'A.(B+C)'

dynamicIdentList = dynamic_indentities.generate_dynamic_identities_list(expression, identitiesDict)

def checkForRepeat(string) -> bool: # Source: https://stackoverflow.com/a/29489919/15394242
    for i in range(len(string)):
        subString = string[i:]
        firstResult = (subString+subString).find(subString, 1, -1)
        result =  False if firstResult == -1 else True

        if result is True:
            return True
    
    return False

def recursive_simplification(expression, dynamicIdentList, simplificationHistory=None, depth=1):
	if depth > 2:
		return []

	
	# random.shuffle(dynamicIdentList)
	simplificationHistory = simplificationHistory if simplificationHistory is not None else [{
			'expression': expression,
			'depth': 0,
			'identity_used': ''
		}]
	histories = []

	for identity in dynamicIdentList:
		print(f"Checking {expression} for {identity['name']} ({identity['startRegex']} -> {identity['resultRegex']})")
		matchObject = re.match(identity['startRegex'], expression)

		if matchObject is None:
			print(f"{identity['name']} ({identity['startRegex']} -> {identity['resultRegex']}) not found in {expression}")
			continue

		newExpression = re.sub(identity['startRegex'], identity['resultRegex'].replace('\\', ''), expression)
		print(f"Created new expression using {identity['name']}, {expression} -> {newExpression}")

		if newExpression in [historicDict['expression'] for historicDict in simplificationHistory]:
			print(f"Rejected {newExpression} as it was in {', '.join([historicDict['expression'] for historicDict in simplificationHistory])}")
			continue
		elif checkForRepeat('-'.join([historicDict['identity_used'] for historicDict in simplificationHistory] + [identity['name']])) is True:
			print(f"Rejected {newExpression} as principal_period returned True")
			continue

		print(checkForRepeat('-'.join([historicDict['identity_used'] for historicDict in simplificationHistory])),
		'-'.join([historicDict['identity_used'] for historicDict in simplificationHistory]))
		
		# if len(simplificationHistory) > 10:
		# 	# print(simplificationHistory, set([historicDict['expression'] for historicDict in simplificationHistory][int(round(len([historicDict['expression'] for historicDict in simplificationHistory])*0.75)):]))
		# 	if len(set([historicDict['expression'] for historicDict in simplificationHistory][int(round(len([historicDict['expression'] for historicDict in simplificationHistory])*0.75)):])) <= 2:
		# 		continue

		simplificationHistory.append({
			'expression': newExpression,
			'depth': 0,
			'identity_used': identity['name']
		})

		print(f'Appended:\n{simplificationHistory[-1]} to simplificationHistory')

		print(f"Calling exendedHistorys({newExpression}, dynamicIdentList, {simplificationHistory})")
		exendedHistorys = recursive_simplification(newExpression, dynamicIdentList, copy.deepcopy(simplificationHistory), depth+1)
		print(f"recursive_simplification returned {exendedHistorys}, extending histories, {histories} by it")
		histories += exendedHistorys
	
	print(f"recursive_simplification returning {histories if len(histories) > 0 else [simplificationHistory]}")
	return histories if len(histories) > 0 else [simplificationHistory]

results = recursive_simplification(expression, dynamicIdentList)

for resultList in results:
	print(' -> '.join([result['expression'] for result in resultList]))

