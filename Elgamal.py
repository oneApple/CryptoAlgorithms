from Crypto import Random
from Crypto.Random import random
import CustomElgamal
from Crypto.PublicKey.pubkey import *
from Crypto.Util import number

def GetElgamalParamqp(bits = 100):
    while 1:
        q = bignum(getPrime(bits-1, Random.new().read))
        p = 2*q+1
        if number.isPrime(p, randfunc=Random.new().read):
            break
    return q,p

class Elgamal:
    def __init__(self,q,p,bits = 100):
        self.__elgamalobject = CustomElgamal.generate(bits, q,p,Random.new().read)
        self.__getRandomk()
        
    def __getRandomk(self):
        while 1:
            k = random.StrongRandom().randint(1,self.__elgamalobject.p-1)
            if GCD(k,self.__elgamalobject.p-1)==1: break
        self.__k = k
    
    def __StringTolist(self,string,blocksize):
        blocknum = len(string) / blocksize
        for i in range(blocknum):
            yield string[:blocksize]
            string = string[blocksize:]
        yield string
    
    def StringToList(self,string,blocksize = 12):
        return list(self.__StringTolist(string, blocksize))
    
    def __EncryptoList(self,stringlist):
        for string in stringlist:
            yield self.__elgamalobject.encrypt(string, self.__k)[1]
            #print self.__elgamalobject.decrypt(self.__elgamalobject.encrypt(string, self.__k))
    def EncryptoList(self,stringlist):
        return list(self.__EncryptoList(stringlist))
    
    def CompareStringList(self,stringlist1,stringlist2):
        len1 = len(stringlist1)
        len2 = len(stringlist2)
        if len1 != len2:
            return False
        for i in range(len1):
            if stringlist1[i] != stringlist2[i]:
                return False
        return True

if __name__ == '__main__':
    param = GetElgamalParamqp()
    e1 = Elgamal(*param)
    e2 = Elgamal(*param)

    s1 = e1.EncryptoList(e2.EncryptoList(e1.StringToList("message12345678901234567890")))
    s2 = e2.EncryptoList(e1.EncryptoList(e1.StringToList("message12345678901234567890")))

    print e1.CompareStringList(s1,s2)