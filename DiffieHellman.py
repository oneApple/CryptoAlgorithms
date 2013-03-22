from random import getrandbits
from Crypto import Random
from Crypto.PublicKey.pubkey import *

_g = 2

def GetBigPrime(bits = 300):
    return bignum(getPrime(bits-1, Random.new().read))

class diffieHellman:
    def __init__(self, prime, bits = 300):
        self.__prime = prime
        while True:
            r = getrandbits(bits)
            if r < self.__prime:
                self.__randnum = r
                break
        self.pubkey = pow(_g, self.__randnum, self.__prime)
    def getPubkey(self):
        return self.pubkey
    def getKey(self,otherpubkey):
        return pow(otherpubkey,self.__randnum, self.__prime)
    
if __name__ == '__main__':
    p = GetBigPrime()
    d1 = diffieHellman(p)
    d2 = diffieHellman(p)

    print d2.getKey(d1.getPubkey())
    print d1.getKey(d2.getPubkey())
    