##Transpotition Cipher Decryption program by Mansoor Nabwi
## https://github.com/Mansoorinho/simple_programs (BSD Licensed)
# january 27 2020

import math, pyperclip
def main():
    myMessage="Trheits  Miess saa gSeec"
    myKey=8
    plaintext = decryptMessage(myKey,myMessage)
    print(plaintext+"|")
    pyperclip.copy(plaintext)

def decryptMessage(key, message):
    