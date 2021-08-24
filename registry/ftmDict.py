import interfaces

class SpookyswapStaking:
    
    def getAddr():
        SpookyswapStakingAddress = '0x2b2929E785374c651a81A63878Ab22742656DcDd'
        return SpookyswapStakingAddress

    def getABI():
        SpookyswapStakingABIPath = 'interfaces/ftminterfaces/SpookyswapStaking.txt'
        f = open(SpookyswapStakingABIPath, 'rt')
        return f.read()

    
