
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
        return -1, queue, front
    
    deQueuedItem = queue[front]
    
    front = (front + 1) % queueMaxLength
    size -= 1

    return deQueuedItem, queue, front, size

def logQueue(queue: list, front: int, rear: int, size: int, queueMaxLength: int):
    print(f'Queue: {queue}')
    print(f'isEmpty: {isEmpty(size)}')
    print(f'isFull: {isFull(size, queueMaxLength)}')

queue, front, rear, size, queueMaxLength = createQueue(4)

logQueue(queue, front, rear, size, queueMaxLength)

queue, rear, size = enQueue(queue, front, rear, size, queueMaxLength, 'Chris')

logQueue(queue, front, rear, size, queueMaxLength)

queue, rear, size = enQueue(queue, front, rear, size, queueMaxLength, 'Alan')
queue, rear, size = enQueue(queue, front, rear, size, queueMaxLength, 'Peter')
queue, rear, size = enQueue(queue, front, rear, size, queueMaxLength, 'Sylvester')

logQueue(queue, front, rear, size, queueMaxLength)

deQueuedItem, queue, front, size = deQueue(queue, front, rear, size, queueMaxLength)

logQueue(queue, front, rear, size, queueMaxLength)

queue, rear, size = enQueue(queue, front, rear, size, queueMaxLength, 'Douglas')
queue, rear, size = enQueue(queue, front, rear, size, queueMaxLength, 'Donald')

logQueue(queue, front, rear, size, queueMaxLength)
