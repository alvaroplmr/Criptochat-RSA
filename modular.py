"""
modular.py

Matemática Discreta - IMAT
ICAI, Universidad Pontificia Comillas

Grupo: GPxxx
Integrantes:
    - XX
    - XX

Descripción:
Librería para la realización de cálculos y resolución de problemas de aritmética modular.
"""

from typing import Tuple, List, Dict
import math

class IncompatibleEquationError(Exception):
    pass


""" Reciba un entero n y devuelva verdadero si es un número primo y falso en caso contrario

    Args:
        n (int): Entero
    
    Returns:
        true si el entero es un número primo.
        false en caso contrario.

    Raises: None
    
    Examples:
        es_primo(5)=true
        es_primo(4)=false
"""
def es_primo(n:int) -> bool:
    # si es mas pequeño o igual que 1 no es primo
    if n <= 1:
        return 'NO'
    
    # El 2 y 3 si que son primos 
    if n <= 3:
        return 'SI'
    
    # Si es divisible por 2 o 3 no es primo, esto se hace para quitar tiempo
    if n % 2 == 0 or n % 3 == 0:
        return 'NO'

    # Solo verifica números de la forma 6k ± 1 hasta la raíz cuadrada de n
    for i in range(5, int(n**0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return 'NO' 
    
    return 'SI'  


""" Recibe dos enteros a y b y devuelva la lista de números primos en el intervalo [a, b)

    Args:
        a (int): Elemento inicial del intervalo (incluido)
        b (int): Elemento final del intervalo (no incluido)
    
    Returns:
        List[int]: lista ordenada de primos mayores o iguales que a y menores que b.

    Raises: None
    
    Examples:
        lista_primos(1,11)=[2,3,5,7]
"""
def lista_primos(a: int, b: int) -> List:
    primos = []

    # Si el límite de abajo es mas pequeño o igual que 2, mete el 2 en la lista de primos y pone el limite en tres
    if a <= 2:
        primos.append(2)
        a = 3 
    
    #Si a es par lo combierte en el siguiente impar
    if a % 2 == 0:
        a += 1 
    # verifica si son primos los números impares en el intervalo [a, b)
    for num in range(a, b, 2):
        if es_primo(num) == 'SI':
            primos.append(num)  # Si es primo, lo agrega a la lista de primos
    
    # Si no se encontraron números primos, devuelve "NE"
    if len(primos) == 0:
        return "NE"
    
    return primos  # Retorna la lista de números primos encontrados

    


""" Recibe  un entero n y devuelve un diccionario cuyas claves son los primos que dividen a n y sus valores los
correspondientes exponentes en la descomposición en producto de factores primos de n.
    Args:
        n (int): Entero que se desea factorizar.
    
    Returns:
        Dict[int,int]: Diccionario en el que las claves son primos positivos p_i que dividen a n y, para cada p_i,
            su valor asociado es el máximo exponente e_i tal que p_i^(e_i) divide a n. Si n=0, devuelve un diccionario vacío.

    Raises: None

    Examples
        factorizar(12)={2: 2, 3: 1}
        factorizar(0)={}
"""
def factorizar(n:int) -> Dict:
    factores = {}  

    # Divide n por 2 hasta que ya no sea divisible
    while n % 2 == 0:
        if 2 in factores:
            factores[2] += 1  
        else:
            factores[2] = 1  
        n //= 2 

    # Comprueba los números impares a partir de 3 hasta la raíz cuadrada de n
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0: 
            if i in factores:
                factores[i] += 1  
            else:
                factores[i] = 1 
            n //= i  

    # Si n es mayor que 2 entonces es primo
    if n > 2:
        factores[n] = 1 

    return factores  



""" Calcula el máximo común divisor de dos enteros a y b.
    Args:
        a (int): Primer entero.
        b (int): Segundo entero.
    
    Returns:
        int: devuelve el máximo común divisor de a y b

    Raises: None

    Examples
        mcd(10,15)=5
"""
def mcd(a: int, b: int) -> int:
    # Si b es divisible por a el mcd es a
    if b % a == 0:
        return a
    
    # Si a es divisible por b el mcd es b
    elif a % b == 0:
        return b
    
    # Usamos el algoritmo de Euclides 
    while b != 0:
        a, b = b, a % b  
        
    return a  
        
        
    
        

""" Calcula el máximo común divisor d de dos enteros a y b junto con dos enteros x e y tales que
        d=ax+by

    Args:
        a (int): Primer entero.
        b (int): Segundo entero.
    
    Returns: (d,x,y)
        d (int): Máximo común divisor.
        x (int): Coeficiente de a.
        y (int): Coeficiente de b.

    Raises: None

    Examples
        bezout(6,10)=(2,2,-1)
"""
def bezout(n:int, m:int) -> Tuple[int,int,int]:
    # Inicializa listas para el mcd y los coeficientes de Bezout
    lista0 = [n, m] 
    listan = [1, 0]
    listam = [0, 1]  

    #Pone los valores positivos si no lo son
    if lista0[0] < 0:
        lista0[0] = -lista0[0]
        listan = [-1, 0]
    
    if lista0[1] < 0:
        lista0[1] = -lista0[1]
        listam = [0, -1]
    
    #Usa el algoritmo de Euclides
    while 0 not in lista0:
        if lista0[0] >= lista0[1]:
            #Modifica los coeficientes y el valor de n
            listan[0] -= (lista0[0] // lista0[1]) * listam[0]
            listan[1] -= (lista0[0] // lista0[1]) * listam[1]
            lista0[0] %= lista0[1]
        else:
            #Modifica los coeficientes y el valor de m
            listam[0] -= (lista0[1] // lista0[0]) * listan[0]
            listam[1] -= (lista0[1] // lista0[0]) * listan[1]
            lista0[1] %= lista0[0]

    # Analiza la lista0 y devuleve los valores en una tupla 
    if lista0[0] == 0:
        return (lista0[1], listam[0], listam[1]) 
    else:
        return (lista0[0], listan[0], listan[1]) 
    
        



""" Dada una lista de enteros, devuelve el máximo divisor común a todos ellos.
    Args:
        nList (List[int]): Lista de enteros.        
    
    Returns:
        int: devuelve el máximo entero que divide a todos los enteros de la lista.

    Raises: None

    Examples
        mcd([4,10,14])=2
"""
def mcd_n(nlist:List[int])->int:
    #Opcional
    pass

""" Dada una lista de enteros [a_1,...,a_n], devuelve el máximo divisor común d a todos ellos y una
lista de coeficientes [x_1,...,x_n] tal que
    d=a_1*x_1+...a_n*x_n

    Args:
        nList (List[int]): Lista de enteros.        
    
    Returns: (d,X)
        d (int): Máximo entero que divide a todos los enteros de la lista.
        X (List[int]): Lista de coeficientes [x_1,...,x_n].

    Raises: None

    Examples
        bezout_n([4,10,14])=(2,[-2,1,0])
"""
def bezout_n(nlist:List[int])->Tuple[int,List[int]]:
    #Opcional
    pass

""" Determina si dos enteros son coprimos.
    Args:
        a (int): Primer entero.
        b (int): Segundo entero.
    
    Returns:
        bool: Verdadero si son coprimos y falso si no.

    Raises: None

    Examples
        coprimos(14,20)=false
        coprimos(14,15)=true
"""
def coprimos(n:int,m:int) -> bool:
    if mcd(n, m) == 1:
        return True  # Si el mcd es 1 son coprimos
    else:
        return False  # Si no, no
""" Calcula potencias módulo p.

    Args:
        base (int): Base de la potencia.
        exp (int): Exponente al que se eleva la base.
        p (int): Módulo.
    
    Returns:
        int: Resto de dividir base^exp módulo p.

    Raises:
        ZeroDivisionError: Si el módulo es 0.
"""
def potencia_mod_p(base:int, exp:int, p:int) -> int:
    try:
        # cambia la base para que esté en el rango del módulo
        base = base % p
        resultado = 1  
        exp_fin = abs(exp) 

        # Pone la base positiva si no lo es
        if base < 0:
            base += p
        
        # Usa la exponenciación rápida
        while exp_fin > 0:
            if exp_fin % 2 == 1: 
                resultado = (resultado * base) % p  
            base = (base * base) % p  
            exp_fin //= 2  
        
        # Si el exponente es negativo usa la inversa
        if exp < 0:
            return inversa_mod_p(resultado, p)
        else:
            return resultado  

    except ZeroDivisionError:
        raise ZeroDivisionError("NE") 

""" Calcula la inversa de un número n módulo p.

    Args:
        n (int): Número que se desea invertir
        p (int): Módulo.
    
    Returns:
        int: Entero x entre 0 y p-1 tal que n*x es congruente con 1 módulo p.

    Raises:
        ZeroDivisionError: Si el módulo es 0 o si n no es invertible módulo p.
"""
def inversa_mod_p(n:int, p:int) -> int:
    try:
        #Usamos el algoritmo de Bezout para calcular el máximo común divisor (mcd) y los coeficientes
        d, x0, y0 = bezout(n, p)

        #Sabemos que si el mcd no es 1 no tiene inversa modular con modulo p
        if d != 1:
            raise ZeroDivisionError

        # Si el mcd es 1 entonces el resto de dividir x0 entre p es la inversa
        return x0 % p

    except ZeroDivisionError:
        raise ZeroDivisionError("NE") 

""" Calcula la función phi de Euler de un entero positivo n, es decir, cuenta cúantos enteros positivos
menores que n son coprimos con n.

    Args:
        n (int): Número entero positivo.
    
    Returns:
        int: Función phi de Euler de n.

    Raises: None
"""
def euler(n:int) -> int:
    # Saca los factores de n
    factores_primos = factorizar(n)  
    resultado = n  

    # Calcula euler 
    for primo in factores_primos:
        # Cambia el resultado segun la formula para cada primo 
        resultado = resultado * (primo - 1) // primo
    
    return resultado 

""" Dado un entero n y un número primo p, calcula el símbolo de Legendre de n módulo p.

    Args:
        n (int): Número entero.
        p (int): Número primo.
    
    Returns:
        int: Símbolo de Legendre de Euler de n módulo p:
            0 si es múltiplo de p
            1 si es un cuadrado perfecto (distinto de 0), módulo p
            -1 en caso contrario.

    Raises:
        ZeroDivisionError: Si el módulo p es 0.
"""
def legendre(n:int,p:int) -> int:
    try:
        #Si p es menor no existe legendre, ya que trabaja con primos mayores que dos 
        if p <= 2:
            raise ZeroDivisionError("p debe ser mayor que 2.")
        
        #Si el resto de n entre p es 0 el símbolo de Legendre es 0
        if n % p == 0:
            return 0 
        
        #Utiliza la exponenciación rápida
        legendre_symbol = potencia_mod_p(n, (p - 1) // 2, p)
        
        #Si da lo mismo que p - 1 entinces devuelve -1
        if legendre_symbol == p - 1:
            return -1 
        
        #Si no devuelve el resultado del símbolo de Legendre
        return legendre_symbol 
            
    except ZeroDivisionError as error:
        raise ZeroDivisionError(error)  

""" Dadas tres listas de números enteros [a_1,...,a_n], [b_1,...,b_n] y [p_1,...,p_n], resuelve el sistema de congruencias
    
    a_i * x = b_i (mod p_i)   i=1,...,n
    
    devolviendo un entero r y un módulo m tales que las soluciones del sistema corresponden a todos los enteros
    x congruentes con r módulo m.

    Args:
        alist (List[int]): Lista de coeficientes de la variable x, [a_1,...,a_n].
        blist (List[int]): Lista de términos independientes [b_1,...,b_n].
        plist (List[int]): Lista de módulos [p_1,...,p_n]
    
    Returns: (r,m)
        r (int): Entero entre 0 y m-1.
        m (int): Entero positivo, módulo de la solución.

    Raises:
        IncompatibleEquationError: Si no es posible resolver el sistema.
"""
def resolver_sistema_congruencias(alist: List[int], blist: List[int], plist: List[int]) -> Tuple[int, int]:
    n = len(alist)  # Número de ecuaciones en el sistema
    try:
        M = 1
        #Esto calcula el producto total de los módulos
        for p in plist:
            M *= p

        r = 0  
        for k in range(n):
            a_k = alist[k]
            b_k = blist[k]
            p_k = plist[k]

            N = M // p_k

            #Hacemos la inversa de N_k y de a_k con p_k
            N_inv = inversa_mod_p(N, p_k)
            a_k_inv = inversa_mod_p(a_k, p_k)

            # Si no existe inversa salta la excepcion
            if type(a_k_inv) == ZeroDivisionError or type(N_inv) == ZeroDivisionError:
                raise IncompatibleEquationError

            r_k = (a_k_inv * b_k * N_inv) % p_k

            r = (r + r_k * N) % M
            
        return r, M

    except IncompatibleEquationError:
        raise IncompatibleEquationError("NE")


""" Encuentra, si existe, una raíz cuadrada para un entero n módulo un número primo p.

    Args:
        n (int): Entero del que se desea hallar la raíz.
        p (int): Módulo. Se asume que es un número primo.
    
    Returns:
        int: Entero x entre 0 y p-1 tal que x^2 = n (mod p).

    Raises:
        IncompatibleEquationError: Si no es posible hallar dicha raíz.
"""
def raiz_mod_p(n:int,p:int)->int:
    #Opcional
    pass

""" Halla, si es posible, las dos posibles soluciones de la ecuación cuadrática ax^2+bx+c=0 (mod p).
Devuelve una tupla con las dos raíces (distintas o una misma raíz repetida en caso de ser doble).

    Args:
        a (int): Coeficiente de x^2.
        b (int): Coeficiente de x.
        c (int): Término independiente.
        p (int): Módulo. Se asume que es un número primo.
    
    Returns: (x1,x2)
        x1 (int): Primera solución. Entero entre 0 y p-1.
        x2 (int): Segunda solución. Entero entre 0 y p-1.

    Raises:
        IncompatibleEquationError: Si no es posible resolver la ecuación.
"""
def ecuacion_cuadratica(a:int,b:int,c:int,p:int)->Tuple[int,int]:
    #Opcional
    pass