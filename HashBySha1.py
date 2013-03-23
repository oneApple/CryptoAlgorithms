from Crypto.Hash import SHA
#the length of string is less than 2^21

class HashBySha1:
    def __init__(self):
        self.__hash = SHA.new()
    def GetHash(self,message):
        assert(pow(2,21) > len(message))
        self.__hash.update(message)
        return self.__hash.hexdigest()
    
if __name__ == '__main__':
    h = HashBySha1()
    print h.GetHash('Hello')