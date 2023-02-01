import binascii
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

data = b'secret data'
mandata = b'secret dat'
data1 = 'secret data'

bi = ' '.join(format(ord(x), 'b') for x in data1)
print(data)
print(bi)

key = get_random_bytes(16)
print("key:")
print(key)
print('\nAES encryption key:', binascii.hexlify(key))

cipher = AES.new(key, AES.MODE_ECB)
cipher_text = cipher.encrypt(pad(data, AES.block_size))
mancipher = cipher.encrypt(pad(mandata, AES.block_size))


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


print("\nciphertext:")
print(cipher_text)
print('\ncipher_text(hex):', binascii.hexlify(cipher_text))

print("\nManiupulated data and ciphertext:")
print(mancipher)

decrypt_cipher = AES.new(key, AES.MODE_ECB)
plain_text = decrypt_cipher.decrypt(cipher_text)
print('\nour plain text after decryption:')
print(plain_text)