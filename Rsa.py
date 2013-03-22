from Crypto.PublicKey import RSA
import pickle ,random

class Rsa:
    def __init__(self,directory = "./"):
        self.__keydir = directory
        self.__prikeydir = self.__keydir + "prikey.pem"
        self.__pubkeydir = self.__keydir + "pubkey.pkl"
    
    def GenerateKeypair(self,bits = 1024):
        key = RSA.generate(bits)
        with open(self.__prikeydir,"w") as f:
            f.write(key.exportKey())
        with open(self.__pubkeydir,"w") as f:
            self.__pubkeystring = pickle.dump(key.publickey(), f)
    
    def EncryptByPubkey(self, plaintext, pubkeydir = ""):
        dir = self.__keydir + pubkeydir + "pubkey.pkl"
        with open(dir, 'r') as f:
            pubkey = pickle.load(f)
        return pubkey.publickey().encrypt(plaintext,random.randint(0,len(plaintext)))
    
    def DecryptByPrikey(self,ciphertext):
        with open(self.__prikeydir,'r') as f:
            key = RSA.importKey(f.read())
            return key.decrypt(ciphertext)
                
    def SignByPrikey(self,message):
        with open(self.__prikeydir,'r') as f:
            key = RSA.importKey(f.read())
            return key.sign(message, random.randint(0,len(message)))
        
    def VerifyByPubkey(self,message,sign,pubkeydir = ""):
        dir = self.__keydir + pubkeydir + "pubkey.pkl"
        with open(dir, 'r') as f:
            pubkey = pickle.load(f)
            return pubkey.verify(message,sign)
   
if __name__ == '__main__':
    r = Rsa()
    r.GenerateKeypair()
    print r.DecryptByPrikey(r.EncryptByPubkey("plaintex"))
    print r.VerifyByPubkey("message", r.SignByPrikey("messag"))
            
        
    
        
        
        
        