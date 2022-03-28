
def Queue():
	def __init__(self):
		self.queue = []

	def enQueue(self, itemToEnQueue) -> None:
		self.queue.append(itemToEnQueue)
	
	def deQueue(self, itemToEnQueue):
		return self.queue.pop(0)
	
	def isFull(self) -> bool:
		return False
	
	def isEmpty(self) -> bool:
		return True if len(self.queue) == 0 else False


