def Contar_Temperatura (lista, temperatura):
    repeticiones = 0
    for num in lista:
        if num == temperatura:
            repeticiones += 1
    return repeticiones