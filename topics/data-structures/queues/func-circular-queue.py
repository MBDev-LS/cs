
def createQueue(queue: list) -> tuple:
    front = 0
    rear = -1
    queueMaxLength = len(queue)
    
    return front, rear, queueMaxLength

def isFull(front: int, rear: int, queueMaxLength: int) -> bool:
    size = rear - front + 1
    if queueMaxLength == size:
        return True
    
    return False

def isEmpty(front: int, rear: int) -> bool:
    size = rear - front
    if size <= 0:
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
        return
    
    deQueuedItem = queue.pop(front)
    front += 1

    return deQueuedItem, queue, front
