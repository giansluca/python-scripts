import unittest
from src.jokes import tell_jokes as under_test


class TellJokesTest(unittest.TestCase):
    def test_make_request_1(self):
        jokes_list = under_test.make_request_1()
        self.assertEqual(len(jokes_list), under_test.number_of_jokes_from_api)

    def test_make_request_2(self):
        jokes_list = under_test.make_request_2()
        self.assertEqual(len(jokes_list), under_test.number_of_jokes_from_api)
