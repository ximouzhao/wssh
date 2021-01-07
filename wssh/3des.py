import hashlib;

from Crypto.Cipher import DES3
import base64
def create_key(sk):

    r=hashlib.md5(sk).digest()
    return r+r[:8]

def init_str(s):
    l=len(s) % 16
    if l!=0:
        c=16-l
        s+=chr(c)*c
    return s



 key='2345'#秘钥

b2bpwd="oohbv"
    keys=create_key(key)

 
    ss=init_str(b2bpwd)
    des3=DES3.new(keys,DES3.MODE_CFB)
    res2=des3.encrypt(ss)
    b2bencryptkey=  base64.standard_b64encode(res2)
    print b2bencryptkey