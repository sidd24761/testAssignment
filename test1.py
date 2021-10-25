# unit test case
import unittest

class TestStringMethods(unittest.TestCase):
	def test_negative(self):
		firstValue = "geeks"
		secondValue = "gfg"
		message = "First value and second value are not equal !"
		self.assertEqual(firstValue, secondValue, message)

if __name__ == '__main__':
	unittest.main()
