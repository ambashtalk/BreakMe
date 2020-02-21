# Python code to implement Atbash Cipher

lookup_table = {'A' : 'Z', 'B' : 'Y', 'C' : 'X', 'D' : 'W', 'E' : 'V',
        'F' : 'U', 'G' : 'T', 'H' : 'S', 'I' : 'R', 'J' : 'Q',
        'K' : 'P', 'L' : 'O', 'M' : 'N', 'N' : 'M', 'O' : 'L',
        'P' : 'K', 'Q' : 'J', 'R' : 'I', 'S' : 'H', 'T' : 'G',
        'U' : 'F', 'V' : 'E', 'W' : 'D', 'X' : 'C', 'Y' : 'B', 'Z' : 'A',
        'a': 'z', 'b': 'y', 'c': 'x', 'd': 'w', 'e': 'v',
        'f': 'u', 'g': 't', 'h': 's', 'i': 'r', 'j': 'q',
        'k': 'p', 'l': 'o', 'm': 'n', 'n': 'm', 'o': 'l',
        'p': 'k', 'q': 'j', 'r': 'i', 's': 'h', 't': 'g',
        'u': 'f', 'v': 'e', 'w': 'd', 'x': 'c', 'y': 'b', 'z': 'a'}

def encrypt(message):
    cipher = ''
    for letter in message:
        # checks for space
        if (letter.isupper() or letter.islower()):
            # adds the corresponding letter from the lookup_table
            cipher += lookup_table[letter]
        else:
            # adds space
            cipher += letter
    return cipher

def decrypt(cipher):
    message = ''
    for letter in cipher:
        # checks for space
        if (letter.isupper() or letter.islower()):
            # adds the corresponding letter from the lookup_table
            message += lookup_table[letter]
        else:
            # adds space
            message += letter
    return message


# Driver code
if __name__ == '__main__': 
    text = 'Break Me If You Can @#'
    print(f'Original Text = {text}')
    print(f'Encrypted Text: {encrypt(text)}')
    print(f'Decrypted Text: {decrypt(encrypt(text))}')