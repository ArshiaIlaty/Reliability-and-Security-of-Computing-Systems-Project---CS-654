from hashlib import md5
from base64 import b64decode
from base64 import b64encode
from Crypto.Cipher import AES


BLOCK_SIZE = 16  # Bytes
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * \
                chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
unpad = lambda s: s[:-ord(s[len(s) - 1:])]


class AESCipher:
    def __init__(self, key):
        self.key = md5(key.encode('utf8')).hexdigest()

    def encrypt(self, raw):
        raw = pad(raw)
        cipher = AES.new(self.key.encode("utf8"), AES.MODE_ECB)
        return b64encode(cipher.encrypt(raw.encode('utf8')))

    def decrypt(self, enc):
        enc = b64decode(enc)
        cipher = AES.new(self.key.encode("utf8"), AES.MODE_ECB)
        return unpad(cipher.decrypt(enc)).decode('utf8')

# MAIN
# Just a test.
msg = input('Message...: ')
pwd = input('Password..: ')
c = AESCipher(pwd).encrypt(msg)
print('Ciphertext:', AESCipher(pwd).encrypt(msg))
print('Ciphertext:', AESCipher(pwd).decrypt(c))