import unittest
from  reverse_cipher import ReverseCipher

test = ReverseCipher() #instantiate test caesar cipher class
class ReverseCipherEncryptTests(unittest.TestCase):
    def test_empty_string(self):
        self.assertMultiLineEqual(test.encrypt(''), '')

    def test_string_with_only_spaces(self):
        self.assertMultiLineEqual(test.encrypt('     '), '     ')

    def test_string_alphabets(self):
        self.assertMultiLineEqual(test.encrypt('abc'), 'cba')

    def test_string_alphanum(self):
        self.assertMultiLineEqual(
            test.encrypt('wvu67'),
            '76uvw')

    def test_multi_word(self):
        self.assertMultiLineEqual(test.encrypt('abc tloe'), 'eolt cba')




class ReverseCipherDecryptTests(unittest.TestCase):
    def test_empty_string(self):
        self.assertMultiLineEqual(test.decrypt(''), '')

    def test_string_with_only_spaces(self):
        self.assertMultiLineEqual(test.decrypt('     '), '     ')

    def test_string_no_wrap_around(self):
        self.assertMultiLineEqual(test.decrypt('cba'), 'abc')

    def test_string_wrap_around(self):
        self.assertMultiLineEqual(
            test.decrypt('def'),
            'fed')

    def test_multi_word(self):
        self.assertMultiLineEqual(test.decrypt('zyx def'), 'fed xyz')

if __name__ == '__main__':
    unittest.main()
    unittest.main()
    