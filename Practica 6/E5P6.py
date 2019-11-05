"""Escribe un programa que te pida números
cada vez más grandes y que se guarden en una lista.
Para acabar de escribir los números,
escribe un número que no sea mayor que el anterior.
El programa termina escribiendo la lista de números:"""
#Francisco Llamas
lista=[]
entrada=int(input("introduzca un numero"))
entrada2=int(input("ntroduzca un numero"))

lista.append(entrada)
lista.append(entrada2)

while lista[-1]>lista[-2]:
    entrada=int(input("introduzca otro numero"))
    lista.append(int(entrada))


for i in range(len(lista)-1):
    print(lista[i], "", end="")

 
