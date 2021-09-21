import hashlib
import json
import time

class Block:

    def __init__(self, index, transactions, previousHash = ''):
        self.index = index
        self.transactions = transactions
        self.timestamp = time.time()
        self.nonce = 0
        self.previousHash = previousHash
        self.hash = self.calculateHash()
        self.miner = None

    def calculateHash(self):
        pattern = f"{self.index}{self.timestamp}{self.previousHash}{self.transactions}{self.nonce}"
        return hashlib.sha256(pattern.encode()).hexdigest()

    def mine(self, miner, difficulty = 1):
        self.miner = miner
        searchHash = self.hash
        while (searchHash[:difficulty] == "0" * difficulty) is False:
            self.nonce += 1
            self.timestamp = time.time()
            searchHash = self.calculateHash()
            # print(f"[Block][Mining] Searching for hash with nonce {self.nonce} and found {searchHash}")
        self.hash = searchHash

    def print(self):
        print('==[ BLOCK')
        print(json.dumps({
            'index': self.index,
            'timestamp': self.timestamp,
            'hash': self.hash,
            'previousHash': self.previousHash,
            'miner': self.miner,
            'nonce': self.nonce,
        }, indent=4))
        for transaction in self.transactions: transaction.print()