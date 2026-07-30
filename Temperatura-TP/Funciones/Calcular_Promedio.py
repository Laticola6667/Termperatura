def calcular_promedio (lista):
    suma_total = 0
    for temperatura in lista:
        suma_total += temperatura
    return suma_total / len(lista)