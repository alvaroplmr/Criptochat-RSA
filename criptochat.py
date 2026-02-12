#Importamos la librerias necesarias
import sys
import rsa 
from typing import List

#Función que saca del fichero las claves públicas del usuario
def coger_calves_publicas(nombre:str) -> List[int]:
    #Abrimos el fichero
    fichero_publico = open(f"Usuarios/pub_{nombre}.txt", 'r')

    #Leemos las líneas y las guardamos en una lista
    datos = fichero_publico.readlines()

    #Cerramos el fichero
    fichero_publico.close

    #Limpiamos la lista
    for i in range(len(datos)):
        datos[i] = int(datos[i].strip())

    #Devolvemos las claves públicas
    return datos

#Función que saca del fichero la clave privada del usuario
def coger_claves_privadas(nombre:str) -> int:
    #Abrimos el fichero
    fichero_privado = open(f"Usuarios/priv_{nombre}.txt", 'r')

    #Leemos la única linea y la limpiamos
    d = int(fichero_privado.readline().strip())

    #Cerramos el fichero
    fichero_privado.close()

    #Devolvemos la clave privada
    return d
    

#Función que pide la opción a ejecutar al usuario
def pedir_opcion() -> str:

    #Printeamos el menú con las opciones a elgir
    print('**********OPCIONES**********')
    print('*                          *')
    print('*        [C]ifrar          *')
    print('*        [D]escifrar       *')
    print('*        [S]alir           *')
    print('*        [X]Cadena         *')
    print('*                          *')
    print('****************************')

    #Pedimos la opción y comprobamos que este dentro de las opciones válidas
    opcion=input("Introduce una opción: ")
    while opcion.upper() != 'C' and opcion.upper() != 'D' and opcion.upper() != 'S' and opcion.upper() != 'X':
        opcion=input("ERROR: Introduce una opción: ")

    #Devolvemos las opción
    return opcion


#Función que pide el mensaje y lo cifra con las claves introducidas
def cifrar_texto(n_usuario2:int, e_usuario2:int, digitos_padding_usuario2:int):

    #Pedimos la cadena
    cadena = input("Introduce el texto que deseas cifrar: ")

    #Printeamos la lista cifrada y capturamos los errores
    try:
        mensaje_cifrado = rsa.cifrar_cadena_rsa(cadena, n_usuario2, e_usuario2, digitos_padding_usuario2)
        cadena_cifrada = ''
        for numero in mensaje_cifrado:
            cadena_cifrada += str(numero) + ' '
        print('---------------------------------------------------------')
        print(cadena_cifrada)
        print('---------------------------------------------------------')
    except ValueError as error:
        print(error)

#Función que pide un str con los valores cifrados separados por un espacio
def descifrar_texto(n_usuario1:int, d_usuario1:int, digitos_padding_usuario1:int):

    #Pide la cadena y la mete cada valor cifrado en una lista 
    cadena_cifrada = input("Introduce la lista que deseas descifrar: ").split(' ')

    #Para cada valor de la lista lo pasa a int
    for i in range(len(cadena_cifrada)):
        cadena_cifrada[i] = int(cadena_cifrada[i])
    
    #Desciframos el mensaje y capturamos los errores
    try:
        print('---------------------------------------------------------')
        print(rsa.descifrar_cadena_rsa(cadena_cifrada, n_usuario1, d_usuario1, digitos_padding_usuario1))
        print('---------------------------------------------------------')
    except ValueError as error:
        print(error)

def ataque_texto_elegido():
    #Abrimos el fichero donde se encuentran los datos y leemos sus líneas en una lista
    fichero = open(f"Criptograma_X.txt", 'r')
    lista = fichero.readlines()
    fichero.close()
    
    #Sacamos el mesaje del txt que equivale a la tercera línea y pasamos sus números a int
    X = lista[3].split()
    for i in range(len(X)):
        X[i] = int(X[i])

    #Sacamos la n y e que se encuentran en la primera línea
    lista[0] = lista[0].strip()
    es_numero = False
    cadena_claves = ''
    for i in range(len(lista[0])):
        if lista[0][i].isdecimal() or es_numero == True:
            es_numero = True
            cadena_claves += lista[0][i]
    lista_claves = cadena_claves.split()
    n = int(lista_claves[0])
    e = int(lista_claves[1])

    #Desciframos el mensaje y campturamos los errores
    try:
        print('---------------------------------------------------------')
        print(rsa.ataque_texto_elegido(X, n, e))
        print('---------------------------------------------------------')
    except ValueError as error:
        print(error)



#Inicializamos el main
if __name__ == "__main__":

    #Cogemos los argumentos metidos en la terminal
    argumentos = sys.argv

    #Comprobamos que el número de argumento es 3 
    if len(argumentos) == 3:

        #Sacamos los nombres de los usuarios
        usuario1, usuario2 = argumentos[1], argumentos[2] 

        #Sacamos las claves públicas de cada usuario
        n_usuario1, e_usuario1, digitos_padding_usuario1 = coger_calves_publicas(usuario1)
        n_usuario2, e_usuario2, digitos_padding_usuario2 = coger_calves_publicas(usuario2)

        #Sacamos la clave privada del primer usuario
        d_usuario1 = coger_claves_privadas(usuario1)

        #Inicializamos la variable opción para que entre en el bucle 
        opcion = ""
        while opcion.upper() !="S":

            #Pedimos la opción 
            opcion = pedir_opcion()

            #Si la opción es cifrar llama a la función cifrar texto
            if opcion.upper() == "C":
                cifrar_texto(n_usuario2, e_usuario2, digitos_padding_usuario2)
            
            #Si la opción es descifrar llama a la función descifrar texto 
            if opcion.upper() == "D":
                descifrar_texto(n_usuario1, d_usuario1, digitos_padding_usuario1)
            
            if opcion.upper() == 'X':
                ataque_texto_elegido()
        
        #Si la opción es salir se sale del programa
        print("¡Hasta pronto!")
    
    #Si los argumentos son 1 entonces la única opción será atacar el mensaje X
    elif len(argumentos) == 1:
        opcion2 = input('Tu uncica opcion es descrifar el mensaje X, ¿desea hacerlo? (SI,NO)')
        if opcion2.upper() == 'SI':
            ataque_texto_elegido()
        else:
            print('¡HASTA PRONTO!')
    else:
        print('ARGUMENTOS NO VALIDOS')
