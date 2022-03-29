
def isEmpty(queue: list) -> bool:
    if len(queue) == 0:
        return True
    
    return False

def enQueue(queue: list, itemToEnQueue) -> tuple:
    queue.append(itemToEnQueue)

    return queue

def deQueue(queue) -> tuple:
    if isEmpty(queue) is True:
        print(f'Failed to dequeue from queue, as queue is empty.')
        return deQueuedItem, queue
    
    deQueuedItem = queue.pop(0)

    return deQueuedItem, queue

queue = []

print(queue)
queue = enQueue(queue, 'Moss')
queue = enQueue(queue, 'Roy')
queue = enQueue(queue, 'Jen')
queue = enQueue(queue, 'Douglas')

print(queue)

deQueuedItem, queue = deQueue(queue)

print(queue)

deQueuedItem, queue = deQueue(queue)
deQueuedItem, queue = deQueue(queue)
deQueuedItem, queue = deQueue(queue)

print(queue)

