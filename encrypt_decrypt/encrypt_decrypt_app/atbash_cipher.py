
class AtbashCipher:
    def encrypt(self, string):
        lst = []
        for elem in string.lower():
            if elem.isalpha():
                lst+=chr(219-ord(elem))
            else:
                lst+=[elem]
        return ''.join(lst).lower()
    def decrypt(self, string):
        return self.encrypt(string).lower() #same result for encryption 