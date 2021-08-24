from web3 import Web3
import environment.getenv
from scripts import terminate

def fantom():
    w3 = Web3(Web3.HTTPProvider(environment.getenv.ftm_API()))
    return evaluate(w3)

def ethereum():
    w3 = Web3(Web3.HTTPProvider(environment.getenv.ethereum_API()))
    return evaluate(w3)

def matic():
    w3 = Web3(Web3.HTTPProvider(environment.getenv.matic_API()))
    return evaluate(w3)

def evaluate(w3):
    connected = w3.isConnected()

    if connected == False:
        print('failed :: w3:: RPC connection has failed...')
        terminate.exitProcedure()
    else:
        print('RPC Connected: ' + str(w3.isConnected()))
        return w3