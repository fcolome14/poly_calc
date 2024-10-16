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


# if __name__ == "__main__":
#     unittest.main()