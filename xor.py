# Python program to implement XOR Cipher


def encrypt(message, key): 
    xorKey = ''
    cipher = ''
    while len(xorKey) < len(message):
        xorKey += key 
    
    for i in range(len(message)): 
        cipher += chr(ord(message[i]) ^ ord(xorKey[i]))
      
    return cipher; 


def decrypt(message, key): 
    xorKey = ''
    decipher = ''
    while len(xorKey) < len(message):
        xorKey += key 
    
    for i in range(len(message)): 
        decipher += chr(ord(message[i]) ^ ord(xorKey[i]))
      
    return decipher;


# Driver code
if __name__ == "__main__": 
    key = 'K'
    text = "Break Me If You Can @#"
    print(f'Original Text = {text}')
    print(f'Encrypted Text: {encrypt(text,key)}')
    print(f'Decrypted Text: {decrypt(encrypt(text,key),key)}')