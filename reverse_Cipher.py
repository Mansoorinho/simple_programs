#Reverse Cipher by Mansoor Nabawi
# January 20 2020
message = "Three can keep a secret, if two of them are dead."

translated = ''

i = len(message) - 1
while i>= 0:
    translated = translated + message[i]
    i = i -1

print(translated)

#### another way of reverse cipher by me
new_msg = "this should work for reverse cipher"
j = -(len(new_msg))
rev_msg = ""
n=-1
while (n >= j):
    rev_msg = rev_msg + new_msg[n]
    n = n - 1
print("new cipher result: ", rev_msg)