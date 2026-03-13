def statistics():
    """
    Ejercicio 5 - Estadísticas Simples

    Dados cuatro números, calcular e imprimir:
    1. El promedio
    2. El máximo
    3. El mínimo
    4. El rango (diferencia entre máximo y mínimo)
    """
    num1 = 15
    num2 = 8
    num3 = 23
    num4 = 12
    print((num1 + num2 + num3 + num4) / 4)
    max_1 = max(num1, num2, num3, num4)
    print(max_1)
    min_1 = min(num1, num2, num3, num4)
    print(min_1)
    print(max_1 - min_1)
statistics()