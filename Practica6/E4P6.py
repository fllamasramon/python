"""Escribe un programa que te pida dos números,
de manera que el segundo sea mayor que el primero.
El programa termina escribiendo los dos números tal y como se pide:"""

numero=int(input("escriba un numero"))
numero2=int(input("escriba un numero que sea mayor que %d" % numero))
while numero2<=numero:
    numero2 = int(input('%d no es mayor que %d' % (numero2,numero)))

print("Has escrito", numero,"y",numero2)
