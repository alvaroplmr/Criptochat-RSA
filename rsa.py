"""
rsa.py

Matemática Discreta - IMAT
ICAI, Universidad Pontificia Comillas

Grupo: GPxxx
Integrantes:
    - XX
    - XX

Descripción:
Librería para la realización de cifrado y descifrado usando el algoritmo RSA.
"""
import modular
from typing import Tuple,List
import random

def generar_claves(min_primo:int,max_primo:int)-> Tuple[int,int,int]:
    """Toma dos primos entre min_primo (incluido) y max_primo (excluido) y devuelve
    n,e,d
    donde (n,e) es la clave pública y d la clave privada para RSA

    Args:
        min_primo (int): Límite inferior para los primo p1 y p2 usados en la clave
        max_primo (int): Límite superior para los primo p1 y p2 usados en la clave
    
    Returns:
        n (int): Módulo para RSA, formado por el producto de dos primos p1 y p2 tales que
            min_primo<=p1, p2 < max_primo
        e (int): Exponente de la clave pública para RSA con módulo n=p1*p2
        d (int): Exponente de la clave privada para RSA con módulo n

    Raises: None
    """
    #Genera la lísta de primos entre los límites introducidos por el usuario
    primos = modular.lista_primos(min_primo, max_primo + 1)

    #Elige el primer primo al azar de la lísta de primos
    primo1 = random.choice(primos)
    primos.remove(primo1)

    #Elige el segundo primo al azar de la lísta de primos
    primo2 = random.choice(primos)

    #Genera la n multiplicando los primos
    n = primo1 * primo2

    #Como sabemos que los dos números son primos podemos sacar el euler directamente con esta fórmula
    eulern = (primo1 - 1) * (primo2 - 1)

    #Sacamos un número mayor que 2 que sea coprimo con el euler de n
    for i in range(2, eulern):
        if modular.coprimos(eulern, i):
            e = i
            break

    #Genera la clave privada 
    d = modular.inversa_mod_p(e, eulern)

    return (n, e, d)


def aplicar_padding(m:int,digitos_padding:int)->int:
    """Dado un mensaje y un número de dígitos de padding, añade
    digitos_padding cifras aleatorias a la derecha del mensaje
    
    Args:
        m (int): Mensaje sin padding
        digitos_padding (int): Número no negativo de cifras de padding
    
    Returns:
        int: entero formado por los dígitos de m seguidos de digitos_padding cifras aleatorias.

    Raises: None

    Example:
        aplicar_padding(24,2)=2419
        aplicar_padding(24,2)=2403
        aplicar_padding(24,3)=24718
        aplicar_padding(24,3)=24845
    """
    #Pasamos el valor de padding a str para ponder introducir dígitos
    m = str(m)
    for i in range(digitos_padding):
        #Añade el dígito aleatorio
        m += str(random.randint(0, 9))
    #Devuelve el número con padding en int
    return int(m)



def eliminar_padding(m:int,digitos_padding:int)->int:
    """Dado un mensaje con padding de digitos_padding cifras al
    final del mismo, elimina dichas cifras aleatorias y devuelve
    el resto de cifras del mensaje

    Args:
        m (int): Mensaje con padding
        digitos_padding (int): Número no negativo de cifras de padding
    
    Returns:
        int: entero resultante de eliminar las últimas digitos_padding cifras de m.

    Raises: None
    
    Example:
        aplicar_padding(2454,1)=245
        aplicar_padding(2454,2)=24
        aplicar_padding(2454,3)=2
        aplicar_padding(2432,2)=24
    """
    #Elimina los dígitos de padding si el padding es diferente que 0
    if digitos_padding != 0:
        return int(str(m)[:-digitos_padding])  
    return m
    


