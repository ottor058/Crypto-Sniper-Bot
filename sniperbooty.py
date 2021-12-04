from web3 import Web3
import json
import time
import config

# Connect to binance smart chain
bsc = "https://bsc-dataseed.binance.org/"
web3 = Web3(Web3.HTTPProvider(bsc))
print(web3.isConnected())

# Interaction with Pancakeswap smart contract
pancakeRouterContractAdress = '0x10ED43C718714eb63d5aA57B78B54704E256024E'
text_file = open("pancakeAbi.txt", "r")
pancakeAbi = text_file.read()
