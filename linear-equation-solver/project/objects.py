
import string
from config import OPERATORS_STRING, OPERATORS, OPERATORS_ASSOCIATIVITY

def lsplit(lst, item):
	try:
		index = lst.index(item)
		return [lst[:index], lst[index+1:]]
	except:
		return [lst, lst]

class Equation():
	def __init__(self, equation: str, var: str):

		self.eq = equation
		self.var = var

	def verify(self):
		chars = []
		for c in self.eq:
			if not c.isdigit() and c in string.ascii_lowercase:
				chars.append(c)
		if len(list(set(chars))) > 1:
			print(
				'This program currently only supports equations with one unknown variable')
			return False

		if self.eq.count('=') < 1:
			print("The equation must have one = sign.")
			return False
		elif self.eq.count('=') > 1:
			print("The equation must have only one = sign.")
			return False

		if len(self.eq.split('=')[0]) == 0 or len(self.eq.split('=')[0]) == 0:
			print("The must be at least one character on each side of the '=' sign.")
			return False

		return True

	def decompose(self):
		self.left = self.eq.split('=')[0]
		self.left_decomposed = []
		self.right = self.eq.split('=')[1]
		self.right_decomposed = []

		actual_count = 0

		# Repeated code is a product of early testing, real version will store 'left' and 'right' in a list and iterate through it.
		for i, char in enumerate(self.left):
			if not i < actual_count:

				if char in OPERATORS_STRING:
					self.left_decomposed.append(char)
				elif char.isdigit():
					num = char
					c = 1
					if len(self.left)-1 >= i+c:
						while True and len(self.left)-1 >= i+c:
							# print(i+c, self.left)
							if self.left[i+c].isdigit() or self.left[i+c] == self.var:
								num += self.left[i+c]
							else:
								break
							c += 1
						actual_count = i + (c - 1)
					self.left_decomposed.append(num)
				elif char == self.var:
					num = char
					c = 1
					if len(self.left)-1 >= i+c:
						while True and len(self.left)-1 >= i+c:
							# print(i+c, self.left)
							if self.left[i+c].isdigit() or self.left[i+c] == self.var:
								num += self.left[i+c]
							else:
								break
							c += 1
						actual_count = i + (c - 1)
					self.left_decomposed.append(num)

				actual_count += 1

		actual_count = 0
		for i, char in enumerate(self.right):
			if not i < actual_count:

				if char in OPERATORS_STRING:
					self.right_decomposed.append(char)
				elif char.isdigit():
					num = char
					c = 1
					if len(self.right)-1 >= i+c:
						while True and len(self.right)-1 >= i+c:
							# print(i+c, self.right)
							if self.right[i+c].isdigit() or self.right[i+c] == self.var:
								num += self.right[i+c]
							else:
								break
							c += 1
						actual_count = i + (c - 1)
					self.right_decomposed.append(num)
				elif char == self.var:
					num = char
					c = 1
					if len(self.right)-1 >= i+c:
						print("working")
						while True and len(self.right)-1 >= i+c:
							if self.right[i+c].isdigit() or self.right[i+c] == self.var:
								print("working")
								num += self.right[i+c]
							else:
								break
							c += 1
						actual_count = i + (c - 1)
					self.right_decomposed.append(num)

				actual_count += 1
		
		for comp in self.left_decomposed:
			if self.var in comp:
				factors = [char for char in comp]
				for i in range(1, len(factors)):
					factors.insert(i, '*')
				newlistparts = lsplit(self.left_decomposed, comp)
				newlist = newlistparts[0] + ['('] + factors + [')'] +  newlistparts[1]
				self.left_decomposed = newlist

		for comp in self.right_decomposed:
			if self.var in comp:
				factors = [char for char in comp]
				for i in range(1, len(factors)):
					factors.insert(i, '*')
				newlistparts = lsplit(self.right_decomposed, comp)
				newlist = newlistparts[0] + ['('] + factors + [')'] +  newlistparts[1]
				self.right_decomposed = newlist

		return [self.left_decomposed, self.right_decomposed]

	def __str__(self):
		return self.eq