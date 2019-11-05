"""Escribe un programa que pida un número (límite) y luego te pida números
hasta que la suma de los números introducidos supere el límite inicial.
El programa termina escribiendo la lista de números."""
#Francisco Llamas
lista=[]
limite=int(input("introduzca el limite"))
suma=0

while suma<limite:
    numero=int(input("escriba otro numero"))
    lista.append(numero)
    suma=numero+suma

print("El limite a superar es", limite,"La lista creada es", lista,"y la suma de los numeros es:", suma)




    
