from Funciones.Agregar_Temp import agregar_temperatura
from Funciones.Buscar_Mayor import buscar_mayor
from Funciones.Buscar_Menor import buscar_menor
from Funciones.Calcular_Promedio import calcular_promedio
from Funciones.Contar_Temperatura import Contar_Temperatura
from Funciones.Mostrar_Temp import mostrar_temperatura
from Funciones.Ordenar_Temp import Ordenar_Temp

temperaturas = []

while True:
    print("\t\tMenú:")
    print("\t1- Agregar Temperatura")
    print("\t2- Mostrar Temperatura")
    print("\t3- Calcular Promedio")
    print("\t4- Buscar Mayor")
    print("\t5- Buscar Menor")
    print("\t6- Contar Temperaturas")
    print("\t7- Ordenar Temperaturas")
    print("\t8- Salir\n")
    opcion = int(input("Opción:\t"))
    if opcion in [1,2,3,4,5,6,7,8]:
        if opcion == 1:
            agregar_temperatura(temperaturas, int(input("Temperatura a agregar:\t")))
        elif opcion == 2:
            mostrar_temperatura(temperaturas)
        elif opcion == 3:
            print("Promedio Total: ",calcular_promedio(temperaturas))
        elif opcion == 4:
            print("Temperatura Mayor: ",buscar_mayor(temperaturas))
        elif opcion == 5:
            print("Temperatura Menor: ",buscar_menor(temperaturas))
        elif opcion == 6:
            temperatura_a_buscar = int(input("Ingrese la temperatura a buscar"))
            print(f"{temperatura_a_buscar}° se ha encontrado {Contar_Temperatura(temperaturas, temperatura_a_buscar)}")
        elif opcion == 7:
            temperaturas = Ordenar_Temp(temperaturas)
            print("Se han ordenado las temperaturas: ", temperaturas)
        elif opcion == 8:
            break