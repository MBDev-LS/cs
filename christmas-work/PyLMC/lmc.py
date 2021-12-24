from pprint import pprint
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

class Lmc:
	def __init__(self, memory: list) -> None:
		self.memory = memory

		self.program_counter = 0
		self.buffer_register = 0
		self.instruction_register = 0
		self.address_register = 0
		self.accumulator = 0

		self.instruction_set = {
			0: self.HLT,
			1: self.ADD,
			2: self.SUB,
			3: self.STA,
			# Need to add an error for 4
			5: self.LDA,
			6: self.BRA,
			7: self.BRZ,
			8: self.BRP,
			9: self.INP_and_OUT_and_OTC,
		}

		self.instruction_set_text = {
			0: 'HLT',
			1: 'ADD',
			2: 'SUB',
			3: 'STA',
			5: 'LDA',
			6: 'BRA',
			7: 'BRZ',
			8: 'BRP',
			9: 'INP_and_OUT_and_OTC',
		}

		self.out_log = []
	
	def log(self, log_type, log_message, exit_program=False) -> None:
		print(f'[{log_type}] {log_message}')
		if exit_program is True:
			exit()

	def HLT(self) -> None:
		print('[HLT] Halting LMC.')
		print('[OUT LOG] ' + ' '.join(str(out_object) for out_object in self.out_log))
		exit()
	
	def ADD(self) -> None:
		self.accumulator = self.accumulator + int(self.memory[self.address_register])
	
	def SUB(self) -> None:
		self.accumulator = self.accumulator - int(self.memory[self.address_register])
	
	def STA(self) -> None:
		self.memory[self.address_register] = f'{self.accumulator:03d}'
	
	def LDA(self) -> None:
		self.accumulator = int(self.memory[self.address_register])

	def BRA(self) -> None:
		self.program_counter = self.address_register
	
	def BRZ(self) -> None:
		if self.accumulator == 0:
			self.program_counter = self.address_register
	
	def BRP(self) -> None:
		if self.accumulator >= 0:
			self.program_counter = self.address_register
	
	def INP_and_OUT_and_OTC(self):
		if self.address_register == 1:
			self.INP()
		elif self.address_register == 2:
			self.OUT()
		elif self.address_register == 22:
			self.OTC()

	def INP(self) -> int:
		user_input = input('[INP] Enter a numerical input: ')
		while not user_input.isdigit():
			print('[INP] Invalid input.')
			user_input = input('[INP] Enter a numerical input: ')
		
		self.accumulator = int(user_input)
	
	def OUT(self) -> None:
		self.out_log.append(self.accumulator)
		print(f'[OUT] {self.accumulator}')
	
	def OTC(self) -> None:
		self.out_log.append(chr(self.accumulator))
		print(f'[OTC] {chr(self.accumulator)}')
	
	def run_cycle(self) -> None:
		self.buffer_register = memory[self.program_counter]
		self.log('BUFFER', f"Setting buffer register to '{self.buffer_register}'")

		self.program_counter += 1
		self.log('PROGRAM COUNTER', f"Incrementing program counter by one, now: '{self.program_counter}'")

		self.instruction_register = int(self.buffer_register[:1])
		self.log('INSTRUCTION REGISTER', f"Setting instruction register to '{self.instruction_register}'")

		self.address_register = int(self.buffer_register[1:])
		self.log('ADDRESS REGISTER', f"Setting address register to '{self.address_register}'")

		print(f'[INSTRUCTION] Now running {self.instruction_set_text[self.instruction_register]} {self.address_register}')
		self.instruction_set[self.instruction_register]()
		print(f'PC: {self.program_counter}, Acc: {self.accumulator}, IR: {self.instruction_register}, MAR: {self.address_register}')
		print(self.memory)

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
	'OTC': {'code': '922', 'hardcoded': True},
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

def remove_comments(intruction: str) -> str:
	comment_splitted_instruction = intruction.split('//')
	if len(comment_splitted_instruction) == 1:
		return intruction
	else:
		if comment_splitted_instruction[0].strip() == '':
			return ''
		return ''.join(comment_splitted_instruction[:1])

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
	if not instruction.upper().split()[0] in INSTRUCTION_SET:
		data_info['address_variables'][instruction.split(' ')[0]] = line_num

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
			if len(instruction_components[-1]) == 3:
				return f'{int(instruction_components[-1]):03d}'
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

for i, instruction in enumerate(instruction_list):
	instruction_list[i] = remove_comments(instruction)

while '' in instruction_list:
	instruction_list.remove('')
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


memory = ['000' for i in range(0, 100)]

for i, translated_instruction in enumerate(translated_program_list):
	if i <= 99:
		memory[i] = translated_instruction

print('\n--------------------------------\n')

lmc = Lmc(memory)

while True:
	lmc.run_cycle()
	# input()