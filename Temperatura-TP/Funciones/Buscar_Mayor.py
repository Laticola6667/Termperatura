def buscar_mayor (lista):
    temperatura_maxima = 0
    for temperatura in lista:
        if temperatura > temperatura_maxima:
            temperatura_maxima = temperatura
    return temperatura_maxima