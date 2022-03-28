
import math

class Queue():
	def __init__(self, queueLength: int=None) -> None:
		self.queue = []
		self.queueLength = queueLength if queueLength is not None else math.inf

	def enQueue(self, itemToEnQueue) -> None:
		if self.isFull() is not True:
			self.queue.append(itemToEnQueue)
		else:
			print(f'Failed to enqueue {itemToEnQueue} as queue ({", ".join(self.queue)}) is full.')
	
	def deQueue(self):
		return self.queue.pop(0)
	
	def isFull(self) -> bool:
		if len(self.queue) == self.queueLength:
			return True
		
		return False
	
	def isEmpty(self) -> bool:
		return True if len(self.queue) == 0 else False

queue = Queue(4)
print(queue.isEmpty())

queue.enQueue('Keir')
queue.enQueue('Boris')
queue.enQueue('Sadiq')
queue.enQueue('Chris')

print(queue.queue)
print(queue.isEmpty())
print(queue.isFull())

print(queue.deQueue())

print(queue.queue)
print(queue.isEmpty())
print(queue.isFull())
