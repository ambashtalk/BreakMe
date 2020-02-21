# Python program to implement Baconian cipher

'''This script uses a dictionary instead of 'chr()' & 'ord()' function'''

# Dictionary to map plaintext with ciphertext
# (key:value) => (plaintext:ciphertext)
# This script uses the 26 letter baconian cipher
# in which I, J & U, V have distinct patterns


lookup = {'A': 'AAAAA', 'B': 'AAAAB', 'C': 'AAABA', 'D': 'AAABB', 'E': 'AABAA',
         'F': 'AABAB', 'G': 'AABBA', 'H': 'AABBB', 'I': 'ABAAA', 'J': 'ABAAB',
         'K': 'ABABA', 'L': 'ABABB', 'M': 'ABBAA', 'N': 'ABBAB', 'O': 'ABBBA',
         'P': 'ABBBB', 'Q': 'BAAAA', 'R': 'BAAAB', 'S': 'BAABA', 'T': 'BAABB',
         'U': 'BABAA', 'V': 'BABAB', 'W': 'BABBA', 'X': 'BABBB', 'Y': 'BBAAA', 'Z': 'BBAAB',
         'a': 'aaaaa', 'b': 'aaaab', 'c': 'aaaba', 'd': 'aaabb', 'e': 'aabaa',
         'f': 'aabab', 'g': 'aabba', 'h': 'aabbb', 'i': 'abaaa', 'j': 'abaab',
         'k': 'ababa', 'l': 'ababb', 'm': 'abbaa', 'n': 'abbab', 'o': 'abbba',
         'p': 'abbbb', 'q': 'baaaa', 'r': 'baaab', 's': 'baaba', 't': 'baabb',
         'u': 'babaa', 'v': 'babab', 'w': 'babba', 'x': 'babbb', 'y': 'bbaaa', 'z': 'bbaab'}


# Function to encrypt the string according to the cipher provided
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


# Function to decrypt the string
# according to the cipher provided
def decrypt(message):
    decipher = ''
    i = 0

    # emulating a do-while loop
    while True:
        # condition to run decryption till
        # the last set of cipher text
        if (i < len(message) - 4):
            # extracting a set of cipher text
            # from the message
            substr = message[i:i + 5]
            # checking for space as the first
            # character of the substring
            if substr[0].isupper() or substr[0].islower():

                # This statement gets us the key(plaintext) using the values(cipher text)
				# Just the reverse of what we were doing in encrypt function

                decipher += list(lookup.keys())[list(lookup.values()).index(substr)]
                i += 5  # to get the next set of ciphertext

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