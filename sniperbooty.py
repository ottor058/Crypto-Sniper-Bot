from eth_utils.currency import to_wei
from web3 import Web3
import json
import time
import config

from web3.contract import build_transaction_for_function
from web3.types import SignedTx
import config

# Connect to binance smart chain
bsc = "https://bsc-dataseed.binance.org/"
web3 = Web3(Web3.HTTPProvider(bsc))
#print(web3.isConnected())

# Interaction with Pancakeswap smart contract
pancakeRouterContractAdress = '0x10ED43C718714eb63d5aA57B78B54704E256024E'
text_file = open("pancakeAbi.txt", "r")
pancakeAbi = text_file.read()

# Wallet adress and balance
sender_adress = 'ENTER SENDER ADRESS'
# balance = web3.eth.get_balance(sender_adress)
# print(balance)
# balance_readable = web3.fromWei(balance, 'ether')
# print(balance_readable)

contract = web3.eth.contract(address=pancakeRouterContractAdress, abi=pancakeAbi)
tokenToBuy = web3.toChecksumAddress('0xae2df9f730c54400934c06a17462c41c08a06ed8')

# bnb doesn't have an ethereum adress, so we have to wrap bnb
spend = web3.toChecksumAddress('0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c') #wbnb contract

nonce = web3.eth.get_transaction_count(sender_adress)

start = time.time()

pancakeswap_txn = contract.functions.swapExactETHForTokens(
    0, # set to 0, or if you want to specify amount of tokens you want to receive (consider decimals)
    [spend,tokenToBuy],
    sender_adress,
    (int(time.time()) + 10000)
).buildTransaction({
    'from': sender_adress,
    'value': web3.toWei(0.01,'ether'), #This is the Token (BNB) amount you want to swap from
    'gas': 250000,
    'gasPrice': web3.toWei('5','gwei'),
    'nonce':nonce,
})

#Sign and send the transaction
signed_txn = web3.eth.account.sign_transaction(pancakeswap_txn, private_key = config.private) #add private key to your config file
tx_token = web3.eth.send_raw_transaction(signed_txn.rawTransaction)

print('Sending transaction...')
print(web3.toHex(tx_token))
print('Token successfully purchased (0.01 BNB)')