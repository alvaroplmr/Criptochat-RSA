#Importamos las librerias
import rsa
import os
from typing import Tuple
import criptochat

#Funcion que recoge los datos que introduce el usuario
def pedir_datos() -> Tuple[str, int, int, str]:

    #Pide el nombre comprobando si esta ya creado y permitiendo cambiarla en caso de ya existir dicho usuario
    entrar = True
    while entrar:
        nombre = input("Introduce tu nombre: ")
    
        if os.path.exists("Usuarios"):
            contenido = os.listdir('Usuarios')

            if f'pub_{nombre}.txt' in contenido:
                print('Ya existe un usuario con ese nombre')
                opcion = input('Desea cambiar sus claves: (SI/NO)')
                if opcion.upper() != 'SI' and opcion.upper() != 'NO':
                    opcion = input('ERROR: Desea cambiar sus claves: (SI/NO)')

                if opcion.upper() == 'SI':
                    n = 3
                    clave_privada = criptochat.coger_claves_privadas(nombre)

                    while n > 0:

                        clave = input('Introduzca su clave privada para verificar que es usted: ')
                        while not clave.isdecimal():
                            clave = input('ERROR: La clave es numerica, vuelva a intentar: ')

                        if clave_privada == int(clave): 
                            entrar = False
                            print('Usuario verificado correctamente: ')
                            n = 0 

                        else:
                            n -= 1
                            print(f'Clave fallida tiene {n} intentos mas')
                            if n == 0:
                                print('ERROR: Ha superado el limite de intentos')
                                print('')
            else:
                entrar = False
        else: entrar = False
                
    #Pide los limites de la lista de primos y comprueba que los numeros introducidos son validos
    min_primo = input(f"{nombre} introduce el menor primo: ") 
    max_primo = input(f"{nombre} introduce el mayor primo: ")
    while not min_primo.isdecimal() or not max_primo.isdecimal() or int(min_primo) >= int(max_primo):
        min_primo = input(f"ERROR: {nombre} introduce el menor primo: ") 
        max_primo = input(f"ERROR: {nombre} introduce el mayor primo: ")
    
    #Pide los digitos de padding y comprueba que los numeros introducidos son validos
    digitos_padding = input(f"{nombre} el número de dígitos padding: ")
    while not digitos_padding.isdecimal():
        digitos_padding = input(f"ERROR: {nombre} el número de dígitos padding: ")

    #Devulve las variables necesarias
    return nombre, int(min_primo), int(max_primo), digitos_padding


#Funcion que crea los ficheros de claves publicas y privadas 
def crear_ficheros(nombre:str, n:int, e:int, d:int, digitos_padding:str) -> None:

    #Comprueba si exite el directorio usuarios
    if not os.path.exists("Usuarios"):
        #Lo crea en caso de que no sea así
        os.makedirs("Usuarios")

    #Crea el fichero de claves publicas y mete las variables necesarias
    with open(f"Usuarios/pub_{nombre}.txt", 'w') as f:
        f.write(f'{n}\n')
        f.write(f'{e}\n')
        f.write(f'{digitos_padding}\n')

    #Crea el fichero de claves privadas y mete las variables necesarias
    with open(f"Usuarios/priv_{nombre}.txt", 'w') as f:
        f.write(f'{d}\n')


#Comenzamos el main
if __name__ == '__main__':

    #Guardamos los datos de usuario llamando a la funcion
    nombre, min_primo, max_primo, digitos_padding = pedir_datos()

    #Guardamos las claves generadas llamando a la funcion del rsa qeu genera las claves
    n, e, d = rsa.generar_claves(min_primo, max_primo)

    #Cramos los ficheros del usuario
    crear_ficheros(nombre, n, e, d, digitos_padding)

    print(f'{nombre} REGISTRADO CORRECTAMENTE')