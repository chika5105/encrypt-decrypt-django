class VigenereCipher():
    def __init__(self):
        self.__dic = {chr(x): x-97 for x in range(97, 123)}
    def encrypt(self, string, key=None):
        if key is None:
            key = ''.join(['z' for elem in string])
        else:
          #TODO validate that key len == message len in forms.py
            key = key.lower()
        string = string.lower()
        result = []
        if len(string.strip()) == 0:
            return ''
        else:
            for i in range(len(string)):
                if string[i] in self.__dic:
                    new_index = (self.__dic[key[i]] + self.__dic[string[i]])%26
                    result += [chr(new_index+ 97)]
                else:
                    result+=[string[i]]
            return ''.join(result).lower()
    def decrypt(self, string, key=None):
        result = []
        if len(string) == 0:
            return ''
        else:
            if key is None:
                key = ''.join(['z']*len(string))
            else:
                key = key.lower()
            string = string.lower()
            for i in range(len(string)):
                if string[i] in self.__dic:
                    new_index = (self.__dic[string[i]] - self.__dic[key[i]])%26
                    result += [chr(new_index+ 97)]
                else:
                    result+=[string[i]]
            return ''.join(result).lower()

