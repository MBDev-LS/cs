from pprint import pprint
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


INSTRUCTION_SET = {
	'HLT': 0,
	'ADD': 1,
	'SUB': 2,
	'STA': 3,
	"STO": 3,
	'LDA': 5,
	'BRA': 6,
	'BRZ': 7,
	'BRP': 8,
	'INP': 9,
	'OTC': 9,
	'DAT': None,
}



line_names = {}

data_info = {
	'variables': {},
	'data_locations': [],
}

with open(BASE_DIR / 'program.txt', 'rt') as f:
	instruction_list = f.read().split('\n')


def raise_exception(exception_type, line_num, instruction):
	print(f'exception: {exception_type} on line {line_num}\n> {instruction}')
	exit()


def proccess_dat(instruction: str, line_num: int, data_info: dict) -> dict:
	if not "DAT" in instruction.upper():
		return data_info

	instruction_components = instruction.split(' ')
	# if not instruction_components[-1].isdigit() and len(instruction_components) != 1:
	# 	raise_exception('syntax', line_num, instruction)
	if len(instruction_components) == 2 and (not instruction_components[0].isdigit() or not instruction_components[1].isdigit()):
		data_info['data_locations'].append(line_num)
	elif len(instruction_components) == 3 and instruction_components[0] not in INSTRUCTION_SET.keys() and instruction_components[1] == 'DAT':
		data_info['variables'][instruction_components[0]] = line_num
		data_info['data_locations'].append(line_num)
	elif len(instruction_components) == 1 and instruction.rstrip() == 'DAT':
		return data_info
	else:
		raise_exception('syntax error', line_num, instruction)

	return data_info


def assign_line_names(instruction: str, line_num: int):
	if not instruction.startswith(tuple(INSTRUCTION_SET.keys())):
		line_names[instruction.split(' ')[0]] = line_num

		return ' '.join(instruction.split(' ')[1:])
	else:
		return instruction


def validate(instruction: str, line_num: int, data_info: dict):
	instruction_components = instruction.split(' ')
	if len(instruction_components) != 2 and 'DAT' not in instruction.upper():
		raise_exception('bad instruction', line_num, instruction)
	elif instruction_components[0].upper() not in INSTRUCTION_SET:
		raise_exception('unknown instruction', line_num, instruction)
	elif not instruction_components[1].isdigit() and instruction_components[1] not in data_info['variables']:
		raise_exception('unknown address label', line_num, instruction)
	else:
		return True


def translate(instruction: str):
	translated_instruction = ''
	instruction_components = instruction.split(' ')
	print(instruction_components)
	
	if 'DAT' in instruction.upper():
		if instruction_components[-1].isdigit():
			return f'0{int(instruction_components[-1]):02d}'
		else:
			return '000'

	translated_instruction += str(
		INSTRUCTION_SET[instruction_components[0].upper()])
	translated_instruction += instruction_components[1] if instruction_components[1].isdigit(
	) else f"{data_info['variables'][instruction_components[1]]:02d}"

	return translated_instruction


new_instruction_list = []

for line_num, instruction in enumerate(instruction_list):
	if 'DAT' in instruction.upper():
		data_info = proccess_dat(instruction, line_num, data_info)

	new_instruction_list.append(assign_line_names(instruction, line_num))

instruction_list = new_instruction_list

translated_program_list = []

for line_num, instruction in enumerate(instruction_list):
	if 'DAT' not in instruction.upper():
		if validate(instruction, line_num, data_info) is True:
			translated_program_list.append(translate(instruction))
	else:
		translated_program_list.append(translate(instruction))


memory = ['000' for i in range(0, 99)]

for i, translated_instruction in enumerate(translated_program_list):
	if i <= 99:
		memory[i] = translated_instruction

buffer_register = ''
program_counter = 0
instruction_resgister = 0
address_register = 0
accumulator = 0

running = True

while running == True:
	buffer_register = memory[program_counter]
	program_counter += 1

	instruction_resgister = int(buffer_register[:1])
	address_register = int(buffer_register[1:])
	print(instruction_resgister)
	running = False
