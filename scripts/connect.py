from web3 import Web3
import environment.getenv
from scripts import terminate

def fantom():
    web3 = Web3(Web3.HTTPProvider(environment.getenv.ftm_API()))
    return evaluate(web3)

def ethereum():
    web3 = Web3(Web3.HTTPProvider(environment.getenv.ethereum_API()))
    return evaluate(web3)

def matic():
    web3 = Web3(Web3.HTTPProvider(environment.getenv.matic_API()))
    return evaluate(web3)

def evaluate(web3):
    connected = web3.isConnected()

    if connected == False:
        print('failed :: web3 RPC connection has failed...')
        terminate.exitProcedure()
    else:
        print('RPC Connected: ' + str(web3.isConnected()))
        return web3