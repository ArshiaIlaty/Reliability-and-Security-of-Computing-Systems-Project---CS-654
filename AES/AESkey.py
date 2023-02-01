# from Crypto.Cipher import AES

# key = b'Sixteen byte key'
# cipher = AES.new(key, AES.MODE_EAX)
# nonce = cipher.nonce
# ciphertext, tag = cipher.encrypt_and_digest(data)


# key = b'Sixteen byte key'
# cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
# plaintext = cipher.decrypt(ciphertext)
# try:
#     cipher.verify(tag)
#     print("The message is authentic:", plaintext)
# except ValueError:
#     print("Key incorrect or message corrupted")

import binascii
import time
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from numpy import pad

data = b'Arshia Ilaty, this is the final project for CS 654, Fall Semester Instructor: Ignacio aj dshfdf f hadffhaf ajhfs fl;j dfhadflha;; fah hf  sg mjsg sgjadf ah jgh u'
print(data)
tic = time.perf_counter()
#encryption
key = get_random_bytes(16)
key_192 = get_random_bytes(24)
key_256 = get_random_bytes(32)


cipher = AES.new(key, AES.MODE_EAX)
ciphertext, tag = cipher.encrypt_and_digest(data)
nonce = cipher.nonce


stored_text = nonce + tag + ciphertext


#decryption
cipher = AES.new(key, AES.MODE_EAX, nonce)
data = cipher.decrypt_and_verify(ciphertext, tag)

toc = time.perf_counter()
print(f"\nAES encrypt and decrypt {toc - tic:0.4f} seconds\n")


print("\nkey192")
print(key_192)
print('AES encryption key 192:', binascii.hexlify(key_192))

print("\nkey256")
print(key_256)
print('AES encryption key 256:', binascii.hexlify(key_256))

print("\nkey128")
print(key)
print('AES encryption key:', binascii.hexlify(key))


print("\nciphertext:")
print(ciphertext)
print('\nCipherText HEX:', binascii.hexlify(key))
print("\ntag:")
print(tag)

print("\nstored text:")
print(stored_text)

print('\nour plain text after decryption:')
print(data)





# cipher = AES.new(key, AES.MODE_CBC)
# cipher_text = cipher.encrypt(pad(data, AES.block_size))
# iv = cipher.iv

# decrypt_cipher = AES.new(key, AES.MODE_CBC, iv)
# plain_text = decrypt_cipher.decrypt(cipher_text)


# cipher = AES.new(key, AES.MODE_CFB)
# cipher_text = cipher.encrypt(data)
# iv = cipher.iv

# decrypt_cipher = AES.new(key, AES.MODE_CFB, iv=iv)
# plain_text = decrypt_cipher.decrypt(cipher_text)


# cipher = AES.new(key, AES.MODE_OFB)
# cipher_text = cipher.encrypt(data)
# iv = cipher.iv

# decrypt_cipher = AES.new(key, AES.MODE_OFB, iv=iv)
# plain_text = decrypt_cipher.decrypt(cipher_text)


