
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
2


REGEXTYPES = {
	"mGroup": r"\sR(1[0-2]|[0-9]),\s?[0-9]{1,3}", # second bit makes no sense
	"gGroup": r"\sR(1[0-2]|[0-9]),\sR(1[0-2]|[0-9]),\s?(R(1[0-2]|[0-9])|#\d+)",
	"b":      r"B\s[a-zA-Z]+",
	"B+" :    r"B(ET|GT|NE|LT)\s[a-zA-Z]+",
	"HALT":   r"HALT",
	"labels":r"(\s*[a-zA-Z]+:)*",
}

class Operand:
	def __init__(self, value, addressingMode) -> None:
		self.value = value
		self.adressingMode = addressingMode

def splitRegex(regexStr: str, *args) -> list:
	splitChars = args

	intialList = regexStr.split(splitChars[0])
	endList = []

	for i in range(1, len(splitChars)):
		
		for string in intialList:
			endList += string.split(splitChars[i])

		if i < len(splitChars)-1:
			intialList = endList
			endList = []

	while '' in endList:
		endList.remove('')
	
	return endList

def reportDetailedError(instructionList: str, errorIndex: int):
	# Use error index and length of corresponding
	# string in instructionList to place error.
	# 
	# Then use instruction index to select error:
	# If there is a label in the instruction, and
	# error index is 0 then the error is with the
	# label. If no label is present and the error
	# index is 0 the the issue is with the
	# 'instruction type'. If the error index > 1,
	# the error will depend  the 'instruction
	# type', will need system for checking this.
	# 
	# The infomation given by the current parameters
	# is sufficient if this is implemented in the
	# way I currently envisage it.
	# 
	# You may decide whether to use print or to
	# raise an exception when reporting an error.
	# If print is used, consider that the program
	# should then be stopped accordingly, likely
	# with the use of exit().
	pass 

def steppedSyntaxCheck(instruction: str, line_num: int):
	instruction_type = re.findall(r"\s?([A-Z]{1}|[A-Z]{3,4})\s", instruction)[0].upper().strip()
	if instruction.split(' ')[0].upper() not in INSTRUCTION_SET:
		instructionRegexList = [REGEXTYPES['labels'], instruction_type] + splitRegex(REGEXTYPES[INSTRUCTION_SET[instruction_type]['regex_group']],',\s?', ',\s', '\s?', '\s') + ['$']
	else:
		instructionRegexList = [instruction_type] + splitRegex(REGEXTYPES[INSTRUCTION_SET[instruction_type]['regex_group']],',\s?', ',\s', '\s?', '\s') + ['$']

	

	instructionList = instruction.split(' ')
	print(instructionList, instructionRegexList)

	for i, regexStr in enumerate(instructionList):
		if i >= len(instructionList):
			reportDetailedError(instructionList, i)

		# Now check if instructionList[i] matches the regexStr



def instructionSyntaxCheck(instruction: str, line_num: int):
	instruction_type = re.findall(r"\s?([A-Z]{1}|[A-Z]{3,4})\s", instruction)

	if len(instruction_type) == 0 or instruction_type[0].strip() not in INSTRUCTION_SET:
		return f"error: unknown instruction \'{instruction_type[0]}\' on line {line_num}"

	instruction_type = instruction_type[0].strip() # Can this not be done betfore first if statement to make this section simplier
	
	

	if INSTRUCTION_SET[instruction_type]['regex_group'] in ['mGroup', 'gGroup']:
		steppedSyntaxCheck(instruction, line_num)
		
		if re.match('^' + instruction_type + REGEXTYPES[INSTRUCTION_SET[instruction_type]['regex_group']] + '$', instruction) is None:
			return f"error: syntax error on line {line_num}"
		# print(re.match(instruction_type + REGEXTYPES[INSTRUCTION_SET[instruction_type]['regex_group']], instruction).groups())
    
	# if re.search(9r"'([0-9]{1,3})'", 'LDR R0, 99')
	
	return True

# def validate(instruction: str, line_num: int): # , data_info: dict
# 	instruction_type = re.findall(r"\s?([A-Z]{1}|[A-Z]{3,4})\s", instruction)

# 	if len(instruction_type) == 0 or instruction_type[0].strip() not in INSTRUCTION_SET:
# 		return "bad instruction"

# 	instruction_type = instruction_type[0].strip()

# 	if INSTRUCTION_SET[instruction_type]['regex_group'] in ['mGroup', 'gGroup']:
# 		if re.match(instruction_type + REGEXTYPES[INSTRUCTION_SET[instruction_type]['regex_group']] + '$', instruction) is None:
# 			return "syntax error (1)"
# 		# print(re.match(instruction_type + REGEXTYPES[INSTRUCTION_SET[instruction_type]['regex_group']], instruction).groups())
    
# 	# if re.search(9r"'([0-9]{1,3})'", 'LDR R0, 99')
	
# 	return True

# LDR R0, 99

print(re.search(r"LDR\sR([0-9]{1,2}),\s?([0-9]{1,3})", 'LDR R0, 99').groups())
print(instructionSyntaxCheck('awjdnk NDER R2, 9999', 0))
print(instructionSyntaxCheck('LDR R0, 9999', 0))
print(instructionSyntaxCheck('LDR R0, 999', 0))