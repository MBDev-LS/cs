
import random 

class Zoo():
	def __init__(self, animals: list=None) -> None:
		self.animals = animals if animals is not None else []
	
	def killAllTheAnimals(self):
		self.animals = []

		print('You monster.')

	def __str__(self) -> str:
		return f'A zoo with the following animals: {", ".join([str(animal) for animal in self.animals])}'

class ZooAnimal():
	def __init__(self, name: str, age: int, species: str) -> None:
		self.name = name
		self.age = age
		self.species = species
	
	def __str__(self) -> str:
		return f'a {self.species} called {self.name} that is {self.age} years old.'

species = ['dog', 'cat', 'baboon', 'granny', 'bear with very large toes']
names = ['dave', 'roger', 'your mum', 'your dad', 'your gran']

random.shuffle(species)
random.shuffle(names)

animals = []

for name in names:
	animals.append(ZooAnimal(name, random.randint(0, 140), random.choice(species)))


bigFunZooLtd = Zoo(animals)

print(bigFunZooLtd)

del bigFunZooLtd

print(animals)