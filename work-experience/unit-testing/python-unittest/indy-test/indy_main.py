

class BinaryValue():
	def __init__(self, value: str) -> None:

		self.value = value if value[0] == '0' else f'0{value}'

	def validateBin(self, value: str = None):
		value = value if value is not None else self.value

		return sorted(set(value)) == ['0', '1'] and value[0] == '0'

	def makeBinValid(self, value: str = None):
		value = value if value is not None else self.value

		for i, bit in enumerate(value):
			if bit != 0:
				break

		newValue = value[i:]
		newValue = newValue if newValue[0] == '0' else f'0{newValue}'

		return newValue if self.validateBin(newValue) is True else False

	def add(self, operand: str) -> str:
		op1 = self.value if self.value != '0' else '00'
		op2 = operand if operand != '0' else '00'

		op2 = self.makeBinValid(op2)

		if op2 is False:
			print('Bad binary value given.')
			return 'error: bad operand given'

		maxedLength = max(len(op1), len(op2))

		op1List = ['0' for i in range(
			maxedLength-len(op1))] + [char for char in op1]
		op2List = ['0' for i in range(
			maxedLength-len(op2))] + [char for char in op2]

		op1List.reverse()
		op2List.reverse()

		carrying1 = False
		result = []

		for i, bit in enumerate(op1List):
			digits = [bit, op2List[i], '1' if carrying1 is True else '0']
			carrying1 = False

			count1s = digits.count('1')
			if count1s == 0:
				result.append('0')
			elif count1s == 1:
				result.append('1')
			elif count1s == 2:
				result.append('0')
				carrying1 = True
			elif count1s == 3:
				result.append('1')
				carrying1 = True

		result.reverse()
		newValue = ''.join(result)
		self.value = newValue if newValue[0] == '0' else f'0{newValue}'

		return self.value
