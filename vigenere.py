# Python code to implement Vigenere Cipher

# This function generates the key in a cyclic manner until it's length isn't equal to the length of original text
def generateKey(string, key):
    key = ''.join([i for i in key if i.isupper() or i.islower()]).upper()
    string = ''.join([i for i in string if i.isupper() or i.islower()])
    key = list(key)
    if len(string) == len(key):
        return (key)
    else:
        for i in range(len(string) - len(key)): 
            key.append(key[i % len(key)])
    return ("".join(key))


# This function returns the encrypted text generated with the help of the key
def encrypt(string, key):
    key = generateKey(string, key)
    cipher_text = []
    k = 0
    string_copy = string
    string = string.upper()
    for i in range(len(string)):
        if string[i].isupper() or string[i].islower():
            x = (ord(string[i]) + ord(key[k])) % 26
            x += ord('A')
            k = k+1
        else:
            x = ord(string[i])
        if string_copy[i].islower():
            cipher_text.append(chr(x).lower())
        else:
            cipher_text.append(chr(x))
    return ("".join(cipher_text))


# This function decrypts the encrypted text and returns the original text
def decrypt(cipher_text, key):
    key = generateKey(cipher_text, key)
    orig_text = []
    k = 0
    cipher_text_copy = cipher_text
    cipher_text = cipher_text.upper()
    for i in range(len(cipher_text)):
        if cipher_text[i].isupper() or cipher_text[i].islower():
            x = (ord(cipher_text[i]) - ord(key[k]) + 26) % 26
            x += ord('A')
            k = k+1
        else:
            x = ord(cipher_text[i])
        if cipher_text_copy[i].islower():
            orig_text.append(chr(x).lower())
        else:
            orig_text.append(chr(x))
    return ("".join(orig_text))


# Driver code
if __name__ == "__main__": 
    text = "Break Me If You Can @#"
    key = "Hello World"
    print(f'Original Text = {text}')
    print(f'Encrypted Text: {encrypt(text,key)}')
    print(f'Decrypted Text: {decrypt(encrypt(text,key),key)}')\