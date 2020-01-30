##Transpotition Cipher Encryption program by Mansoor Nabwi
## https://github.com/Mansoorinho/simple_programs (BSD Licensed)
# january 30 2020

import random, sys, Transposition_Cipher_Encryption, TranspostionCipher_Decryption

def main():
    random.seed(42)
    #test 20 times
    for i in range(20):
        #generate random messages to test
        #the message will have a random length
        message = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"*random.randint(4,40)
        #convert the message string to a list to shuffle it
        message = list(message)
        random.shuffle(message)
        message = "".join(message)

        print("Test #%s: '%s...'"%(i+1,message[:50]))

            #check all possible keys for each message
        for key in range(1,int(len(message)/2)):
            encrypted = Transposition_Cipher_Encryption.encryptMessage(key,message)
            decrypted = TranspostionCipher_Decryption.decryptMessage(key,encrypted)

            #if decryption deosn't match the original message, show an error and quit
            if message != decrypted:
                print("Missmatch with key %s and message: %s" % (key,message))
                print("Descrypted as: "+ decrypted)
                sys.exit()

    print("Transposition Cipher test passed")

if __name__ == "__main__":
    main()