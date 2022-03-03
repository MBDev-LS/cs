
class Exprs():
	pass


class Operators(Exprs):
	def __init__(self, l, r):
		self.l = l
		self.r = r

	def __str__(self):
		return f'{self.l} {self.symb} {self.r}'


class Minus(Operators):
	def __init__(self):
		super().__init__()
		self.symb = '-'


class Plus(Operators):
	def __init__(self):
		super().__init__()
		self.symb = '+'


class Times(Operators):
	def __init__(self):
		super().__init__()
		self.symb = '*'


class Divide(Operators):
	def __init__(self):
		super().__init__()
		self.symb = '/'

class Const(Exprs):
	def __init__(self, value):
		self.value = value
	
	def __str__(self):
		return str(self.value)


class Var(Exprs):
	def __init__(self, name):
		self.name = name
	
	def __str__(self):
		return str(self.name)


e0 = Times(Const(5), Const(4))
e1 = Times(Const(5), Plus(Const(4), Var('x')))


print(e1)


