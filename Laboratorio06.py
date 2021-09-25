#Codigo de referencia: https://nitratine.net/blog/post/how-to-hash-passwords-in-python/

#Librerias a utilizar
import hashlib
import getpass
import hmac
import os

#Funcion para registrar ususarios nuevos.
def Register(usuario, contraseña):
    try:
        with open('registros.txt', 'a') as doc:
            salt = os.urandom(hashlib.blake2b.SALT_SIZE)
            process = hashlib.pbkdf2_hmac("sha512", str.encode(contraseña), salt, 100)
            hashed = process.hex()
            doc.write(usuario + " " + salt.hex() + " " + hashed + "\n")
            return True
    except OSError:
        print("Intente de nuevo ): ")

#Funcion para iniciar sesion. 
def Login(usuario, contraseña):
    try:
        with open('registros.txt', 'r') as data:
            datos = data.read().splitlines()
            for d in datos:
                singleLine = d.split(" ")
                if(usuario == singleLine[0]):
                    salt = bytes.fromhex(singleLine[1])
                    process = hashlib.pbkdf2_hmac("sha512", str.encode(contraseña), salt, 100)
                    hashed = process.hex()
                    if(hashed == singleLine[2]):
                        return True
                    else:
                        return False
                    
    except OSError:
        print("Intentelo de nuevo ); ")

#Menu 
menu = input("1. Registrarse\n2. Iniciar Sesion\nA continuacion ingrese la opcion que desea realizar: ")
while menu != 0:
    
    if menu == '1':
        usuario = input("Ingrese su Usuario:")
        contra = getpass.getpass("Ingrese su Contraseña:")
        if(Register(usuario, contra) == True):
            print("Se registro exitosamene (: ")

    elif menu == '2':
        usuario = input("Ingrese su Usuario:")
        contra = getpass.getpass("Ingrese su Contraseña:")
        if(Login(usuario, contra) == True):
            print(" Ingreso Exitosamente, Bienvenido (: ")
        else:
            print("Su usuario y/o contraseña no son correctos, por favor intente de nuevo.")

    menu = input("1. Registrarse\n2. Iniciar Sesion\nA continuacion ingrese la opcion que desea realizar: ")

