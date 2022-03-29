
import math

def createQueue(queueLength: int) -> tuple:
	queue = [None for i in range(queueLength)]
	front = 0
	rear = -1
	size = 0
	queueMaxLength = len(queue)
	
	return queue, front, rear, size, queueMaxLength

def isFull(size: int, queueMaxLength: int) -> bool:
	if size == queueMaxLength:
		return True
	
	return False

def isEmpty(size: int) -> bool:
	if size <= 0:
		return True
	
	return False

def enQueue(queue: list, front: int, rear: int, size: int, queueMaxLength: int, itemToEnQueue) -> tuple:
	if isFull(size, queueMaxLength) is True:
		print(f'Failed to enqueue {itemToEnQueue} as queue ({", ".join(queue)}) is full.')
		return queue, rear, size
	
	rear = (rear + 1) % queueMaxLength
	queue[rear] = itemToEnQueue
	size += 1

	return queue, rear, size

def deQueue(queue: list, front: int, rear: int, size: int, queueMaxLength: int) -> tuple:
	if isEmpty(size) is True:
		print(f'Failed to dequeue from queue, as queue is empty.')
		return -1, queue, front, size
	
	deQueuedItem = queue[front]
	
	front = (front + 1) % queueMaxLength
	size -= 1

	return deQueuedItem, queue, front, size

def renderQueue(queue, front, rear):
	resString = '\n' + '\n'.join([f'{i}  {"f" if front == i else " "} {"r" if rear == i else " "} {item}' for i, item in enumerate(queue)]) + '\n'

	return resString


def logQueue(queue: list, front: int, rear: int, size: int, queueMaxLength: int):
	print()
	if isEmpty(size) is True:
		print(f'Queue: ()')
	elif rear - front >= 0:
		print(f'Queue: ({", ".join(queue[front:rear+1])})')
	else:
		print(f'Queue: {", ".join(queue[:rear+1] + queue[front:])}')
		

	print(renderQueue(queue, front, rear))
	
	print(f'isEmpty: {isEmpty(size)}')
	print(f'isFull: {isFull(size, queueMaxLength)}')
	print()

def getIntInput(prompt: str) -> int:
	intInput = input(prompt)
	while intInput.isdigit() is not True:
		print('Please enter an integer.')
		intInput = input(prompt)
	
	return int(intInput)

def menuGen(optionsList):
	outputString = '\nPick an option:\n'
	outputString += '\n'.join([f'{i+1}. {option}' for i, option in enumerate(optionsList)])
	outputString += '\nEnter: '
	
	while True:
		inputRes = getIntInput(outputString)
		if int(inputRes) > 1 or int(inputRes) < len(optionsList):
			break
		print(f'Please enter a number from 1 to {len(optionsList)}')
	
	return int(inputRes) - 1


queueUserSetSize = getIntInput('Enter queue size: ')
while queueUserSetSize <= 0:
	print('Enter an integer greater than 0.')
	queueUserSetSize = getIntInput('Enter queue size: ')

queue, front, rear, size, queueMaxLength = createQueue(queueUserSetSize)

actionsList = ['enQueue', 'deQueue', 'check if queue is full', 'check if queue is empty', 'log queue', 'exit']
while True:
	nextAction = menuGen(actionsList)
	if nextAction == 0:
		stringToEnqueue = input('Enter string to enqueue: ')
		queue, rear, size = enQueue(queue, front, rear, size, queueMaxLength, stringToEnqueue)
		logQueue(queue, front, rear, size, queueMaxLength)
	elif nextAction == 1:
		deQueuedItem, queue, front, size = deQueue(queue, front, rear, size, queueMaxLength)
		print(f'deQueued Item: {deQueuedItem}')
		logQueue(queue, front, rear, size, queueMaxLength)
	elif nextAction == 2:
		print(f'Queue full: {isFull(size, queueMaxLength)}')
	elif nextAction == 3:
		print(f'Queue empty: {isEmpty(size)}')
	elif nextAction == 4:
		logQueue(queue, front, rear, size, queueMaxLength)
	elif nextAction == 5:
		logQueue(queue, front, rear, size, queueMaxLength)
		print('\nPress enter to complete shutdown.')
		input()
		exit()
