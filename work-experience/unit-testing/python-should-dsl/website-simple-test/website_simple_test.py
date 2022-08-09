
import unittest
from should_dsl import should, should_not


def add(num1, num2):
	return num1 + num2

class WidgetTestCase(unittest.TestCase):

	def testAddition(self):
		add(1, 1) | should | equal_to(2)

	def testAddition2(self):

		unittest.assertEqual()


unittest.main()
