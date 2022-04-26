
size = 0
top = -1
maxSize = 5

stack = [None for i in range(5)]

def push(item, stack, maxSize, size, top):
	if size == maxSize:
		print(f'Unable to push item \'{item}\' as stack is full')
		return stack, size, top
	
	top += 1
	size += 1
	stack[top] = item
	
	return stack, size, top

def pop(stack, size, top):
	if size == 0:
		print(f'Unable to pop item from stack as stack is empty')
		return None, size, top
	
	poppedItem = stack[top]
	size -= 1
	top -= 1

	return poppedItem, size, top

def peak(stack, size, top):
	if size == 0:
		print('Unable to peak, stack is empty.')
	
	return stack[top]

def isFull(size, maxSize):
	return size == maxSize

def isEmpty(size):
	return size == 0

def stackLog(stack, size, maxSize, top):

	outputStr = ''
	outputStr += 'STACK LOG'
	outputStr = outputStr.center(50)
	outputStr += f'\n{"Index":>15}{"Top Pointer":>15}{"Value":>15}\n'
	for i in range(maxSize):
		if i > top:
			outputStr += f'{i:>15}{"h" if top == i else " ":>15}{"":>15}\n'
		else:
			outputStr += f'{i:>15}{"h" if top == i else " ":>15}{stack[i]:>15}\n'
	
	print()
	print(outputStr)
	print(f'StackFull: {isFull(size, maxSize)}')
	print(f'StackEmpty: {isEmpty(size)}\n')


stackLog(stack, size, maxSize, top)

stack, size, top = push(1, stack, maxSize, size, top)
stack, size, top = push(2, stack, maxSize, size, top)

stackLog(stack, size, maxSize, top)

stack, size, top = push(3, stack, maxSize, size, top)
stack, size, top = push(4, stack, maxSize, size, top)
stack, size, top = push(5, stack, maxSize, size, top)

stackLog(stack, size, maxSize, top)

poppedItem, size, top =  pop(stack, size, top)

print(poppedItem, stack[:top+1])
