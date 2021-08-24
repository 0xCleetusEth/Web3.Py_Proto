from dotenv import load_dotenv
import os

load_dotenv()

def publicKey():
    farmAccountPublic = os.getenv('ACCOUNT_PUBLIC')
    return farmAccountPublic

def privateKey():
    farmAccountPrivate = os.getenv('ACCOUNT_PRIVATE')
    return farmAccountPrivate

def ethereum_API():
    API = os.getenv('ETH_API')
    return API

def ftm_API():
    API = os.getenv('FTM_API')
    return API

def matic_API():
    API = os.getenv('MATIC_API')
    return API

