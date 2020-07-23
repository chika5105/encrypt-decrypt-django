import unittest
from  caesar_cipher import CaesarCipher

test = CaesarCipher() #instantiate test caesar cipher class
class CaesarCipherEncryptTests(unittest.TestCase):
    def test_empty_string(self):
        self.assertMultiLineEqual(test.encrypt(''), '')

    def test_string_with_only_spaces(self):
        self.assertMultiLineEqual(test.encrypt('     '), '     ')

    def test_string_no_wrap_around_default_key_20(self):
        self.assertMultiLineEqual(test.encrypt('abc'), 'uvw')

    def test_string_wrap_around_default_key_20(self):
        self.assertMultiLineEqual(
            test.encrypt('txyz'),
            'nrst')

    def test_multi_word_default_key_20(self):
        self.assertMultiLineEqual(test.encrypt('abc txyz'), 'uvw nrst')

    def test_custom_key_2(self):
        self.assertMultiLineEqual(test.encrypt('txyz', 2), 'vzab')
    def test_custom_key_greater_than_26(self):
        self.assertMultiLineEqual(test.encrypt('lmao', 200),'desg')

    #for values of key less than 0, JavaScript frontend is tasked with validating 
    #that key must be >= 0. Hence the test is skipped here


class CaesarCipherDecryptTests(unittest.TestCase):
    def test_empty_string(self):
        self.assertMultiLineEqual(test.decrypt(''), '')

    def test_string_with_only_spaces(self):
        self.assertMultiLineEqual(test.decrypt('     '), '     ')

    def test_string_no_wrap_around_default_key_20(self):
        self.assertMultiLineEqual(test.decrypt('uvw'), 'abc')

    def test_string_wrap_around_default_key_20(self):
        self.assertMultiLineEqual(
            test.decrypt('nrst'),
            'txyz')

    def test_multi_word_default_key_20(self):
        self.assertMultiLineEqual(test.decrypt('uvw nrst'), 'abc txyz')

    def test_custom_key_2(self):
        self.assertMultiLineEqual(test.decrypt('vzab', 2), 'txyz')
    def test_custom_key_greater_than_26(self):
        self.assertMultiLineEqual(test.decrypt('desg', 200),'lmao')

if __name__ == '__main__':
    unittest.main()
    unittest.main()
    