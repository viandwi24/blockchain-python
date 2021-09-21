import json
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from base64 import b64decode, b64encode

class Transaction:

    def __init__(self, fromAddress, toAddress, amount):
        self.fromAddress = fromAddress
        self.toAddress = toAddress
        self.amount = amount
        self.signature = None

    def __repr__(self) -> str:
        return json.dumps({
            'fromAddress': self.fromAddress,
            'toAddress': self.toAddress,
            'amount': self.amount
        })

    def signing(self, privateKeyBase64String = ''):
        pattern = {
            'fromAddress': self.fromAddress,
            'toAddress': self.toAddress,
            'amount': self.amount,
        }
        privateKey = b64encode(privateKeyBase64String.encode('ascii'))
        key = RSA.importKey(format='DER', key=privateKey)
        signer = PKCS1_OAEP.new(key)
        self.signature = signer.encrypt(pattern)
        print(key)
        self.signature = privateKeyBase64String
        # signer = PKCS1_OAEP.new(privateKey)
        # print(signer.encrypt('test'))
        # self.signature = b64encode(signer.encrypt(json.dumps(pattern).decode()))
        return self

    def print(self):
        print(json.dumps({
            'fromAddress': self.fromAddress,
            'toAddress': self.toAddress,
            'amount': self.amount,
            'signature': self.signature
        }, indent=4))