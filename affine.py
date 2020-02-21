# Python program to implement Affine Cipher

# Extended Euclidean Algorithm for finding modular inverse
# eg: modinv(7, 26) = 15
def egcd(a, b):
    x, y, u, v = 0, 1, 1, 0
    while a != 0:
        q, r = b // a, b % a
        m, n = x - u * q, y - v * q
        b, a, x, y, u, v = a, r, u, v, m, n
    gcd = b
    return gcd, x, y


def modinv(a, m):
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None  # modular inverse does not exist
    else:
        return x % m


# affine cipher encryption function returns the cipher text
def encrypt(text, a, b):
    '''
    C = (a*P + b) % 26
    '''
    return ''.join([chr(((a * (ord(t) - ord('A')) + b) % 26) + ord('A')).upper() if t.isupper() else chr(((a * (ord(t) - ord('a')) + b) % 26) + ord('a')).lower() if t.islower() else t for t in text])


# affine cipher decryption function returns original text
def decrypt(cipher, a, b):
    '''
    P = (a^-1 * (C - b)) % 26
    '''
    # for i in range(len(text)):
    return ''.join(
        [chr(((modinv(a, 26) * (ord(c) - ord('A') - b)) % 26) + ord('A')).upper() if c.isupper() else chr(((modinv(a, 26) * (ord(c) - ord('a') - b)) % 26) + ord('a')).lower() if c.islower() else c for c in cipher])


# Driver code
if __name__ == '__main__': 
    a = 17
    b = 20
    text = 'Break Me If You Can @#'
    print(f'Original Text = {text}')
    print(f'Encrypted Text: {encrypt(text, a, b)}')
    print(f'Decrypted Text: {decrypt(encrypt(text, a, b), a, b)}')