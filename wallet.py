from Crypto.PublicKey import RSA
from base64 import b64decode, b64encode

class Wallet:

    def __init__(self, name):
        self.name = name
        self.publicKey = None
        self.privateKey = None
        self.generate()
    
    def generate(self):
        key = RSA.generate(1024)
        self.publicKey = b64encode(key.publickey().exportKey(format='DER')).decode('ascii')
        self.privateKey = b64encode(key.exportKey(format='DER')).decode('ascii')