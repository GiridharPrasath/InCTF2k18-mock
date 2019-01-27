from Crypto.Util.number import *
from Crypto.PublicKey import RSA
import gmpy
 	
# size() from Crypto.Util.number tells the size of the number (in bits)

f = open("publickey.pem",'r').read();
n=RSA.importKey(f).n
e=RSA.importKey(f).e
obj1 = open("ciphertext.txt",'r').read();
obj1 = bytes_to_long(obj1)
m = gmpy.root(obj1, 3)[0]
if pow(m, 3, n) == obj1:
	print(long_to_bytes(m))

# Read this documentation on how to construct and import PEM files using pycrypto
# Public Key encryption: https://www.dlitz.net/software/pycrypto/api/2.6/toc-Crypto.PublicKey.RSA-module.html
# Construct PEM files: https://www.dlitz.net/software/pycrypto/api/2.6/Crypto.PublicKey.RSA-module.html#construct
# Import PEM files: https://www.dlitz.net/software/pycrypto/api/2.6/Crypto.PublicKey.RSA-module.html#importKey


