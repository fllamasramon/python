#Francisco Llamas
#Practica 4 ejercicio 2
a=int(input("introduce un numero"))
b=int(input("introduce un numero"))
c=int(input("introduce un numero"))
d=int(input("introduce un numero"))
e=int(input("introduce un numero"))
if a >b and a >c and a >d and a >e:
    print("los números están en orden decreciente")
elif e >a and e >b and e >c and e >d:
    print("los números están en orden creciente")
else:
    print("los números están desordenados")
