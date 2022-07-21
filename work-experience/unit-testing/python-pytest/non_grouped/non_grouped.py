
# Our code to be tested
class Rectangle:
	def __init__(self, width, height):
		self.width = width
		self.height = height

	def get_area(self):
		return self.width * self.height

	def set_width(self, width):
		self.width = width

	def set_height(self, height):
		self.height = height

# The test function to be executed by PyTest


def test_normal_case():
	rectangle = Rectangle(2, 3)
	assert rectangle.get_area() == 6, "incorrect area"
