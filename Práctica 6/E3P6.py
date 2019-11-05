"""Escribe un programa que pida notas y los guarde en una lista.
Para terminar de introducir notas, escribe una nota que no esté entre 0 y 10.
El programa termina escribiendo la lista de notas."""
#Francisco Llamas
notas=[]
entrada=float(input("introduzca las notas"))
while entrada in range(11):
    notas.append(float(entrada))
    entrada=float(input("deme otra nota o pulse 11 para salir"))

print("Las notas introducidas son: ", notas)
