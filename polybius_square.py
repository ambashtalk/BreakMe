# Python Program to implement Polybius Square cipher

# Decrypt function is to be written and 2 outputs will be shown as 'i' and 'j' have same values

lookup = {'A': '11', 'B': '12', 'C': '13', 'D': '14', 'E': '15', 
          'F': '21', 'G': '22', 'H': '23', 'I': '24', 'J': '24','K': '25', 
          'L': '31', 'M': '32', 'N': '33', 'O': '34', 'P': '35', 
          'Q': '41', 'R': '42', 'S': '43', 'T': '44', 'U': '45', 
          'V': '51', 'W': '52', 'X': '53', 'Y': '54', 'Z': '55',
          'a': '11', 'b': '12', 'c': '13', 'd': '14', 'e': '15', 
          'f': '21', 'g': '22', 'h': '23', 'i': '24', 'j': '24','k': '25', 
          'l': '31', 'm': '32', 'n': '33', 'o': '34', 'p': '35', 
          'q': '41', 'r': '42', 's': '43', 't': '44', 'u': '45', 
          'v': '51', 'w': '52', 'x': '53', 'y': '54', 'z': '55',}

antilookup = {'11': 'A', '12': 'B', '13': 'C', '14': 'D', '15': 'E', 
              '21': 'F', '22': 'G', '23': 'H', '24': 'I', '25': 'K', 
              '31': 'L', '32': 'M', '33': 'N', '34': 'O', '35': 'P', 
              '41': 'Q', '42': 'R', '43': 'S', '44': 'T', '45': 'U', 
              '51': 'V', '52': 'W', '53': 'X', '54': 'Y', '55': 'Z'}

def encrypt(message):
    cipher = ''
    for letter in message:
        # checks for space
        if letter.isupper() or letter.islower():
            # adds the ciphertext corresponding to the plaintext from the dictionary
            cipher += lookup[letter]
        else:
            # adds special character
            cipher += letter
    return cipher


def decrypt(message):
    decipher = ''
    i = 0

    # emulating a do-while loop
    while True:
        # condition to run decryption till
        # the last set of cipher text
        if (i < len(message) - 1):
            # extracting a set of cipher text
            # from the message
            substr = message[i:i + 2]
            # checking for space as the first
            # character of the substring
            if substr[0].isdigit() and substr[1].isdigit() and substr in antilookup.keys():

                # This statement gets us the key(plaintext) using the values(cipher text)
				# Just the reverse of what we were doing in encrypt function

                decipher += antilookup[substr]
                i += 2  # to get the next set of ciphertext

            else:
                # adds space
                decipher += substr[0]
                i += 1  # index next to the space
        else:
            decipher += message[i:]
            break  # emulating a do-while loop

    return decipher

# Driver code
if __name__ == "__main__": 
    text = "Break Me If You Can @#"
    print(f'Original Text = {text}')
    print(f'Encrypted Text: {encrypt(text)}')
    print(f'Decrypted Text: {decrypt(encrypt(text))}')
    print(decrypt('121 3131424'))