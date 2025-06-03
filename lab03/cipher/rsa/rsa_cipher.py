import rsa as rsa_lib, os # Changed import to use an alias for the 'rsa' library

if not os.path.exists('cipher/rsa/keys'):
    os.makedirs('cipher/rsa/keys')

class RSACipher:
    def __init__(self):
        pass

    def generate_keys(self):
        # Use the aliased 'rsa_lib' to call newkeys from the actual rsa library
        (public_key, private_key) = rsa_lib.newkeys(1024) 
        with open('cipher/rsa/keys/publicKey.pem', 'wb') as p:
            p.write(public_key.save_pkcs1('PEM'))
        with open('cipher/rsa/keys/privateKey.pem', 'wb') as p:
            p.write(private_key.save_pkcs1('PEM'))

    def load_keys(self):
        with open('cipher/rsa/keys/publicKey.pem', 'rb') as p:
            # Use the aliased 'rsa_lib' to load public key
            public_key = rsa_lib.PublicKey.load_pkcs1(p.read()) 
        with open('cipher/rsa/keys/privateKey.pem', 'rb') as p:
            # Use the aliased 'rsa_lib' to load private key
            private_key = rsa_lib.PrivateKey.load_pkcs1(p.read()) 
        return private_key, public_key

    def encrypt(self, message, key):
        # Use the aliased 'rsa_lib' for encryption
        return rsa_lib.encrypt(message.encode('ascii'), key)

    def decrypt(self, ciphertext, key):
        try:
            # Use the aliased 'rsa_lib' for decryption
            return rsa_lib.decrypt(ciphertext, key).decode('ascii')
        except:
            return False

    def sign(self, message, key):
        # Use the aliased 'rsa_lib' for signing
        return rsa_lib.sign(message.encode('ascii'), key, 'SHA-1')

    def verify(self, message, signature, key):
        try:
            # Use the aliased 'rsa_lib' for verification
            return rsa_lib.verify(message.encode('ascii'), signature, key,) == 'SHA-1'
        except:
            return False