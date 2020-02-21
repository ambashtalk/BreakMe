# Python program to implement Caesar Cipher

def encrypt(text, s):
    result = ''

    # traverse text
    for i in range(len(text)):
        char = text[i]

        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + s - 65) % 26 + 65)

        # Encrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) + s - 97) % 26 + 97)

        # Leave special symbols as they are
        else:
            result += char

    return result


def decrypt(text, p):
    s = 26 - p
    result = ''

    # traverse text
    for i in range(len(text)):
        char = text[i]

        # Encrypt uppercase characters
        if (char.isupper()):
            result += chr((ord(char) + s - 65) % 26 + 65)

        # Encrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) + s - 97) % 26 + 97)

        # Leave special symbols as they are
        else:
            result += char

    return result


# Driver code
if __name__ == '__main__':
    text = 'Break Me If You Can @#'
    print(f'Original Text = {text}')
    print(f'Encrypted Text: {encrypt(text, 14)}')
    print(f'Decrypted Text: {decrypt(encrypt(text, 14), 14)}')
