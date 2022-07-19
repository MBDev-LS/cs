
import unittest
from indy_main import *

class BinaryValueAddTests(unittest.TestCase):
	@classmethod
	def setUp(self) -> None:
		self.binaryValue = BinaryValue('0')

	def test_normal_add(self):
		self.binaryValue.value = '0111'

		res = self.binaryValue.add('11101011')
		self.assertEqual(res, '011110010')
	
	def test_edge_case_add(self):
		self.binaryValue.value = '0'

		res = self.binaryValue.add('1')
		self.assertEqual(res, '01')
	
	def test_edge_case_with_carry_add(self):
		self.binaryValue.value = '1'

		res = self.binaryValue.add('1')
		self.assertEqual(res, '010')

	def test_tripple_one_carry_add(self):
		self.binaryValue.value = '11'

		res = self.binaryValue.add('11')
		self.assertEqual(res, '0110')


	def test_add_error(self):
		res = self.binaryValue.add('2121')
		self.assertEqual(res, 'error: bad operand given')


calculate_area_suite = unittest.TestLoader() \
	.loadTestsFromTestCase(BinaryValueAddTests)

runner = unittest.TextTestRunner()
runner.run(calculate_area_suite)