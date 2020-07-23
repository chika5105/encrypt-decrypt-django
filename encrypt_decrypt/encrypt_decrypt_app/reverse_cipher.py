class ReverseCipher:
    def encrypt(self, string):
       return string[::-1].lower()
    def decrypt(self, string):
        return self.encrypt(string) #same result for encryption 