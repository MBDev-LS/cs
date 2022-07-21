
import unittest

from gi_main import *

class TestGetAreaRectangle(unittest.TestCase):
	def runTest(self):
		rectangle = Rectangle(2, 3)
		self.assertEqual(rectangle.get_area(), 6, "incorrect area")

unittest.main()
