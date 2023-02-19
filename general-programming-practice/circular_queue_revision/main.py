

class CircularQueue():
	def __init__(self, length: int) -> None:
		self.queueList = [None for i in range(length)]
		self.length = length

		self.front = -1
		self.rear = -1

	def __get_next_front(self) -> int:
		return (self.front + 1) % self.length
	
	def __get_next_rear(self) -> int:
		return (self.rear + 1) % self.length
	
	def is_full(self) -> bool:
		return self.__get_next_rear() == self.front
	
	def is_empty(self) -> bool:
		return self.front == -1 or self.front > self.rear

	def enqueue(self, obj) -> None:
		if self.is_full() is True:
			print(f'Unable to enqueue object ({obj}) as queue ({self}) is full.')

			return
		
		self.rear = self.__get_next_rear()

		self.queueList[self.rear] = obj

	def dequeue(self):
		if self.is_empty() is True:
			print(f'Unable to dequeue from queue, as queue ({self}) is empty.')

			return
		
		dequeuedObj = self.queueList[self.front]
		self.front = self.__get_next_front()

		if self.is_empty():
			self.front = 0
			self.rear = -1

		return dequeuedObj
	
	def __str__(self) -> str:
		return str(self.queueList)
	
	def log(self):
		print(self, {'F': self.front, 'R': self.rear})


cQueue = CircularQueue(4)
print(cQueue)
cQueue.enqueue('One')
cQueue.enqueue('Two')
cQueue.log()
print('Dequeued:', cQueue.dequeue())
cQueue.log()
print('Dequeued:', cQueue.dequeue())
cQueue.log()
print(cQueue.is_empty())
cQueue.enqueue(1)
cQueue.enqueue(2)
cQueue.log()
cQueue.enqueue(3)
cQueue.enqueue(4)
cQueue.log()
cQueue.enqueue(5)
cQueue.log()