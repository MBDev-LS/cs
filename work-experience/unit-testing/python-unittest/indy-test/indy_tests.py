
import unittest
from indy_main import *

class BinaryValueAddTests(unittest.TestCase):

	@classmethod
	def setUp(self) -> None:
		self.binaryValue = BinaryValue('0')


	def test_normal_add(self):
		"""
		Tests for normal binary
		addition, including both
		carry types.
		"""
		self.binaryValue.value = '0111'

		res = self.binaryValue.add('11101011')
		self.assertEqual(res, '011110010')


	def test_edge_case_add(self):
		"""
		Tests the function's ability
		to add two single-bit binary
		numbers.
		"""
		self.binaryValue.value = '0'

		res = self.binaryValue.add('1')
		self.assertEqual(res, '01')


	def test_edge_case_with_carry_add(self):
		"""
		Tests the function's ability
		to carry correctly when adding
		two single-bit binary numbers.
		"""
		self.binaryValue.value = '1'

		res = self.binaryValue.add('1')
		self.assertEqual(res, '010')


	def test_tripple_one_carry_add(self):
		"""
		Tests the function's ability
		to carry correctly when adding
		three 1s.
		"""
		self.binaryValue.value = '11'

		res = self.binaryValue.add('11')
		self.assertEqual(res, '0110')


	def test_add_error(self):
		"""
		Tests the functions ability
		to return the appropriate
		error when supplied an invalid
		operand.
		"""
		res = self.binaryValue.add('2121')
		self.assertEqual(res, 'error: bad operand given')


calculate_area_suite = unittest.TestLoader() \
	.loadTestsFromTestCase(BinaryValueAddTests)

runner = unittest.TextTestRunner()
runner.run(calculate_area_suite)