import unittest
from  vigenere_cipher import VigenereCipher

test = VigenereCipher() #instantiate test caesar cipher class
class VigenereCipherEncryptTests(unittest.TestCase):
    def test_empty_string(self):
        self.assertMultiLineEqual(test.encrypt(''), '')

    def test_string_with_only_spaces(self):
        self.assertMultiLineEqual(test.encrypt('     '), '')

    def test_string_no_wrap_around_default_key(self):
        self.assertMultiLineEqual(test.encrypt('abc'), 'zab')

    def test_string_wrap_around_custom_key(self):
        self.assertMultiLineEqual(
            test.encrypt('txyzi', 'chika'),
            'vegji')

    def test_multi_word_default_key(self):
        self.assertMultiLineEqual(test.encrypt('abc txyz'), 'zab swxy')

    def test_multi_word_custom_key(self):
        self.assertMultiLineEqual(test.encrypt('abc txyz', 'jul enjlij'), 'jvn xkhk')

    #for values of key less than 0, JavaScript frontend is tasked with validating 
    #that key must be >= 0. Hence the test is skipped here


class VigenereCipherDecryptTests(unittest.TestCase):
    def test_empty_string(self):
        self.assertMultiLineEqual(test.decrypt(''), '')

    def test_string_with_only_spaces(self):
        self.assertMultiLineEqual(test.decrypt('     '), '     ')

    def test_string_no_wrap_around_default_key(self):
        self.assertMultiLineEqual(test.decrypt('zab'), 'abc')

    def test_string_wrap_around_custom_key(self):
        self.assertMultiLineEqual(
            test.decrypt('vegji', 'chika'),
            'txyzi')

    def test_multi_word_default_key(self):
        self.assertMultiLineEqual(test.decrypt('zab swxy'), 'abc txyz')

    def test_multi_word_custom_key(self):
        self.assertMultiLineEqual(test.decrypt('jvn xkhk', 'jul enjlij'), 'abc txyz')

if __name__ == '__main__':
    unittest.main()
    unittest.main()
    