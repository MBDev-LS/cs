dominanceOr = r'A\+1' # Result '0'
dominanceAnd = r'A\.0' # Result '0'

identityOr = r'A\+0' # Result 'A'
identityAnd = r'A\.1' # Result 'A'

idempotenceOr = r'A\+A' # Result 'A'
idempotenceAnd = r'A\.A' # Result 'A'

complementarityOr = r'A\+~A' # Result '1'
complementarityAnd = r'A\.~A' # Result '0'

orCommutativityOne = r'A\+B' # Result 'B+A'
andCommutativity = r'A\.B' # Result 'B.A'

associativityOr = r'\(A+B\)+C' # Result 'A+(B+C)'
associativityAnd = r'\(A.B\).C' # Result 'A.(B.C)'

distributivityOr = r'A+\(B\.C\)' # Result '(A+B).(A+C)'
distributivityAnd = r'A.\(B\+C\)' # Result '(A.B)+(A.C)'

absorptionOr = r'A\.\(A\+B\)' # Result 'A'
absorptionAnd = r'A\.\(A\+B\)' # Result 'A'

deMorgansOr = r'A\+B' # Result '~(~A.~B)'
deMorgansAnd = r'A\.B' # Result '~(~A+~B)'

identities = [
	{
		'name': 'logic_inverse',
		'varCount': 0,
		'versions': {
			'expression1': {
					'regex1': r'~0',
					'regex2': r'1'
				},
			'expression2': {
					'regex1': r'~1',
					'regex2': r'0'
				}
		}
	},
	{
		'name': 'involution',
		'varCount': 1,
		'versions': {
			'expression1': {
					'regex1': r'~~A',
					'regex2': r'A'
				},
		}
	},
	{
		'name': 'dominance',
		'varCount': 1,
		'versions': {
			'or': {
					'regex1': r'A\+1',
					'regex2': r'0'
				},
			'and': {
					'regex1': r'A\.0',
					'regex2': r'0'
				}
		}
	},
	{
		'name': 'identity',
		'varCount': 1,
		'versions': {
			'or': {
					'regex1': r'A\+0',
					'regex2': r'A'
				},
			'and': {
					'regex1': r'A\.1',
					'regex2': r'A'
				}
		}
	},
	{
		'name': 'idempotence',
		'varCount': 1,
		'versions': {
			'or': {
					'regex1': r'A\+A',
					'regex2': r'A'
				},
			'and': {
					'regex1': r'A\.A',
					'regex2': r'A'
				}
		}
	},
	{
		'name': 'complementarity',
		'varCount': 1,
		'versions': {
			'or': {
					'regex1': r'A\+~A',
					'regex2': r'1'
				},
			'and': {
					'regex1': r'A\.~A',
					'regex2': r'0'
				}
		}
	},
	{
		'name': 'commutativity',
		'varCount': 2,
		'versions': {
			'or': {
					'regex1': r'A\+B',
					'regex2': r'B\+A'
				},
			'and': {
					'regex1': r'A\.B',
					'regex2': r'B\.A'
				}
		}
	},
	{
		'name': 'associativity',
		'varCount': 3,
		'versions': {
			'or': {
					'regex1': r'\(A+B\)\+C',
					'regex2': r'A\+\(B\+C\)'
				},
			'and': {
					'regex1': r'\(A.B\)\.C',
					'regex2': r'A\.\(B\.C\)'
				}
		}
	},
	{
		'name': 'distributivity',
		'varCount': 3,
		'versions': {
			'or': {
					'regex1': r'A\+\(B\.C\)',
					'regex2': r'\(A\+B\)\.\(A\+C\)'
				},
			'and': {
					'regex1': r'A\.\(B\+C\)',
					'regex2': r'\(A\.B\)\+\(A\.C\)'
				}
		}
	},
	{
		'name': 'absorption',
		'varCount': 2,
		'versions': {
			'or': {
					'regex1': r'A\.\(A\+B\)',
					'regex2': r'A'
				},
			'and': {
					'regex1': r'A\.\(A\+B\)',
					'regex2': r'A'
				}
		}
	},
	{
		'name': 'deMorgans',
		'varCount': 2,
		'versions': {
			'or': {
					'regex1': r'A\+B',
					'regex2': r'~\(~A\.~B\)'
				},
			'and': {
					'regex1': r'A\.B',
					'regex2': r'~\(~A\+~B\)'
				}
		}
	},
]
