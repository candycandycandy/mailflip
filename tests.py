from app import create_app
import unittest

class TestCase(unittest.TestCase):
	def test_truth(self):
		assert 1 == 1

if __name__ == '__main__':
	unittest.main()