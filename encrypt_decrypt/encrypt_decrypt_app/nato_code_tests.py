import unittest
from nato_code import NatoCode

test = NatoCode()
class NatoCodeEncryptTests(unittest.TestCase):
    def test_empty_string(self):
        self.assertMultiLineEqual(test.encrypt(''), '')

    def test_string_with_only_spaces(self):
        self.assertMultiLineEqual(test.encrypt('    '), '    ')

    def test_string_lower_case(self):
        self.assertMultiLineEqual(test.encrypt('abct'), 'alfa bravo charlie tango ')

    def test_string_upper_case(self):
        self.assertMultiLineEqual(
            test.encrypt('ABC'),
            'alfa bravo charlie ')

    def test_multi_word_lower(self):
        self.assertMultiLineEqual(test.encrypt('abc wvu'), 'alfa bravo charlie  whiskey victor uniform ')

    def test_multi_word_upper(self):
        self.assertMultiLineEqual(test.encrypt('ABC WVU'), 'alfa bravo charlie  whiskey victor uniform ')

    def test_alphanumeric(self):
        self.assertMultiLineEqual(test.encrypt('ABC WVU123'), 'alfa bravo charlie  whiskey victor uniform one two three ')



class NatoCodeDecryptTests(unittest.TestCase):
    def test_empty_string(self):
        self.assertMultiLineEqual(test.decrypt(' '), '  ')

    def test_string_with_only_spaces(self):
        self.assertMultiLineEqual(test.decrypt('    '), '     ')

    def test_string_lower_case(self):
        self.assertMultiLineEqual(test.decrypt('alfa bravo charlie tango '), 'abct ')

    def test_string_upper_case(self):
        self.assertMultiLineEqual(
            test.decrypt('alfa bravo charlie ').upper(),
            'ABC ')

    def test_multi_word_lower(self):
        self.assertMultiLineEqual(test.decrypt('alfa bravo charlie  whiskey victor uniform '), 'abc wvu ')

    def test_multi_word_upper(self):
        self.assertMultiLineEqual(test.decrypt('alfa bravo charlie  whiskey victor uniform ').upper(), 'ABC WVU ')

    def test_alphanumeric(self):
        self.assertMultiLineEqual(test.decrypt('alfa bravo charlie  whiskey victor uniform one two three '), 'abc wvu123 ')


if __name__ == '__main__':
    unittest.main()
    unittest.main()
    