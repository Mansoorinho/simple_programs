##Transpotition Cipher Encryption program by Mansoor Nabwi
## https://github.com/Mansoorinho/simple_programs (BSD Licensed)
# january 23 2020

import pyperclip

def main():
    myMessage = "This is a Secret Message"
    myKey = 13

    cipher_text = encryptMessage(myKey,myMessage)
    print(cipher_text+"|")
    pyperclip.copy(cipher_text)

def encryptMessage(Key,Message):
    ciphertext = [""]*Key
    for column in range(Key):
        currentIndex = column

        while currentIndex < len(Message):
            ciphertext[column] += Message[currentIndex]
            currentIndex += Key
    return "".join(ciphertext)

if __name__ == "__main__":
    main()