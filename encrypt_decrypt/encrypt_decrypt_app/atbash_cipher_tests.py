import unittest
from  atbash_cipher import AtbashCipher

test = AtbashCipher() #instantiate test caesar cipher class
class AtbashCipherEncryptTests(unittest.TestCase):
    def test_empty_string(self):
        self.assertMultiLineEqual(test.encrypt(''), '')

    def test_string_with_only_spaces(self):
        self.assertMultiLineEqual(test.encrypt('     '), '     ')

    def test_string_no_wrap_around(self):
        self.assertMultiLineEqual(test.encrypt('abc'), 'zyx')

    def test_string_wrap_around(self):
        self.assertMultiLineEqual(
            test.encrypt('wvu'),
            'def')

    def test_multi_word(self):
        self.assertMultiLineEqual(test.encrypt('abc wvu'), 'zyx def')


    #for values of key less than 0, JavaScript frontend is tasked with validating 
    #that key must be >= 0. Hence the test is skipped here


class AtbashCipherDecryptTests(unittest.TestCase):
    def test_empty_string(self):
        self.assertMultiLineEqual(test.decrypt(''), '')

    def test_string_with_only_spaces(self):
        self.assertMultiLineEqual(test.decrypt('     '), '     ')

    def test_string_no_wrap_around(self):
        self.assertMultiLineEqual(test.decrypt('zyx'), 'abc')

    def test_string_wrap_around(self):
        self.assertMultiLineEqual(
            test.decrypt('def'),
            'wvu')

    def test_multi_word(self):
        self.assertMultiLineEqual(test.decrypt('zyx def'), 'abc wvu')

if __name__ == '__main__':
    unittest.main()
    unittest.main()
    