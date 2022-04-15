
import re
from pprint import pprint

from identities import identitiesDict
import dynamic_indentities

expression = 'A+(B.C)'

dynamicIdentList = dynamic_indentities.generate_dynamic_identities_list(expression, identitiesDict)

# pprint(dynamicIdentList)

def recursive_simplification(expression, dynamicIdentList, simplificationHistory=None):
	simplificationHistory = simplificationHistory if simplificationHistory is not None else [expression]
	histories = [simplificationHistory]

	for identity in dynamicIdentList:
		matchObject = re.match(identity['startRegex'], expression)
		if matchObject is None:
			continue

		newExpression = re.sub(identity['startRegex'], identity['resultRegex'].replace('\\', ''), expression)

		if newExpression in simplificationHistory:
			continue

		simplificationHistory.append(newExpression)

		exendedHistorys = recursive_simplification(newExpression, dynamicIdentList, simplificationHistory)
		histories += exendedHistorys
	
	return histories

print(recursive_simplification(expression, dynamicIdentList))
