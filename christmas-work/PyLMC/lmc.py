from pprint import pprint
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


INSTRUCTION_SET = {
	'HLT': {'code': '000', 'hardcoded': True},
	'ADD': {'code': 1, 'hardcoded': False},
	'SUB': {'code': 2, 'hardcoded': False},
	'STA': {'code': 3, 'hardcoded': False},
	"STO": {'code': 3, 'hardcoded': False},
	'LDA': {'code': 5, 'hardcoded': False},
	'BRA': {'code': 6, 'hardcoded': False},
	'BRZ': {'code': 7, 'hardcoded': False},
	'BRP': {'code': 8, 'hardcoded': False},
	'INP': {'code': '901', 'hardcoded': True},
	'OUT': {'code': '902', 'hardcoded': True},
	'OTC': {'code': 9, 'hardcoded': True},
	'DAT': {'code': None, 'hardcoded': True},
}



line_names = {}

data_info = {
	'address_variables': {},
	'data_locations': [],
}

with open(BASE_DIR / 'program.txt', 'rt') as f:
	instruction_list = f.read().split('\n')


def raise_exception(exception_type, line_num, instruction):
	print(f'exception: {exception_type} on line {line_num}\n> {instruction}')
	exit()

def get_component_list(instruction: str) -> list:
	instruction_components = instruction.split(' ')

	while '' in instruction_components:
		instruction_components.remove('')
	
	return instruction_components

def proccess_dat(instruction: str, line_num: int, data_info: dict) -> dict:
	if not "DAT" in instruction.upper():
		return data_info

	instruction_components = get_component_list(instruction.replace('	', ' '))

	if len(instruction_components) == 2 and (not instruction_components[0].isdigit() or not instruction_components[1].isdigit()):
		if instruction_components[0] not in INSTRUCTION_SET:
			data_info['data_locations'].append(line_num)
			data_info['address_variables'][instruction_components[0]] = line_num
	elif len(instruction_components) == 3 and instruction_components[0] not in INSTRUCTION_SET and instruction_components[1].upper() == 'DAT':
		data_info['address_variables'][instruction_components[0]] = line_num
		data_info['data_locations'].append(line_num)
	elif len(instruction_components) == 1 and instruction.rstrip() == 'DAT':
		return data_info
	else:
		raise_exception('syntax error', line_num, instruction)

	return data_info


def assign_line_names(instruction: str, line_num: int, data_info: dict) -> tuple:
	print(instruction.upper(), tuple(INSTRUCTION_SET))
	print(instruction, not instruction.upper().startswith(tuple(INSTRUCTION_SET)))
	if not instruction.upper().startswith(tuple(INSTRUCTION_SET.keys())):
		print(instruction)
		data_info['address_variables'][instruction.split(' ')[0]] = line_num

		print(' '.join(instruction.split(' ')[1:]))
		return ' '.join(instruction.split(' ')[1:]), data_info
	else:
		return instruction, data_info


def validate(instruction: str, line_num: int, data_info: dict):
	instruction_components = get_component_list(instruction)

	if instruction_components[0].upper() not in INSTRUCTION_SET:
		raise_exception('unknown instruction', line_num, instruction)
	elif len(instruction_components) != 2 and not INSTRUCTION_SET[instruction_components[0].upper()]['hardcoded']:
		raise_exception('bad instruction', line_num, instruction)
	
	if len(instruction_components) == 2:
		if not instruction_components[1].isdigit() and instruction_components[1] not in data_info['address_variables'] and ():
			raise_exception('unknown address label', line_num, instruction)
	return True


def translate(instruction: str):
	translated_instruction = ''
	instruction_components = get_component_list(instruction)

	if not INSTRUCTION_SET[instruction_components[0].upper()]['hardcoded']:
		translated_instruction += str(
			INSTRUCTION_SET[instruction_components[0].upper()]['code'])
		translated_instruction += instruction_components[1] if instruction_components[1].isdigit() else f"{data_info['address_variables'][instruction_components[1]]:02d}"

		return translated_instruction
	
	if 'DAT' in instruction.upper():
		if instruction_components[-1].isdigit():
			return f'0{int(instruction_components[-1]):02d}'
		else:
			return '000'
	
	return INSTRUCTION_SET[instruction.upper().replace(' ', '').replace('	', '')]['code']

def print_instruction(line_num, instruction):
	if len(instruction.strip().split()) == 2:
		if not instruction.strip().split()[1].isdigit():
			print(f'[{line_num:02d}] {instruction.strip().split()[0].upper()} {data_info["address_variables"][instruction.strip().split()[1]]:02d}')
		else:
			print(f'[{line_num:02d}] {instruction.strip().split()[0].upper()} {int(instruction.strip().split()[1]):02d}')
	else:
		if 'DAT' in instruction.upper():
			print(f'[{line_num:02d}] {instruction.strip().split()[0].upper()} 00')
		else:
			print(f'[{line_num:02d}] {instruction.strip().split()[0].upper()}')




new_instruction_list = []

for line_num, instruction in enumerate(instruction_list):
	if 'DAT' in instruction.upper():
		data_info = proccess_dat(instruction, line_num, data_info)

	new_instruction, data_info = assign_line_names(instruction, line_num, data_info)

	new_instruction_list.append(new_instruction)



instruction_list = new_instruction_list

translated_program_list = []


for line_num, instruction in enumerate(instruction_list):
	if 'DAT' not in instruction.upper():
		if validate(instruction, line_num, data_info) is True:
			translated_program_list.append(translate(instruction))
	else:
		translated_program_list.append(translate(instruction))
	
	print_instruction(line_num, instruction)


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

# while running == True:
# 	buffer_register = memory[program_counter]
# 	program_counter += 1

# 	instruction_resgister = int(buffer_register[:1])
# 	address_register = int(buffer_register[1:])
# 	print(instruction_resgister)
# 	running = False

print(memory)