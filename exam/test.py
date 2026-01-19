import unittest
from main import square_root

class TestSquareRoot(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(square_root(9), 3)
        self.assertEqual(square_root(0), 0)
        self.assertAlmostEqual(square_root(2), 2 ** 0.5)
        
    def test_negative(self):
        with self.assertRaises(ValueError):
            square_root(-4)
            
if __name__ == '__main__':
    unittest.main()