#Transposition Cipher Encryption/Decryption File by Mansoor Nabawi
#February 2 2020
#https://github.com/Mansoorinho/simple_programs (BSD Licensed)
import time, os, sys, Transposition_Cipher_Encryption, TranspostionCipher_Decryption

def main():
    inputFilename = 'frankenstein.txt'

    outputFilename = 'frankenstein.encrypted.txt'
    myKey = 10
    myMode = 'encrypt'

    if os.path.exists(outputFilename):
        print("This will overwrite the file %s. (C)ontinue or (Q)uit?" %(outputFilename))
        response = input("> ")
        if not response.lower().startswith('c'):
            sys.exit()

    fileObj = open(inputFilename)
    content = fileObj.read()
    fileObj.close()

    print("%sing..." % (myMode.title()))
    #measure how long the encryption/decryption takes:
    startTime = time.time()
    if myMode == 'encrypt':
        translated = Transposition_Cipher_Encryption.encryptMessage(myKey, content)
    elif myMode == 'decrypt':
        translated = TranspostionCipher_Decryption.decryptMessage (myKey, content)
    totalTime = round(time.time() - startTime, 2)
    print("%sion time: %s seconds" % (myMode.title(), totalTime))

    #Write out the translated message to the output file:
    outputFileObj = open(outputFilename, "w")
    outputFileObj.write(translated)
    outputFileObj.close()

    print("Done %sing %s (%s characters)." %(myMode,inputFilename,len(content)))
    print("%sed file is %s." % (myMode.title(), outputFilename))

if __name__ == "__main__":
    main()