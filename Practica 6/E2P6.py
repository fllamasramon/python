"""Escribe un programa que te pida números y los guarde en una lista.
Para terminar de introducir número, simplemente escribe “Salir”.
El programa termina escribiendo la lista de números."""
#Francisco Llamas
numeros=[]
print("escriba salir para finalizar")
entrada=input("Escribe un numero")
while entrada!="salir":
    numeros.append(int(entrada))
    entrada=input("dame un numero")

print("los numeros introducidos son: ", numeros)

