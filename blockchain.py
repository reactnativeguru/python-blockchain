# define blockchain list
blockchain = []

# get last value in chain


def get_last_blockchain_value():
    """return last value of current blockchain """
    if len(blockchain) < 1:
        return None
    return blockchain[-1]

# appending last element in list to the blochain


def add_transaction(transaction_amount, last_transaction=[1]):
    #  append new value as well as the last blockchain value to the blockchain
    # arguments:
    # : transaction_amount: amount to be added
    # :last_transaction: the last blockchain transaction (default[1])
    if last_transaction == None:
        last_transaction = [1]
    blockchain.append([last_transaction, transaction_amount])


def get_transaction_value():
    # returns the input of the user (a new transaction amount) as a float
    user_input = float(input('Your transaction amount please:: '))
    return user_input


def get_user_choice():
    user_input = input('Your choice: ')
    return user_input


def print_blockchain_elements():
    # print(blockchain)
    for block in blockchain:
        print('outputting block')
        print(block)


# # get second transaction input and add value to blockchain
# tx_amount = get_user_input()
# add_value(last_transaction=get_last_blockchain_value(),
#           transaction_amount=tx_amount)


# # get third transaction input and add value to blockchain
# tx_amount = get_user_input()
# add_value(tx_amount, get_last_blockchain_value())

while True:
    print('Please choose:')
    print('1: Add new transaction value')
    print('2: Output the blockchain blocks')
    print('q: Quit')
    user_choice = get_user_choice()

    if user_choice == '1':
        tx_amount = get_transaction_value()
        add_transaction(tx_amount, get_last_blockchain_value())

    elif user_choice == '2':
        print_blockchain_elements()

    elif user_choice == 'q':
        break
    else:
        print('Invalid value please enter valid value')
    print('Choice registered!')


print('Done')
