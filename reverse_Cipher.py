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
def reverse_function (new_msg):
    ##new_msg="this new approach works too"
    j = -(len(new_msg))
    rev_msg = ""
    n=-1
    while (n >= j):
        rev_msg = rev_msg + new_msg[n]
        n = n - 1
    print("new cipher result: ", rev_msg)

### asking for user input to be reversed
user_input = input("Insert your message to be reversed: ")
cipher = reverse_function(user_input)