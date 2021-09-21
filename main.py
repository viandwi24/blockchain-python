from block import Block
from transaction import Transaction
from wallet import Wallet

def main():
    # create wallet
    myWallet = Wallet('Alfian Dwi Nugraha')
    # create tra
    transactions = [
        Transaction('sender', 'receiver-1', 100).signing(myWallet.privateKey),
        Transaction('receiver-2', 'sender', 10)
    ]
    newBlock = Block(0, transactions)
    newBlock.mine('miner-address')
    newBlock.print()

if __name__ == "__main__":
    main()