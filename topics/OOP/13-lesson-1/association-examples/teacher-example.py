
import random 

class Department():
	def __init__(self, teachers: list=None) -> None:
		self.teachers = teachers if teachers is not None else []

	def __str__(self) -> str:
		return f'A department with the following teachers: {", ".join([str(teacher) for teacher in self.teachers])}'

class Teacher():
	def __init__(self, name: str) -> None:
		self.name = name
	
	def __str__(self) -> str:
		return f'teacher called {self.name}'


names = ['Dr. Dave', 'Mr. Roger', 'Dr. James', 'Mrs Montague of North London', 'Ms Landline']

random.shuffle(names)

teachers = []

for name in names:
	teachers.append(Teacher(name))


aSchoolThatRequiresImprovement = Department(teachers)

print(aSchoolThatRequiresImprovement)

del aSchoolThatRequiresImprovement

print('\n' + ', '.join([str(teacher) for teacher in teachers]))
