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


##############parte1###############

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

##############parte2##############

def sha256sum(filename):
    key = "Guido"
    h  = sha256()
    b  = bytearray(128*1024)
    mv = memoryview(b)
    with open(filename, 'rb', buffering=0) as f:
        for n in iter(lambda : f.readinto(mv), 0):
            palabra = mv[:n]
        h.update(palabra)
    return h.hexdigest()

def sha512sum(filename):
    key = "Guido"
    h  = sha512()
    b  = bytearray(128*1024)
    mv = memoryview(b)
    with open(filename, 'rb', buffering=0) as f:
        for n in iter(lambda : f.readinto(mv), 0):
            palabra = mv[:n]
        h.update(palabra)
    return h.hexdigest()

def blake2bsum(filename):
    key = "hola"
    h  = blake2b(key=key.encode('utf-8'),digest_size=64)
    b  = bytearray(128*1024)
    mv = memoryview(b)
    with open(filename, 'rb', buffering=0) as f:
        for n in iter(lambda : f.readinto(mv), 0):
            palabra = mv[:n]
        h.update(palabra)
    return h.hexdigest()

def verificacion(filename,hashh,key):
    h  = blake2b(key=key.encode('utf-8'),digest_size=64)
    b  = bytearray(128*1024)
    mv = memoryview(b)
    with open(filename, 'rb', buffering=0) as f:
        for n in iter(lambda : f.readinto(mv), 0):
            palabra = mv[:n]
        h.update(palabra)
        h.hexdigest()
        if(h.hexdigest() == hashh):
            return "Verificado, el hash corresponde al archivo"
        else:
            return "El hash no corresponde al archivo"

print("\nSHA256")
print("Archivo 1:",sha256sum("ejemplo.txt"))
print("Archivo 2:",sha256sum("ejemplo2.txt"))
print("\nSHA512")
print("Archivo 1:",sha512sum("ejemplo.txt"))
print("Archivo 2:",sha512sum("ejemplo2.txt"))
print("\nBLAKE2B")
print("Archivo 1:",blake2bsum("ejemplo.txt"))
print("Archivo 2:",blake2bsum("ejemplo2.txt"))
print("")
print("Prueba con el hash1 en el archivo1:",verificacion("ejemplo.txt",blake2bsum("ejemplo.txt"),"hola"))
print("Prueba con el hash2 en el archivo1:",verificacion("ejemplo.txt",blake2bsum("ejemplo2.txt"),"hola"))
