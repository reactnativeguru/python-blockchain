# define blockchain list
blockchain = []

# get last value in chain


def get_last_blockchain_value():
    return blockchain[-1]

# appending last element in list to the blochain


def add_value(transaction_amount, last_transaction=[1]):
    #  append new value as well as the last blockchain value to the blockchain
    # arguments:
    # : transaction_amount: amount to be added
    # :last_transaction: the last blockchain transaction (default[1])
    blockchain.append([last_transaction, transaction_amount])


def get_user_input():
    # returns the input of the user (a new transaction amount) as a float
    user_input = float(input('Your transaction amount please:: '))
    return user_input


# get the first transaction inout and add the value to the blockchain
tx_amount = get_user_input()
add_value(tx_amount)

# get second transaction input and add value to blockchain
tx_amount = get_user_input()
add_value(last_transaction=get_last_blockchain_value(),
          transaction_amount=tx_amount)


# get third transaction input and add value to blockchain
tx_amount = get_user_input()
add_value(tx_amount, get_last_blockchain_value())


print(blockchain)