def cifrar_rsa(m:int,n:int,e:int,digitos_padding:int)->int:
    """Dado un mensaje m entero, un módulo y exponente que formen parte
    de una clave pública de RSA, con m<n*10^{-digitos_padding}, y un número
    de dígitos de padding, aplica el padding al mensaje y lo cifra
    usando RSA con módulo n y exponente e.
    
    Args:
        m (int): Mensaje original claro (sin padding)
        n (int): Módulo de la clave pública de RSA
        e (int): Exponente de la clave pública de RSA
        digitos_padding (int): Número no negativo de cifras de padding
    
    Returns:
        int: entero resultante de agregar el padding a m y aplicar RSA.

    Raises: None
    """
    #Aplicamos el padding
    mensaje_padding = aplicar_padding(m, digitos_padding)

    #Devolvemos el número cifrado
    return modular.potencia_mod_p(mensaje_padding, e, n)



def descifrar_rsa(c:int,n:int,d:int,digitos_padding:int)->int:
    """Dado un cifrado c entero que haya sido cifrado con RSA usando
    digitos_padding cifras de padding al final del mensaje y el 
    módulo y exponente privado, n y d que formen la clave privada de RSA cuya pareja se
    utilizó para cifrar c, descifra c y elimina el padding, devolviendo
    el mensaje original.

    Args:
        c (int): Mensaje original claro (sin padding)
        n (int): Módulo de la clave pública de RSA usado para cifrar
        d (int): Exponente de la clave privada de RSA cuya pareja se utilizó para cifrar c
        digitos_padding (int): Número no negativo de cifras de padding usados para cifrar c
    
    Returns:
        int: entero resultante de descifrar c usando RSA con módulo m y exponente e y después eliminar el padding al resultado.

    Raises: None
    """
    #Desciframos el número
    numero_descifrado = modular.potencia_mod_p(c, d, n)
    
    #Devolvemos el número descifrado pero sin padding
    return eliminar_padding(numero_descifrado, digitos_padding)

def codificar_cadena(s:str)->List[int]:
    """Convierte una cadena de caracteres a la lista de
    enteros que representa el valor unicode cada uno de sus caracteres.

    Args:
        s (str): cadena en texto plano

    Returns:
        int: lista de enteros que representan el código unicode de cada carácter de la cadena s.

    Raises: None.

    Example:
        codificar_cadena("¡Hola mundo!")=[161, 72, 111, 108, 97, 32, 109, 117, 110, 100, 111, 33]
    """
    #Creamos la lista 
    lista = []

    #Para cada caracter de la cadena lo pasamos a su numero en ASCI y lo introducimos en la lista
    for i in s:
        lista.append(ord(i))
    
    #Devolvemos la lista
    return lista


def decodificar_cadena(m:List[int])->str:
    """Convierte una lista de enteros que representen caracteres unicode
    en la cadena que representan.
    
    Args:
        m (List[int]): lisa de enteros que representan los códigos unicode de una cadena de caracteres.
    
    Returns:
        str: cadena que representan

    Raises:
        ValueError: Si alguno de los enteros no representa un caracter unicode válido.
    
    Example:
        decodificar_cadena([161, 72, 111, 108, 97, 32, 109, 117, 110, 100, 111, 33])="¡Hola mundo!"
    """
    #Creamos la variable str donde introduciremos la cadena
    str_resuelta = ''

    #Para cada número de la lista lo pasamos a su caracter ASCI y lo metemos en la cadena str
    for numero in m:
        #Comprobamos con una excepción que para ese número existe un caracter en ASCI
        try:
            str_resuelta += chr(numero)
        except ValueError:
            #Printeamos el error
            raise ValueError(f'ERROR: {numero} no representa un caracter unicode válido')
        
    #Devolvemos la cadena
    return str_resuelta

def cifrar_cadena_rsa(s:str,n:int,e:int,digitos_padding:int)->List[int]:
    """Cifra carácter a carácter una cadena de caracteres usando RSA con clave púbica (n,e)
    y digitos_padding cifras de padding al final del mensaje y devuelve la lista de enteros
    que representan el mensaje cifrado correspondiente.
    Args:
        s (str): texto claro
        n (int): módulo para RSA
        e (int): clave pública para RSA
        digitos_padding (int): número no negativo de dígitos de padding que deben usarse para el cifrado del mensaje.
    
    Returns:
        List[int]: lista de enteros que representa el mensaje cifrado con RSA para la clave dada.

    Raises: None
    """
    #LLamamos a al función codificar para pasar la cadena a una lista con número ASCI
    lista = codificar_cadena(s)

    #Creamos la lista para introducir los valores cifrados
    lista_cifrada = []

    #Para cada número de la lista llamamos a la función cifrar_rsa para que le añada el padding y lo cifre
    for numero in lista:
        lista_cifrada.append(cifrar_rsa(numero, n, e, digitos_padding))

    #Develvemos la lista cifrada
    return lista_cifrada 


