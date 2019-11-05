"""Escribe un programa que te pida primero un número y luego te pida números
hasta que la suma de los números introducidos coincida con el número inicial.
El programa termina escribiendo la lista de números."""
#Francisco Llamas
lista=[]
limite=int(input("introduzca el limite"))
suma=0

while suma<limite:
    numero=int(input("escriba otro numero"))
    lista.append(numero)
    suma=numero+suma
    if suma>limite:
        print("el número", numero,"es demasiado grande.")
        

    elif suma==limite:
        print("El límite a alcanzar es", limite,"La lista creada es", lista)
