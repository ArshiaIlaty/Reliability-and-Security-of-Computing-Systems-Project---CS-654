import binascii
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

key = b"aaaabbbbccccdddd"
cipher = AES.new(key, AES.MODE_ECB)

with open("AES/tux.bmp", "rb") as f:
  clear = f.read()

clear_trimmed = clear[64:-2]
ciphertext = cipher.encrypt(clear_trimmed)

ciphertext = clear[0:64] + ciphertext + clear[-2:]
with open("tux_ecb.bmp", "wb") as f:
  f.write(ciphertext)

with open("tux_ecb.bmp", "rb") as f:
  bytes = f.read()


iv = b"0000111122223333"
cipher = AES.new(key, AES.MODE_CBC, iv)
ciphertext = cipher.encrypt(clear_trimmed)
ciphertext = clear[0:64] + ciphertext + clear[-2:]
with open("tux_cbc.bmp", "wb") as f:
  f.write(ciphertext)