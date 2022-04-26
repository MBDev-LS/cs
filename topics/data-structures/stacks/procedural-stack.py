
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

print(stack, isFull(size, maxSize), isEmpty(size))

stack, size, top = push(1, stack, maxSize, size, top)
stack, size, top = push(2, stack, maxSize, size, top)

print(stack, isFull(size, maxSize), isEmpty(size))

stack, size, top = push(3, stack, maxSize, size, top)
stack, size, top = push(4, stack, maxSize, size, top)
stack, size, top = push(5, stack, maxSize, size, top)

print(stack, isFull(size, maxSize), isEmpty(size))

poppedItem, size, top =  pop(stack, size, top)

print(poppedItem, stack[:top+1])
