
import pytest
from indy_main import *
import sys

class TestBinaryValueAdd:
	@pytest.fixture
	def _binaryValue(self) -> None:
		return BinaryValue('0')

	def test_normal_add(self, _binaryValue):
		"""
		Tests for normal binary
		addition, including both
		carry types.
		"""
		_binaryValue.value = '0111'

		res = _binaryValue.add('11101011')
		assert res == '011110010', 'normal addition incorrect'

	def test_edge_case_add(self, _binaryValue):
		"""
		Tests the function's ability
		to add two single-bit binary
		numbers.
		"""
		_binaryValue.value = '0'

		res = _binaryValue.add('1')
		assert res == '01', 'single digit edge case incorrect'

	def test_edge_case_with_carry_add(self, _binaryValue):
		"""
		Tests the function's ability
		to carry correctly when adding
		two single-bit binary numbers.
		"""
		_binaryValue.value = '1'

		res = _binaryValue.add('1')
		assert res == '010', 'single digit with carrying edge case incorrect'

	def test_tripple_one_carry_add(self, _binaryValue):
		"""
		Tests the function's ability
		to carry correctly when adding
		three 1s.
		"""
		_binaryValue.value = '11'

		res = _binaryValue.add('11')
		assert res == '0110', 'double carry edge case incorrect'

	def test_add_error(self, _binaryValue):
		"""
		Tests the functions ability
		to return the appropriate
		error when supplied an invalid
		operand.
		"""
		res = _binaryValue.add('2121')
		assert res + '.' == 'error: bad operand given', 'appropriate error not returned when invalid operand supplied'
