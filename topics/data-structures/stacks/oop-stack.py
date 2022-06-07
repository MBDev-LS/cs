
import enum
import math

from regex import D

class Stack():
	def __init__(self, max_size: int=None) -> None:
		self.stack = []
		self.max_size = max_size if max_size != None else math.inf
	
	def push(self, item) -> None:
		if self.is_full() is True:
			print('Failed to push, stack full.')
			return -1
		
		self.stack.append(item)
	
	def pop(self):
		if self.is_empty() is True:
			print('Failed to pop, stack empty.')
			return -1

		return self.stack.pop()
	
	def peek(self):
		if self.is_empty() is True:
			print('Failed to peek, stack empty.')
			return -1
		
		return self.stack[-1]

	def is_empty(self):
		return True if len(self.stack) == 0 else False
	
	def is_full(self):
		return True if len(self.stack) == self.max_size else False
	
	def log(self):
		commaIndexes = [0]
		commaIndexes += [i for i, char in enumerate(str(self.stack)) if char == ',']
		commaIndexes.append(len(str(self.stack))-1)

		outputStr = ' '*len(str(self.stack))
		midPoints = []
		for i in range(len(commaIndexes)-1):
			midPoints.append(int((commaIndexes[i] + commaIndexes[i+1]) / 2))
		
		outputStr = outputStr[:midPoints[-1]] + 'h' + outputStr[midPoints[-1]:]

		print(str(self.stack))
		print(outputStr)


stack = Stack()

stack.push('Toast')
print(stack.peek(), stack.stack)

stack.push('Fandango')
stack.push('Ray Purchase')


stack.log()

# print(stack.stack)
# print(stack.pop())
# print(stack.stack)
