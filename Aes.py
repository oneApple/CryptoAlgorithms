from Crypto.Cipher import AES
from Crypto import Random

import random

_sample = "1234567890qwertyuioasdfghjklzxcvbnm"

class Aes:
    def __init__(self,bits = 32,iv = None,key = None):
        if not iv or not key:
            self.__iv = Random.new().read(AES.block_size)
            self.__key = "".join(random.sample(_sample,bits))
        else:
            self.__iv = iv
            self.__key = key
        self.__cipher = AES.new(self.__key, AES.MODE_CFB, self.__iv)
    
    def GetKeyParam(self):
        return self.__iv,self.__key
    
    def Encrypt(self,plaintext):
        return self.__iv + self.__cipher.encrypt(plaintext)
    
    def Decrypt(self,ciphertext):
        return self.__cipher.decrypt(ciphertext)[len(self.__iv):]

if __name__ == '__main__':
    aes = Aes()
    print aes.GetKeyParam()
    print aes.Decrypt(aes.Encrypt("plaintext"))