def Ordenar_Temp (lista):
    for i in range(1, len(lista)):
        for j in range(0, len(lista)-1):
            if lista[j] > lista[j+1]:
                Aux = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = Aux
    return lista