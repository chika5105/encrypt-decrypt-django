class MorseCode():
    def __init__(self):
        self.__dic_plain = { 'A':'.-', 'B':'-...', 
            'C':'-.-.', 'D':'-..', 'E':'.', 
            'F':'..-.', 'G':'--.', 'H':'....', 
            'I':'..', 'J':'.---', 'K':'-.-', 
            'L':'.-..', 'M':'--', 'N':'-.', 
            'O':'---', 'P':'.--.', 'Q':'--.-', 
            'R':'.-.', 'S':'...', 'T':'-', 
            'U':'..-', 'V':'...-', 'W':'.--', 
            'X':'-..-', 'Y':'-.--', 'Z':'--..', 
            '1':'.----', '2':'..---', '3':'...--', 
            '4':'....-', '5':'.....', '6':'-....', 
            '7':'--...', '8':'---..', '9':'----.', 
            '0':'-----', ', ':'--..--', '.':'.-.-.-', 
            '?':'..--..', '/':'-..-.', '-':'-....-', 
            '(':'-.--.', ')':'-.--.-'} 
        self.__dic_cipher = {self.__dic_plain[i]:i for i in self.__dic_plain}
    def encrypt(self, string):
        string = string.upper()
        lst = []
        for i in string:
            if i in self.__dic_plain:
                lst+=[self.__dic_plain[i], ' ']
            elif i == ' ':
                lst+=[i]
            else:
                lst+=[i, ' ']
        return ''.join(lst).lower()
    def decrypt(self, string):
        string = string.split(' ')
        lst = []
        for i in string:
            if i in self.__dic_cipher:
                lst+=[self.__dic_cipher[i]]
            elif i == '':
                lst+=[' ']
            else:
                lst+=[i]
        return ''.join(lst).lower()
        

