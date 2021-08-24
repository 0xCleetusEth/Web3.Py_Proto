import web3
from registry import ftmDict
from environment import getenv
from scripts import connect, terminate


def toNormal(_inWei):
    _inNormal = web3.fromWei(_inWei, 'ether')
    return _inNormal

# Establish choice of infura/chain here, connect...
#connect.fantom(), connect.eth(), connect.matic()
web3 = connect.fantom()
myAddress = getenv.publicKey()


balance = web3.eth.getBalance(myAddress)
print(toNormal(balance))
    
#initializes spookychef interface, checks ftm-usdc pool for boo outstanding
contract = web3.eth.contract(address = ftmDict.SpookyswapStaking.getAddr(), abi = ftmDict.SpookyswapStaking.getABI())
print(toNormal(contract.caller.pendingBOO(2, myAddress)))
terminate.exitProcedure()
