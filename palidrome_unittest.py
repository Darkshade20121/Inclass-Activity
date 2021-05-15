import unittest
import palidrome

class palidrome_test(unittest.TestCase):
    def test_palidrome_pass(self):
        result = palidrome.palidrome("racecar")
        self.assertEqual(result,True)

    def test_palidrome_test_pass(self):
        result = palidrome.palidrome("hello")
        self.assertEqual(result,False)

    def test_palidrome_test_fail(self):
        result = palidrome.palidrome("RaceCar")
        self.assertEqual(result,True)
