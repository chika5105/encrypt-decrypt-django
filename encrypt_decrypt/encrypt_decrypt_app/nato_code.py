class NatoCode():
    def __init__(self):
        self.__dic_plain = {
    'a': 'alfa',
    'b': 'bravo',
    'c': 'charlie',
    'd':'delta',
    'e': 'echo',
    'f': 'foxtrot',
    'g': 'golf',
    'h': 'hotel',
    'i': 'india',
    'j': 'juliett',
    'k': 'kilo',
    'l': 'lima',
    'm': 'mike',
    'n': 'november',
    'o': 'oscar',
    'p': 'papa',
    'q': 'quebec',
    'r': 'romeo',
    's': 'sierra',
    't': 'tango',
    'u': 'uniform',
    'v': 'victor',
    'w': 'whiskey',
    'x': 'xray',
    'y': 'yankee',
    'z': 'zulu',
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine',
    '0': 'zero'

    }
        self.__dic_cipher = {self.__dic_plain[i]:i for i in self.__dic_plain}
    def encrypt(self, string):
        string = string.lower()
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
        string = string.lower().split(' ')
        lst = []
        for i in string:
            if i in self.__dic_cipher:
                lst+=[self.__dic_cipher[i]]
            elif i == '':
                lst+=[' ']
            else:
                lst+=[i]
        return ''.join(lst).lower()

       


