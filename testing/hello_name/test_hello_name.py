import unittest

from hello_name import hello_name

"""
you can call this test file directly by running pytest in the
terminal if it is the only test file in the directory referenced,
also, eliminates the need for using the main function

def test_hello_world(self):
	assert hello_world('matt') == 'hello matt'

"""

class testHello(unittest.TestCase):
	def test_hello_name(self):
		self.assertEqual(hello_name('matt'), 'hello matt')
		self.assertNotEqual(hello_name('matt'), 'hello mat')

if __name__=='__main__':
	unittest.main()