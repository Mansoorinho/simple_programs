#Caesar Cipher Hacker by Mansoor Nabawi
#January 22 2020
#https://github.com/Mansoorinho/simple_programs (BSD Licensed)

message = "7uv6Jv6JnJ6rp5r7Jzr66ntr"
SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?."

#Loop through every possible key:
for key in range(len(SYMBOLS)):
    translated=""
    for symbol in message:
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            translatedIndex = symbolIndex - key

            #Handle the wraparound
            if translatedIndex < 0:
                translatedIndex = translatedIndex + len(SYMBOLS)
            
            #append the decrypted symbol:
            translated = translated + SYMBOLS[translatedIndex]
        else:
            translated = translated + symbol
        print("key #%s: %s" % (key, translated))