import unittest
from fizz_buzz.fizz_buzz import checar


class FizzBuzzTest(unittest.TestCase):

	def test_imprime_um(self):
		self.assertEqual("1", checar())