##Ceasar Cipher program by Mansoor Nabwi
## https://github.com/Mansoorinho/simple_programs (BSD Licensed)
# january 21 2020
#to copy the result into clipboard you can install it by
#pip install pyperclip
#you can comment it if you don't want to use it
import pyperclip
# the message to be decryped/encrypted
message = "7uv6Jv6JnJ6rp5r7Jzr66ntr"
#the key to decryption/encryption
key = 13
#Whether the program decrypts or encrypts
mode = "decrypt"

#Every possible symbols that can be decrypted
SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?."

##store the encrypted/decrypted message here
translated = ""
for symbol in message:
    # note only symbols in the SYMBOLS can be decrypted/encrypted
    if symbol in SYMBOLS:
        symbolIndex = SYMBOLS.find(symbol)
        #perform encryption/decryption
        if mode== "encrypt":
            translatedIndex = symbolIndex + key
        elif mode=="decrypt":
            translatedIndex = symbolIndex - key

            #handle wraparound, if needed
        if translatedIndex > len(SYMBOLS):
                translatedIndex = translatedIndex - len(SYMBOLS)
        elif translatedIndex < 0:
                translatedIndex = translatedIndex + len(SYMBOLS)

        translated = translated + SYMBOLS[translatedIndex]
    else:
                #append  the symbol without encrypting/decrypting
                translated = translated + symbol

print(translated)
pyperclip.copy(translated)