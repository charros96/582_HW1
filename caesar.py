import string
def encrypt(key,plaintext):
    ciphertext=""
    uppers = string.ascii_uppercase
    for letter in plaintext:
        i = uppers.index(letter)
        ciphertext = ciphertext + (uppers[(i+key)%26])
    return ciphertext

def decrypt(key,ciphertext):
    plaintext=""
    plaintext = encrypt(-key,ciphertext)
    return plaintext

#key = -26
#ciphertext = encrypt(key,"BIG")

#print(ciphertext)
#print(decrypt(key,ciphertext))