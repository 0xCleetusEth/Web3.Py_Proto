import web3
from environment import getenv
from scripts import connect, terminate
from registry import ftmDict
import scripts.spookyfarm

def toNormal(_inWei):
    _inNormal = w3.fromWei(_inWei, 'ether')
    return _inNormal

# Establish choice of infura/chain here, connect...
#connect.fantom(), connect.eth(), connect.matic()
w3 = connect.fantom()
me = getenv.publicKey()

balance = w3.eth.getBalance(me)
print(toNormal(balance))
    
#initializes spookychef interface, checks ftm-usdc pool for boo outstanding
contract = w3.eth.contract(address = ftmDict.SpookyswapStaking.getAddr(), abi = ftmDict.SpookyswapStaking.getABI())
print(toNormal(contract.functions.pendingBOO(2, me).call()))

# Call script here, such as spookyfarm.py - loop in script
if w3.isConnected():
    try:
        scripts.spookyfarm.farm()
    except:
        terminate.exitProcedure()

