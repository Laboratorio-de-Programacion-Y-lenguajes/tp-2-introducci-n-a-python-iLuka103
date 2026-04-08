# ============================================================
# MÓDULO 7: Operaciones con Strings
# ============================================================


def es_palindromo(texto: str) -> bool:
    """
    Retorna True si el texto es palíndromo (ignorando espacios y mayúsculas).
    Ejemplo: es_palindromo("Anita lava la tina") -> True
    """
    texto_crudo = texto.lower().replace(" ", "")
    return texto_crudo == texto_crudo[::-1]
    pass


def capitalizar_palabras(texto: str) -> str:
    """
    Capitaliza la primera letra de cada palabra.
    Ejemplo: capitalizar_palabras("hola mundo") -> "Hola Mundo"
    """
    palabras = texto.split()
    palabras_capitalizadas = [p.capitalize() for p in palabras]
    
    return " ".join(palabras_capitalizadas)
    pass


def contar_vocales(texto: str) -> int:
    """
    Retorna la cantidad de vocales (a,e,i,o,u) en el texto,
    sin distinguir mayúsculas/minúsculas.
    """
    vocales = "aeiou"
    return sum(1 for caracter in texto.lower() if caracter in vocales)
    pass


def caesar_cipher(texto: str, desplazamiento: int) -> str:
    """
    Aplica el cifrado César al texto con el desplazamiento dado.
    Solo desplaza letras (a-z, A-Z), los demás caracteres no cambian.
    Ejemplo: caesar_cipher("abc", 1) -> "bcd"
    """
    resultado = ""
    
    for caracter in texto:
        if caracter.isalpha():
            base = ord('A') if caracter.isupper() else ord('a')
            nuevo_codigo = (ord(caracter) - base + desplazamiento) % 26 + base
            resultado += chr(nuevo_codigo)
        else:
            resultado += caracter
            
    return resultado
    pass
