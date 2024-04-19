import time
import os

class CaesarCipher:
    def __init__(self, name):
        self.name = name
        self.alphabet_1 ='abcdefghijklmnopqrstuvwxyz'
        self.alphabet_2='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.alphabet_3 = 'ÁÉÍÓÚÀÈÌÒÙÂÊÎÔÛÃÕÇ'
        self.alphabet_4 = 'áéíóúàèìòùâêîôûãõç'

    def key_passer(self):
        request_1 = str(input('Enter the letters of the alphabet you want to decipher.\nLetters: '))
        request_2 = int(input('What key do you want to use for decryption?\nKey number: '))

        letters = ''
        for char in request_1:
            if char.isupper():
                if char in self.alphabet_3:
                    letters += char
                    continue
                locating = self.alphabet_2.index(char)
                position = locating + request_2
                letter = self.alphabet_2[position]
                uppercase_letter = letter.upper()
                letters += uppercase_letter
            elif char.islower():
                if char in self.alphabet_4:
                    letters += char
                    continue
                locating = self.alphabet_1.index(char)
                position = locating + request_2
                letter = self.alphabet_1[position]
                lowercase_letter = letter.lower()
                letters += lowercase_letter
        print(f'This is the {self.name} encoding: {letters}')

# Welcome message
print('Welcome to Caesar Cipher!')
print('===========================')
start = int(input('Do you want to start the program? 1 - YES | 2 - NO\nAnswer: '))
name = str(input('What is your name?\nEnter your name here: '))
user = CaesarCipher(name)
print(f'Alright {name}. We are starting the decipher...')
time.sleep(2)
os.system('cls')

if start == 1:
    while True:
        user.key_passer()
        continue_option = int(input('Do you want to continue? 1 - YES | 2 - NO\nAnswer: '))
        if continue_option == 1:
            os.system('cls')
            continue
        else:
            print(f'Closing Caesar Cipher!\nGoodbye {name}')
            break
else:
    print(f'Closing Caesar Cipher!\nGoodbye {name}')
