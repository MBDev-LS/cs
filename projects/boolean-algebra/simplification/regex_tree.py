
from pprint import pprint

from identities import identitiesDict
import dynamic_indentities

expression = 'A+(B.C)'

dynamicIdentList = dynamic_indentities.generate_dynamic_identities_list(expression, identitiesDict)

pprint(dynamicIdentList)
