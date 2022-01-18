import regex

import re

# print(re.match(r"[A-Z]{3}\sR[0-9]{1,2},\s?([0-9]{1,3})", 'LDR R0, 99'))
# print(re.search(r"'([0-9]{1,3})'", 'LDR R0, 99'))
# print(re.findall(r"[A-Z]{3}\sR[0-9]{1,2},\s?[0-9]{1,3}", 'LDR R0, 99'))

# print(re.findall(r"\s?[A-Z]{3}", 'LDR R0, 99'))

INSTRUCTION_SET = {
	'LDR': {'code': 1, 'regex_group': 'mGroup'},
	'STR': {'code': 1, 'regex_group': 'mGroup'},
	'ADD': {'code': 1, 'regex_group': 'gGroup'},
	'SUB': {'code': 1, 'regex_group': 'gGroup'},
	'MOV': {'code': 1, 'regex_group': 'lGroup'},
	'CMP': {'code': 1, 'regex_group': 'lGroup'},
	'B': {'code': 1, 'regex_group': 'B'},
	'B+': {'code': 1, 'regex_group': 'B+'},
	'AND': {'code': 1, 'regex_group': 'gGroup'},
	'ORR': {'code': 1, 'regex_group': 'gGroup'},
	'EOR': {'code': 1, 'regex_group': 'gGroup'},
	'MVN': {'code': 1, 'regex_group': 'lGroup'},
	'LSL': {'code': 1, 'regex_group': 'gGroup'},
	'LSR': {'code': 1, 'regex_group': 'gGroup'},
	'HALT': {'code': 1, 'regex_group': 'HALT'},
}

regexTypes = {
	"mGroup":  r"\sR(1[0-2]|[0-9]),\s?[0-9]{1,3}",
	"gGroup":  r"\sR(1[0-2]|[0-9]),\sR(1[0-2]|[0-9]),\s?(R(1[0-2]|[0-9])|#\d+)",
	"b":       r"B\s[a-zA-Z]+",
	"B+" :     r"B(ET|GT|NE|LT)\s[a-zA-Z]+",
	"HALT":    r"HALT",
	"labels": r"\s*[a-zA-Z]+:",
}

def validate(instruction: str, line_num: int): # , data_info: dict
	instruction_type = re.findall(r"\s?[A-Z]{3}\s", instruction)

	if len(instruction_type) == 0 or instruction_type[0][:-1] not in INSTRUCTION_SET:
		return "bad instruction"

	instruction_type = instruction_type[0][:-1]

	if INSTRUCTION_SET[instruction_type]['regex_group'] in ['mGroup', 'gGroup']:
		if re.match(instruction_type + regexTypes[INSTRUCTION_SET[instruction_type]['regex_group']], instruction) is None:
			return "syntax error (1)"
		print(re.match(instruction_type + regexTypes[INSTRUCTION_SET[instruction_type]['regex_group']], instruction).groups())
    
	# if re.search(9r"'([0-9]{1,3})'", 'LDR R0, 99')
	
	return True

# LDR R0, 99

print(re.search(r"LDR\sR[0-9]{1,2},\s?([0-9]{1,3})", 'LDR R0, 99').group(1))
print(validate('LDR R0, 9999', 0))
