# ============================================================
# MÓDULO 3: Listas
# ============================================================


def suma_lista(numeros: list) -> int | float:
    """
    Retorna la suma de todos los elementos de la lista.
    """
    return sum(numeros) 
    pass


def filtrar_pares(numeros: list) -> list:
    """
    Retorna una nueva lista con solo los números pares.
    """
    return [n for n in numeros if n % 2 == 0]
    pass


def invertir_lista(lista: list) -> list:
    """
    Retorna la lista invertida SIN modificar la original.
    """
    return lista[::-1]
    pass


def eliminar_duplicados(lista: list) -> list:
    """
    Retorna una nueva lista sin elementos duplicados,
    manteniendo el orden de primera aparición.
    """
    nueva_lista = []
    for elemento in lista:
        if elemento not in nueva_lista:
            nueva_lista.append(elemento)
    return nueva_lista
    pass


def aplanar_lista(lista: list) -> list:
    """
    Dada una lista de listas, retorna todos los elementos en una sola lista.
    Ejemplo: aplanar_lista([[1,2],[3,4]]) -> [1, 2, 3, 4]
    """
    return [item for sublista in lista for item in sublista]
    pass
