import unittest
import wordcount

class wordcount_test(unittest.TestCase):
    def test_wordcount_pass(self):
        result = wordcount.count("Hello World")
        self.assertEqual(result,2)

    def test_wordcount_2_pass(self):
        result = wordcount.count("Hello my friends. I am Andrew")
        self.assertEqual(result,6)

    def test_wordcount_fail(self):
        result = wordcount.count("Hello,there")
        self.assertEqual(result,2)
