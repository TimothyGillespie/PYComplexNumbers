import unittest
from CN import *



class TestCNMethods(unittest.TestCase):
	
	def setUp(self):
		self.a = CN(1, 1)
		self.b = CN(2, 2)
		self.c = CN(10, 4)
		self.d = CN(-10, 25)
		self.e = CN(-10, -25)
		self.f = CN(9, 9)
		self.g = CN(9, -9)
		self.h = CN(0, 0)



	
	def test_getRe(self):
		self.assertEqual(1, self.a.getRe())
		self.assertEqual(2, self.b.getRe())
		self.assertEqual(10, self.c.getRe())
		self.assertEqual(-10, self.d.getRe())
		self.assertEqual(-10, self.e.getRe())
		self.assertEqual(9, self.f.getRe())
		self.assertEqual(9, self.g.getRe())
		self.assertEqual(0, self.h.getRe())
		
	def test_getIm(self):
		self.assertEqual(1, self.a.getIm())
		self.assertEqual(2, self.b.getIm())
		self.assertEqual(4, self.c.getIm())
		self.assertEqual(25, self.d.getIm())
		self.assertEqual(-25, self.e.getIm())
		self.assertEqual(9, self.f.getIm())
		self.assertEqual(-9, self.g.getIm())
		self.assertEqual(0, self.h.getIm())
		

if __name__ == '__main__':
	unittest.main()		
