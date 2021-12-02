from config import OPERATORS_STRING, OPERATORS, OPERATORS_ASSOCIATIVITY
import math


def lsplit(lst, item):
	try:
		index = lst.index(item)
		return [lst[:index], lst[index+1:]]
	except:
		return [lst, lst]


def isfloat(value: str):
	try:
		float(value)
		return True
	except:
		return False


def decompose(expression, var):
	decomposed = []

	actual_count = 0

	for i, char in enumerate(expression):
		if not i < actual_count:

			if char in OPERATORS_STRING:
				decomposed.append(char)
			elif char.isdigit():
				num = char
				c = 1
				if len(expression)-1 >= i+c:
					while True and len(expression)-1 >= i+c:
						# print(i+c, expression)
						if expression[i+c].isdigit() or expression[i+c] == var:
							num += expression[i+c]
						else:
							break
						c += 1
					actual_count = i + (c - 1)
				decomposed.append(num)
			elif char == var:
				num = char
				c = 1
				if len(expression)-1 >= i+c:
					while True and len(expression)-1 >= i+c:
						# print(i+c, self.left)
						if expression[i+c].isdigit() or expression[i+c] == var:
							num += expression[i+c]
						else:
							break
						c += 1
					actual_count = i + (c - 1)
				decomposed.append(num)

			actual_count += 1

			actual_count += 1
	
	for comp in decomposed:
		if var in comp:
			factors = [char for char in comp]
			for i in range(1, len(factors)):
				factors.insert(i, '*')
			newlistparts = lsplit(decomposed, comp)
			newlist = newlistparts[0] + ['('] + factors + [')'] +  newlistparts[1]
			decomposed = newlist

	return decomposed


def infix_to_postfix(side, var):
	print('Side: ', side)

	
	results = []

	print('e', side)

	print('b', side)

	stack = []
	output = ''

	for i, comp in enumerate(side):
		if comp == '(':
			# print('True')
			toeval = ''
			c = 1
			bracket_count = 1
			while bracket_count > 0:
				print('Side & i+c:', side, i+c)
				
				current_comp = side.pop(i+1)
				
				if current_comp == '(':
					bracket_count += 1
				elif current_comp == ')':
					bracket_count -= 1
				
				if bracket_count > 0:
					print(current_comp)
					toeval += current_comp
				
				
				c += 1
			# if toeval == var:
			# 	return
			print('Eval Info:', side, toeval)
			print('Look here:', infix_to_postfix(decompose(toeval, var), var))
			output.join(infix_to_postfix(decompose(toeval, var), var))
		elif comp == ')':
			if len(stack) == 0:
				continue
			while stack[len(stack)-1] != '(':
				output += stack.pop() + ' '
				if len(stack) == 0:
					print("Mismatching brackets.")
					exit()
			if stack[len(stack)-1] == '(':
				stack.pop()

		elif not comp in list(OPERATORS.keys()):
			output += comp + ' '
		else:
			if len(lsplit(stack, '(')[1]) > 0 and (OPERATORS[stack[len(stack)-1]] > OPERATORS[comp] or (OPERATORS[stack[len(stack)-1]] == OPERATORS[comp] and OPERATORS_ASSOCIATIVITY[comp] == 'left')):
				output += stack.pop() + ' '
			stack.append(comp)

	stack.reverse()

	for comp in stack:
		if comp != '(':
			output += comp + ' '

	results.append(output)

	return results


def eval_postfix(expression: str, var):
	expression = expression.replace(' ', '')

	stack = []

	for comp in expression:
		print('Stack:', stack)
		if comp in OPERATORS.keys():
			var_in = False
			operands = [stack.pop(), stack.pop()]

			for i, operand in enumerate(operands):
				if var in operand:
					# print(operand)
					var_in = True
					if operand == var:
						operands[i] = 1
					else:
						factors = operand.split(var)
						for j, factor in enumerate(factors):
							if not isfloat(factor):
								factors.pop(j)
							else:
								if factor.isdigit():
									factors[j] = int(factor)
								elif isfloat(factor):
									factors[j] = float(factor)

						print('F', factors)
						operands[i] = str(math.prod(factors))

			calc = f"{operands[1]} {comp} {operands[0]}".replace('^', '**')
			print(calc)
			# print(calc)
			res = eval(calc)
			stack.append(str(res) + 'x' if var_in else str(res))
		else:
			stack.append(str(comp))
	# print(stack)
	return stack[0]


# print(eval_postfix("1 2 2 * x * 2 * / 2 4 ^ 4 + 2 / + ", 'x'))

print(decompose("(2*x)^4+4)", 'x'))