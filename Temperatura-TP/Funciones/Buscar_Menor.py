def buscar_menor (lista):
    temperatura_menor = 0
    for temperatura in lista:
        if temperatura < temperatura_menor or temperatura_menor == 0:
            temperatura_menor = temperatura
    return temperatura_menor