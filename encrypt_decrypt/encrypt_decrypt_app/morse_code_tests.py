import unittest
from morse_code import MorseCode

test = MorseCode()
class MorseCodeEncryptTests(unittest.TestCase):
    def test_empty_string(self):
        self.assertMultiLineEqual(test.encrypt(''), '')

    def test_string_with_only_spaces(self):
        self.assertMultiLineEqual(test.encrypt('     '), '     ')

    def test_string_lower_case(self):
        self.assertMultiLineEqual(test.encrypt('abc'), '.- -... -.-. ')

    def test_string_upper_case(self):
        self.assertMultiLineEqual(
            test.encrypt('ABC'),
            '.- -... -.-. ')

    def test_multi_word_lower(self):
        self.assertMultiLineEqual(test.encrypt('abc wvu'), '.- -... -.-.  .-- ...- ..- ')

    def test_multi_word_upper(self):
        self.assertMultiLineEqual(test.encrypt('ABC WVU'), '.- -... -.-.  .-- ...- ..- ')

    def test_alphanumeric(self):
        self.assertMultiLineEqual(test.encrypt('ABC 123'), '.- -... -.-.  .---- ..--- ...-- ')



class MorseCodeDecryptTests(unittest.TestCase):
    def test_empty_string(self):
        self.assertMultiLineEqual(test.decrypt(''), ' ')

    def test_string_with_only_spaces(self):
        self.assertMultiLineEqual(test.decrypt('  '), '   ')

    def test_string_lower_case(self):
        self.assertMultiLineEqual(test.decrypt('.- -... -.-. '), 'abc ')

    def test_string_upper_case(self):
        self.assertMultiLineEqual(
            test.decrypt('.- -... -.-. '),
            'abc ')

    def test_multi_word_lower(self):
        self.assertMultiLineEqual(test.decrypt('.- -... -.-.  .-- ...- ..- '), 'abc wvu ')

    def test_multi_word_upper(self):
        self.assertMultiLineEqual(test.decrypt('.- -... -.-.  .-- ...- ..- '), 'abc wvu ')

    def test_alphanumeric(self):
        self.assertMultiLineEqual(test.decrypt('.- -... -.-. .---- ..--- ...-- '), 'abc123 ')


if __name__ == '__main__':
    unittest.main()
    unittest.main()
    