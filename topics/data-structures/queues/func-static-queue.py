
def createQueue(queueLength: int) -> tuple:
    queue = [None for i in range(queueLength)]
    front = 0
    rear = -1
    queueMaxLength = len(queue)
    
    return queue, front, rear, queueMaxLength

def isFull(front: int, rear: int, queueMaxLength: int) -> bool:
    size = rear - front + 1
    if size >= queueMaxLength:
        return True
    
    return False

def isEmpty(front: int, rear: int) -> bool:
    size = rear - front
    if size < 0:
        return True
    
    return False

def enQueue(queue: list, front: int, rear: int, queueMaxLength: int, itemToEnQueue) -> tuple:
    if isFull(front, rear, queueMaxLength) is True:
        print(f'Failed to enqueue {itemToEnQueue} as queue ({", ".join(queue)}) is full.')
        return
    
    rear += 1
    queue[rear] = itemToEnQueue

    return queue, rear

def deQueue(queue: list, front: int, rear: int, queueMaxLength: int) -> tuple:
    if isEmpty(front, rear) is True:
        print(f'Failed to dequeue from queue, as queue is empty.')
        return -1, queue, front
    
    deQueuedItem = queue[front]
    queue[front] = None
    
    front += 1

    return deQueuedItem, queue, front



queue, front, rear, queueMaxLength = createQueue(4)

print(queue)
print(isEmpty(front, rear))
print(isFull(front, rear, queueMaxLength))

queue, rear = enQueue(queue, front, rear, queueMaxLength, 'Moss')
queue, rear = enQueue(queue, front, rear, queueMaxLength, 'Roy')
queue, rear = enQueue(queue, front, rear, queueMaxLength, 'Jen')
queue, rear = enQueue(queue, front, rear, queueMaxLength, 'Douglas')

print(queue)
print(isEmpty(front, rear))
print(isFull(front, rear, queueMaxLength))

deQueuedItem, queue, front = deQueue(queue, front, rear, queueMaxLength)
deQueuedItem, queue, front = deQueue(queue, front, rear, queueMaxLength)
deQueuedItem, queue, front = deQueue(queue, front, rear, queueMaxLength)
deQueuedItem, queue, front = deQueue(queue, front, rear, queueMaxLength)

print(queue)
print(isEmpty(front, rear))
print(isFull(front, rear, queueMaxLength))