def descifrar_cadena_rsa(cList:List[int],n:int,d:int,digitos_padding:int)->str:
    """Dado un mensaje cifrado con RSA usando la clave pública cuya clave privada asociada es (n,d)
    y digitos_padding cifras de padding al final del mensaje, devuelve la cadena orignal.
    Args:
        cList (List[int]): lisa de enteros que representan el mensaje cifrado
        n (int): módulo para RSA
        d (int): clave privada para RSA
        digitos_padding (int): número no negativo de dígitos de padding usados para el cifrado de cList.
    
    Returns:
        str: cadena que representa el texto claro correspondiente al mensaje cifrado cList.

    Raises:
        ValueError: Si, tras decodificar, alguno de los enteros del mensaje no representa un caracter unicode válido.    
    """
    #Creamos la lista_numeros para introducir los números descrifrados 
    lista_numeros = []

    #Para cada número de la lista introducida lo descrifra y le quita el padding
    for numero in cList:
        lista_numeros.append(descifrar_rsa(numero, n, d, digitos_padding))
    
    #Pasa la lista de números desciframos a sus caracteres ASCI y comprueba que existe con una excepción
    try:
        cadena_original = decodificar_cadena(lista_numeros)
    except ValueError as error:
        raise ValueError(error)
    
    #Devulve la cadena descifrada 
    return cadena_original


def romper_clave(n:int,e:int)->int:
    """A partir de una clave pública válida (n,e), recupera la clave privada d tal que
    de = 1 (mod phi(n)).
    
    Args:
        n (int): módulo para RSA
        e (int): clave pública para RSA
    
    Returns:
        int: clave privada d

    Raises:
        ValueError: Si no existe ninguna clave privada d compatible con la clave pública (n,e).
    """
    #Calculamos la clave privada a partir de las claves públicas de otro usuario y comprueba con una excepción que existe la inversa de n mod(eulern)
    try:
        d = modular.inversa_mod_p(e, modular.euler(n))
    except ZeroDivisionError:
        raise ValueError(f"ERROR: No existe ninguna clave privada d compatible con la clave pública ({n}, {e})")
    
    #Devulve la clave privada
    return d



def ataque_texto_elegido(cList:List[int],n:int,e:int)->str:
    """Ejecuta un ataque de texto claro elegido sobre un mensaje que ha sido cifrado
    con RSA plano sin usar padding a partir de su clave pública.

    Args:
        cList (List[int]): lisa de enteros que representan el mensaje cifrado
        n (int): módulo para RSA
        e (int): clave pública para RSA
    
    Returns:
        str: texto plano descifrado para el mensaje cifrado cList

    Raises:
        ValueError: Si el mensaje no se corresponde con ningún texto plano que haya sido codificado con RSA sin padding.
    """

    dic_valores = {}
    #Hay 255 valores ASCII en el alfabeto estándar, incluyendo los posibles caracteres con tildes
    for i in range(255): 
        #Ciframos cada valor del ASCII según la n y la e dadas y las metemos como claves de diccionario
        cifrado = modular.potencia_mod_p(i, e, n) 
        #Asignamos a cada clave su valor real
        dic_valores[cifrado] = chr(i) 
    mensaje = ""

    #Asignamos a cada número de la lista su valor real gracias al diccionario y, si alguno de ellos no se encuentra en el diccionario
    #significará que no se corresponde con ningún carácter que haya sido codificado con RSA sin padding y será necesario capturar el error
    for i in cList:
        try:
            mensaje += dic_valores[i]
        except KeyError:
            raise ValueError(f"El caracter {i} no se corresponde con ninguno que haya sido codificado con RSA sin padding")

    return mensaje