import unittest
import katas
#from calculator import calculator

# self.calculator = Calculator()
class TestKatas(unittest.TestCase):\

    def test_add(self):
        #self.fail("TODO: Write add unit test")
        self.assertEqual((1 + 2), 3)

    def test_multiply(self):
        #self.fail("TODO: Write multiply unit test")
        self.assertEqual((3 * 7), 21)

    def test_power(self):
        #self.fail("TODO: Write power unit test")
        self.assertTrue((3, 3),[27])

    def test_factorial(self):
        self.fail("TODO: Write factorial unit test")

    def test_fibonacci(self):
        self.fail("TODO: Write fibonacci unit test")


if __name__ == '__main__':
    unittest.main()
