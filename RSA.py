import rsa
import time
#from timer import Timer

def generateKeys():
    (publicKey, privateKey) = rsa.newkeys(2048)
    with open('keys/publicKey.pem', 'wb') as p:
        p.write(publicKey.save_pkcs1('PEM'))
    with open('keys/privateKey.pem', 'wb') as p:
        p.write(privateKey.save_pkcs1('PEM'))


def loadKeys():
    with open('keys/publicKey.pem', 'rb') as p:
        publicKey = rsa.PublicKey.load_pkcs1(p.read())
    with open('keys/privateKey.pem', 'rb') as p:
        privateKey = rsa.PrivateKey.load_pkcs1(p.read())
    return publicKey, privateKey


def encrypt(message, key):
    return rsa.encrypt(message.encode('ascii'), key)


def decrypt(ciphertext, key):
    try:
        return rsa.decrypt(ciphertext, key).decode('ascii')
    except:
        return False

def sign(message, key):
    return rsa.sign(message.encode('ascii'), key, 'SHA-1')

def verify(message, signature, key):
    try:
        return rsa.verify(message.encode('ascii'), signature, key) == 'SHA-1'
    except:
        return False

generateKeys()
publicKey, privateKey =loadKeys()

message = input('Write your message here:')

tic = time.perf_counter()
#t = Timer()
# t.start()

#start = process_time()

ciphertext = encrypt(message, publicKey)
signature = sign(message, privateKey)
text = decrypt(ciphertext, privateKey)

#t.stop()

#end = process_time()
#print("process time in seconds:", end-start)
toc = time.perf_counter()
print(f"\nRSA encrypt and decrypt {toc - tic:0.4f} seconds\n")

print(f'Cipher text: {ciphertext}')
print(f'\nSignature: {signature}')

if text:
    print(f'\nMessage text: {text}')
else:
    print(f'\nUnable to decrypt the message.')

if verify(text, signature, publicKey):
    print("\nSuccessfully verified signature")
else:
    print('\nThe message signature could not be verified')