# CriptoChat (RSA + Aritmética modular)

Proyecto en Python que implementa **RSA** (cifrado/descifrado), junto con una librería de **aritmética modular**. Incluye:

- Generación de claves RSA (públicas y privadas)
- Cifrado y descifrado de **cadenas de texto** carácter a carácter (Unicode → enteros)
- Soporte de **padding** (añade dígitos aleatorios al final de cada carácter antes de cifrar)
- Un módulo de “**ataque de texto claro elegido**” (para el caso RSA *sin padding*)
- Programas de consola para registrar usuarios y “chatear” cifrando/descifrando

---

## Estructura del proyecto

- `modular.py`  
  Funciones de aritmética modular: primos, factorización, Bezout, inversas modulares, potencia modular, Euler, etc.

- `rsa.py`  
  Implementación de RSA:
  - `generar_claves(min_primo, max_primo)` → `(n, e, d)`
  - `cifrar_rsa(...)` / `descifrar_rsa(...)`
  - `cifrar_cadena_rsa(...)` / `descifrar_cadena_rsa(...)`
  - `ataque_texto_elegido(...)` (ataque para RSA **sin padding**)

- `registrarusuario.py`  
  Crea usuarios y guarda sus claves en ficheros dentro de `Usuarios/`:
  - `Usuarios/pub_<nombre>.txt` (n, e, dígitos de padding)
  - `Usuarios/priv_<nombre>.txt` (d)

- `criptochat.py`  
  Programa principal de consola:
  - Cifrar con la clave pública del otro usuario
  - Descifrar con la clave privada del usuario 1
  - Opción `X` para descifrar el criptograma de `Criptograma_X.txt` usando el ataque

- `Criptograma_X.txt`  
  Fichero con una clave pública y un mensaje `X` cifrado (pensado para el ataque sin padding).

- `P2GP12.pdf`  
  Documento del enunciado/entrega (si aplica al contexto académico).

---

## Autores
[@alvaroplmr](https://github.com/alvaroplmr)
[@pablordgzglez](https://github.com/pablordgzglez)
