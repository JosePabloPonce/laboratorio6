import json
import re
from base64 import b64encode, b64decode
import hmac
import hashlib
import random
import ast
import codecs
from Crypto.Cipher import AES, DES
from Crypto import Random
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from hashlib import sha256
from hashlib import blake2b
from hashlib import sha512


##############parte1##############

print("SHA256")
h = sha256()
h.update(b'hello, world1!')
print('binario:', bin(int( h.hexdigest(), 16))[2:])
print('hexadecimal:', h.hexdigest())
print('base64:', codecs.encode(h.digest(), 'base64'))
print(" ")

print("SHA512")
k =sha512()
k.update(b'hello, world2!')
print('binario:', bin(int( k.hexdigest(), 16))[2:])
print('hexadecimal:', k.hexdigest())
print('base64:', codecs.encode(k.digest(), 'base64'))
print(" ")

print("BLAKE2B")
b = blake2b(digest_size=64)
b.update(b'hello, world3!')
print('binario:', bin(int( b.hexdigest(), 16))[2:])
print('hexadecimal:', b.hexdigest())
print('base64:', codecs.encode(b.digest(), 'base64'))