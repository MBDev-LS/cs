
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

REGEXTYPES = {
	"mGroup": r"\sR(1[0-2]|[0-9]),\s?[0-9]{1,3}", # second bit makes no sense
	"gGroup": r"\sR(1[0-2]|[0-9]),\sR(1[0-2]|[0-9]),\s?(R(1[0-2]|[0-9])|#\d+)",
	"b":      r"\s[a-zA-Z]+",
	"B+" :    r"(ET|GT|NE|LT)\s[a-zA-Z]+",
	"HALT":   r"HALT",
	"labels":r"(\s*[a-zA-Z]+:)*",
}

ERRORINDEXTOERRORWITHLABEL = {
	0: "error: issue with label",
	1: "error: issue with instruction"
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

def printError(line_num: int, errorText: str, lineText: str, arrowText: str):
	print(f"""  error in program, line {line_num}
{errorText}
{lineText}
{arrowText}""")

	exit()

ERRORINDEXTOERROR = {

}

def reportDetailedError(instructionList: str, errorIndex: int, line_num: int, instructionMissing: bool=False):
	baseArrowOffset = 0
	for i in range(errorIndex):
		baseArrowOffset += len(instructionList[i]) + 1
	
	arrowLine = (baseArrowOffset * ' ') + '^'.center(len(instructionList[errorIndex])) if instructionMissing is False else (baseArrowOffset * ' ') + '^'.center(2)
	lineText = ' '.join(instructionList)

	offsetErrorIndex = errorIndex if instructionList[0].upper() in INSTRUCTION_SET else errorIndex - 1

	if instructionList[0].upper() not in INSTRUCTION_SET:
		if errorIndex in ERRORINDEXTOERRORWITHLABEL:
			printError(line_num, ERRORINDEXTOERRORWITHLABEL[errorIndex], lineText, arrowLine)
	
	if 'R' in instructionList[errorIndex].upper():
		printError(line_num, 'error: bad parameter, unknown register referenced', lineText, arrowLine)
	else:
		printError(line_num, 'error: bad parameter', lineText, arrowLine)




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


def steppedSyntaxCheck(instruction: str, line_num: int):
	instruction_type = re.findall(r"\s?([A-Z]{1}|[A-Z]{3,4})\s", instruction)[0].upper().strip()
	if instruction.split(' ')[0].upper() not in INSTRUCTION_SET:
		# instructionRegexList = [REGEXTYPES['labels'], instruction_type] + splitRegex(REGEXTYPES[INSTRUCTION_SET[instruction_type]['regex_group']],',\s?', ',\s', '\s?', '\s') + ['$']
		instructionRegexList = [REGEXTYPES['labels'], instruction_type] + splitRegex(REGEXTYPES[INSTRUCTION_SET[instruction_type]['regex_group']], '\s?', '\s') + ['$']
	else:
		# instructionRegexList = [instruction_type] + splitRegex(REGEXTYPES[INSTRUCTION_SET[instruction_type]['regex_group']],',\s?', ',\s', '\s?', '\s') + ['$']
		instructionRegexList = [instruction_type] + splitRegex(REGEXTYPES[INSTRUCTION_SET[instruction_type]['regex_group']], '\s?', '\s') + ['$']

	instructionList = instruction.split(' ')
	print(instructionList, instructionRegexList)

	for i, regexStr in enumerate(instructionRegexList[:-1]):
		if i >= len(instructionList):
			reportDetailedError(instructionList, i, line_num, True)
		elif re.match(regexStr, instructionList[i]) is None:
			reportDetailedError(instructionList, i, line_num)

		# Now check if instructionList[i] matches the regexStr - should be done



def instructionSyntaxCheck(instruction: str, line_num: int):
	instruction_type = re.findall(r"\s?([A-Z]{1}|[A-Z]{3,4})\s", instruction)

	if len(instruction_type) == 0 or instruction_type[0].strip() not in INSTRUCTION_SET:
		return f"error: unknown instruction \'{instruction_type[0]}\' on line {line_num}"

	instruction_type = instruction_type[0].strip() # Can this not be done betfore first if statement to make this section simplier
	
	

	if INSTRUCTION_SET[instruction_type]['regex_group'] in ['mGroup', 'gGroup']:
		
		
		if re.match('^' + instruction_type + REGEXTYPES[INSTRUCTION_SET[instruction_type]['regex_group']] + '$', instruction) is None:
			steppedSyntaxCheck(instruction, line_num)
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
# print(instructionSyntaxCheck('lab LDR R0, a12', 0))
print(instructionSyntaxCheck('LDR RDAVE, 999', 0))