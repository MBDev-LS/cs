dominanceOr = r'A\+1' # Result '0'
dominanceAnd = r'A\*0=0' # Result '0'

identityOr = r'A+0' # Result 'A'
identityAnd = r'A+1' # Result 'A'

idempotenceOr = 'A\+A' # Result 'A'
idempotenceAnd = 'A\.A' # Result 'A'

complementarityOr = 'A\+~A' # Result '1'
complementarityAnd = 'A\.~A' # Result '0'

orCommutativityOne = 'A+B' # Result 'B+A'
andCommutativity = 'A.B' # Result 'B.A'

associativityOr = '\(A+B\)+C' # Result '(1)'