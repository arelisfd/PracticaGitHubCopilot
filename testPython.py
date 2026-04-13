"""
Módulo de operaciones matemáticas básicas.
Ejemplos de uso de GitHub Copilot para Python.
"""

from typing import List, Union


def calculate_average(numbers: List[Union[int, float]]) -> float:
    """
    Calcula el promedio de una lista de números.

    Args:
        numbers: Lista de números enteros o flotantes.

    Returns:
        El promedio de los números.

    Raises:
        ValueError: Si la lista está vacía.
    """
    if not numbers:
        raise ValueError("La lista de números no puede estar vacía")
    return sum(numbers) / len(numbers)


def multiply_numbers(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Multiplica dos números e imprime el resultado.

    Args:
        a: Primer número.
        b: Segundo número.

    Returns:
        El producto de a y b.
    """
    resultado = a * b
    print(f"Multiplicación: {a} × {b} = {resultado}")
    return resultado


def sumar_y_multiplicar(a: Union[int, float], b: Union[int, float]) -> dict:
    """
    Suma y multiplica dos números e imprime ambos resultados.

    Args:
        a: Primer número.
        b: Segundo número.

    Returns:
        Diccionario con las claves 'suma' y 'multiplicacion'.
    """
    suma = a + b
    multiplicacion = a * b
    print(f"La suma es: {suma} y la multiplicación es: {multiplicacion}")
    return {"suma": suma, "multiplicacion": multiplicacion}


def divide_numbers(a: Union[int, float], b: Union[int, float]) -> float:
    """
    Divide dos números e imprime el resultado.

    Args:
        a: Dividendo.
        b: Divisor.

    Returns:
        El resultado de la división.

    Raises:
        ValueError: Si b es cero.
    """
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    resultado = a / b
    print(f"División: {a} ÷ {b} = {resultado}")
    return resultado


if __name__ == "__main__":
    # Ejemplos de uso de cada función
    print("=== Ejemplos de uso ===\n")

    # Promedio
    print("1. Promedio:")
    promedio = calculate_average([10, 20])
    print(f"Promedio de [10, 20]: {promedio}\n")

    # Multiplicación
    print("2. Multiplicación:")
    multiply_numbers(5, 4)
    print()

    # Suma y multiplicación
    print("3. Suma y Multiplicación:")
    sumar_y_multiplicar(5, 4)
    print()

    # División
    print("4. División:")
    divide_numbers(20, 4)
