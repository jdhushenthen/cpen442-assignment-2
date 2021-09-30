'''
    Author: Janahan Dhushenthen (56777220)
    Date: 2021-09-29
    Description: CPEN 442 Assignment 2 - Problem 1
                 analyze_frequency(): finds frequency of letters in the ciphertext
                 decrypt_substitution(): applies key to recover plaintext from monoalphabetic substitution cipher
'''

import string

class Problem1:
    def __init__(self):
        self.ciphertext = "VRPARPNYONHHRJAKNJVPHRDPWJAXDDKNKPIHRJRKHHJCIXHKEPAJFJEHICJKIFOEEMUOQQEJIIXHHRJRKHHJCNCJDKCLNJJDJIHXRKSJWXNXCHXFDJKWPWTPWPHAXDDKKWIMJHPHVKNAJCHKPWEMJWTEPNRIXHPIXWHZOPHJOWIJCNHKWIMXOAXDDKNRJNKPIAXDDKKNUXEPHJEMKNNRJAXOEIIXHHRJIXCDXONJPNKNEJJUKTKPWAXDDKNKPIHRJRKHHJCAXDDKKWIRJUXOCJIKEPHHEJRXHHJKOUXWPHNWXNJIXHHRJIXCDXONJNRXXLPHNRJKIPDUKHPJWHEMAXDDKKWINKPIAXDDKVPHRXOHXUJWPWTPHNJMJNAXDDKXFAXOCNJAXDDKXFAXOCNJYONHVRKHPVKNTXPWTHXCJDKCLDMNJEFIXHRKSJMXOTOJNNJIHRJCPIIEJMJHHRJRKHHJCNKPIAXDDKHOCWPWTHXKEPAJKTKPW"    
        self.key = {    'Z': 'Q', 
                        'Q': 'Z', 
                        'Y': 'J', 
                        'S': 'V', 
                        'L': 'K', 
                        'V': 'W', 
                        'F': 'F', 
                        'U': 'P', 
                        'T': 'G', 
                        'M': 'Y', 
                        'E': 'L', 
                        'O': 'U', 
                        'C': 'R', 
                        'A': 'C', 
                        'W': 'N', 
                        'R': 'H', 
                        'I': 'D', 
                        'D': 'M', 
                        'P': 'I', 
                        'N': 'S', 
                        'X': 'O', 
                        'K': 'A', 
                        'H': 'T', 
                        'J': 'E'    }

    def analyze_frequency(self):
        cipher_letter_frequency = {}

        for ch in string.ascii_uppercase:
            cipher_letter_frequency[ch] = self.ciphertext.count(ch)

        print("Frequency Analysis: ", dict(sorted(cipher_letter_frequency.items(), key=lambda item: item[1])))

    def decrypt_substitution(self):
        plaintext = ""

        for ch in self.ciphertext:
            plaintext += self.key[ch]
        
        print("Plaintext: ", plaintext)

if __name__ == "__main__":
    P1 = Problem1()
    #P1.analyze_frequency()
    P1.decrypt_substitution()