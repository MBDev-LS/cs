# dominanceOr = 'A\+1' # Result '0'
# dominanceAnd = 'A\.0' # Result '0'

# identityOr = 'A\+0' # Result 'A'
# identityAnd = 'A\.1' # Result 'A'

# idempotenceOr = 'A\+A' # Result 'A'
# idempotenceAnd = 'A\.A' # Result 'A'

# complementarityOr = 'A\+~A' # Result '1'
# complementarityAnd = 'A\.~A' # Result '0'

# orCommutativityOne = 'A\+B' # Result 'B+A'
# andCommutativity = 'A\.B' # Result 'B.A'

# associativityOr = '\(A+B\)+C' # Result 'A+(B+C)'
# associativityAnd = '\(A.B\).C' # Result 'A.(B.C)'

# distributivityOr = 'A+\(B\.C\)' # Result '(A+B).(A+C)'
# distributivityAnd = 'A.\(B\+C\)' # Result '(A.B)+(A.C)'

# absorptionOr = 'A\.\(A\+B\)' # Result 'A'
# absorptionAnd = 'A\.\(A\+B\)' # Result 'A'

# deMorgansOr = 'A\+B' # Result '~(~A.~B)'
# deMorgansAnd = 'A\.B' # Result '~(~A+~B)'

identitiesDict = {
	'metadata': {
		'vars': ('A', 'B', 'C')
	},
	'identities': [
		{
			'name': 'logic_inverse',
			'varCount': 0,
			'versions': {
				'expression1': {
						'regex1': '~0',
						'regex2': '1'
					},
				'expression2': {
						'regex1': '~1',
						'regex2': '0'
					}
			}
		},
		{
			'name': 'involution',
			'varCount': 1,
			'versions': {
				'expression1': {
						'regex1': '~~A',
						'regex2': 'A'
					},
			}
		},
		{
			'name': 'dominance',
			'varCount': 1,
			'versions': {
				'o': {
						'regex1': 'A\+1',
						'regex2': '0'
					},
				'and': {
						'regex1': 'A\.0',
						'regex2': '0'
					}
			}
		},
		{
			'name': 'identity',
			'varCount': 1,
			'versions': {
				'o': {
						'regex1': 'A\+0',
						'regex2': 'A'
					},
				'and': {
						'regex1': 'A\.1',
						'regex2': 'A'
					}
			}
		},
		{
			'name': 'idempotence',
			'varCount': 1,
			'versions': {
				'o': {
						'regex1': 'A\+A',
						'regex2': 'A'
					},
				'and': {
						'regex1': 'A\.A',
						'regex2': 'A'
					}
			}
		},
		{
			'name': 'complementarity',
			'varCount': 1,
			'versions': {
				'o': {
						'regex1': 'A\+~A',
						'regex2': '1'
					},
				'and': {
						'regex1': 'A\.~A',
						'regex2': '0'
					}
			}
		},
		{
			'name': 'commutativity',
			'varCount': 2,
			'versions': {
				'o': {
						'regex1': 'A\+B',
						'regex2': 'B\+A'
					},
				'and': {
						'regex1': 'A\.B',
						'regex2': 'B\.A'
					}
			}
		},
		{
			'name': 'associativity',
			'varCount': 3,
			'versions': {
				'o': {
						'regex1': '\(A+B\)\+C',
						'regex2': 'A\+\(B\+C\)'
					},
				'and': {
						'regex1': '\(A.B\)\.C',
						'regex2': 'A\.\(B\.C\)'
					}
			}
		},
		{
			'name': 'distributivity',
			'varCount': 3,
			'versions': {
				'o': {
						'regex1': 'A\+\(B\.C\)',
						'regex2': '\(A\+B\)\.\(A\+C\)'
					},
				'and': {
						'regex1': 'A\.\(B\+C\)',
						'regex2': '\(A\.B\)\+\(A\.C\)'
					}
			}
		},
		{
			'name': 'absorption',
			'varCount': 2,
			'versions': {
				'o': {
						'regex1': 'A\.\(A\+B\)',
						'regex2': 'A'
					},
				'and': {
						'regex1': 'A\.\(A\+B\)',
						'regex2': 'A'
					}
			}
		},
		{
			'name': 'deMorgans',
			'varCount': 2,
			'versions': {
				'o': {
						'regex1': 'A\+B',
						'regex2': '~\(~A\.~B\)'
					},
				'and': {
						'regex1': 'A\.B',
						'regex2': '~\(~A\+~B\)'
					}
			}
		},
	]
}