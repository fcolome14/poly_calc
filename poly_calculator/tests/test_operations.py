""" python -m unittest .\tests\test_operations.py """

import unittest
import opeartions

class TestOperations(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(opeartions.add(10, 5), 15) #Check if the assert is true or false
        self.assertEqual(opeartions.add(-10, 5), -5)
        self.assertEqual(opeartions.add(10, -5), 5)
        self.assertEqual(opeartions.add(-10, -5), -15)
        self.assertEqual(opeartions.add(1, -1), 0)
    
    def test_sub(self):
        self.assertEqual(opeartions.sub(10, 5), 5)
        self.assertEqual(opeartions.sub(-10, 5), -15)
        self.assertEqual(opeartions.sub(10, -5), 15)
        self.assertEqual(opeartions.sub(-10, -5), -5)
        self.assertEqual(opeartions.sub(1, -1), 2)
    
    def test_mult(self):
        self.assertEqual(opeartions.mult(10, 5), 50)
        self.assertEqual(opeartions.mult(-10, 5), -50)
        self.assertEqual(opeartions.mult(10, -5), -50)
        self.assertEqual(opeartions.mult(-10, -5), 50)
        self.assertEqual(opeartions.mult(1, -1), -1)
    
    def test_div(self):
        self.assertEqual(opeartions.div(10, 5), 2)
        self.assertEqual(opeartions.div(-10, 5), -2)
        self.assertEqual(opeartions.div(10, -5), -2)
        self.assertEqual(opeartions.div(-10, -5), 2)
        self.assertEqual(opeartions.div(1, -1), -1)
        self.assertRaises(ZeroDivisionError, opeartions.div, 1, 0)
    
    def test_exp(self):
        self.assertEqual(opeartions.exp(2, 2), 4)
        self.assertEqual(opeartions.exp(-2, 2), 4)
        self.assertEqual(opeartions.exp(2, -1), 0.5)

# if __name__ == "__main__":
#     unittest.main()