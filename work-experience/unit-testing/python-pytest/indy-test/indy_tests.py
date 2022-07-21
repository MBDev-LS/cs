
import pytest
from indy_main import *


class BinaryValueAddTests:

	def __init__(self) -> None:
		self.binaryValue = BinaryValue('0')

	def test_normal_add(self):
		"""
		Tests for normal binary
		addition, including both
		carry types.
		"""
		self.binaryValue.value = '0111'

		res = self.binaryValue.add('11101011')
		assert res == '011110010', 'normal addition incorrect'

	def test_edge_case_add(self):
		"""
		Tests the function's ability
		to add two single-bit binary
		numbers.
		"""
		self.binaryValue.value = '0'

		res = self.binaryValue.add('1')
		assert res == '01', 'single digit edge case incorrect'

	def test_edge_case_with_carry_add(self):
		"""
		Tests the function's ability
		to carry correctly when adding
		two single-bit binary numbers.
		"""
		self.binaryValue.value = '1'

		res = self.binaryValue.add('1')
		assert res == '010', 'single digit with carrying edge case incorrect'

	def test_tripple_one_carry_add(self):
		"""
		Tests the function's ability
		to carry correctly when adding
		three 1s.
		"""
		self.binaryValue.value = '11'

		res = self.binaryValue.add('11')
		assert res == '0110', 'double carry edge case incorrect'

	def test_add_error(self):
		"""
		Tests the functions ability
		to return the appropriate
		error when supplied an invalid
		operand.
		"""
		res = self.binaryValue.add('2121')
		assert res == 'error: bad operand given', 'appropriate error not returned when invalid operand supplied'
