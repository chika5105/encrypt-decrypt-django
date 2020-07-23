class CaesarCipher:
    def __init__(self,key=20):
        self.__key = key
    def encrypt(self, string, key=20):
        lst = []
        for i in string.lower():
            if i.isalpha():
                new_i = chr(((ord(i)-97+key)%26)+ 97)
                lst+=[new_i]
            else:
                lst+=[i]
        return ''.join(lst).lower()
    def decrypt(self, string, key=20):
        lst = []
        for i in string.lower():
            if i.isalpha():
                new_i = chr((ord(i)-97-key)%26 + 97)
                lst+=[new_i]
            else:
                lst+=[i]
        return ''.join(lst).lower()
    

