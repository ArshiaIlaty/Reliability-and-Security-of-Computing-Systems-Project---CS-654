import binascii
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from numpy import pad

data = b'Arshia Ilaty, this is the final project for CS 654, Fall Semester Instructor: Ignacio'

key = get_random_bytes(16)
print("key")
print(key)
print('AES encryption key:', binascii.hexlify(key))

cipher = AES.new(key, AES.MODE_OFB)
cipher_text = cipher.encrypt(data)
iv = cipher.iv

print("ciphertext")
print(cipher_text)
print('cipher_text(hex):', binascii.hexlify(cipher_text))

# nobytestring = cipher_text.decode('utf-16')
# cipherbin = ' '.join(format(ord(x), 'b') for x in nobytestring)
# cipherMan = ''.join('1' if x == '0' else '0' for x in cipherbin)
# print('binary cipher text ready for manipulation:', cipherbin)
# print('binary cipher after manipulation:', cipherMan)

# binarytobyte = bytes(int(cipherMan[i : i + 8], 2) for i in range(0, len(cipherMan), 8))
# decryptcipher = AES.new(key, AES.MODE_ECB)
# plaintext = decryptcipher.decrypt(binarytobyte)
# print('\nour plain text after decryption:')
# print(plaintext)



decrypt_cipher = AES.new(key, AES.MODE_OFB, iv=iv)
plain_text = decrypt_cipher.decrypt(cipher_text)
print('our plain text after decryption:')
print(plain_text)