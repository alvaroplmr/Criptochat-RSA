# Sistema de Cifrado RSA en Python con Aritmética Modular

Este proyecto implementa un sistema de cifrado basado en el algoritmo RSA desarrollado desde cero en Python. Incluye la generación de claves públicas y privadas, cifrado y descifrado de mensajes, un sistema básico de padding y una demostración de ataque sobre RSA sin padding.

El núcleo del proyecto consiste en la implementación manual de los fundamentos matemáticos que sustentan RSA (aritmética modular, algoritmo extendido de Euclides, exponenciación modular eficiente, etc.) y su aplicación en un entorno interactivo de consola tipo "chat cifrado".

El código está organizado en varios módulos que permiten generar claves, registrar usuarios, cifrar y descifrar mensajes, así como analizar vulnerabilidades cuando no se utiliza padding criptográfico seguro.

---

## Estructura del proyecto

El repositorio contiene los siguientes archivos:

- **criptochat.py**  
  Script principal. Gestiona la interacción con el usuario, permite cifrar y descifrar mensajes entre usuarios y ejecutar el ataque sobre el criptograma de ejemplo.

- **rsa.py**  
  Implementación del algoritmo RSA:
  - Generación de claves (n, e, d)
  - Cifrado y descifrado de enteros
  - Cifrado y descifrado de cadenas de texto
  - Ataque de texto claro elegido para el caso sin padding

- **modular.py**  
  Implementación de funciones de teoría de números y aritmética modular:
  - Cálculo del máximo común divisor
  - Algoritmo extendido de Euclides
  - Inverso modular
  - Exponenciación modular eficiente
  - Utilidades relacionadas con números primos

- **registrarusuario.py**  
  Script para generar usuarios y almacenar sus claves en la carpeta `Usuarios/`.

- **Criptograma_X.txt**  
  Archivo que contiene una clave pública y un mensaje cifrado utilizado para demostrar el ataque sin padding.

- **Usuarios/**  
  Carpeta donde se almacenan las claves públicas y privadas generadas.

---

## Requisitos

El proyecto utiliza únicamente Python estándar y no requiere dependencias externas.

sys
typing (List, Tuple, Dict)
os
math
random

---

## Autores

[@alvaroplmr](https://github.com/alvaroplmr)  
[@pablordgzglez](https://github.com/pablordgzglez)
