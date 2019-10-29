#Francisco Llamas
#Práctica 4 ejercici 3
input("Pulse intro para continuar")
escribir=input("Pulse (C) si desea calcular el del cuadrado o (T) el del triangulo")
if escribir=="T":
    base=int(input("Introduzca la base"))
    altura=int(input("Introduza la altura"))
    area=base*altura/2
    print(area)
elif escribir=="C":
    lado=int(input("introduzca el lado"))
    z=lado*lado
    print(z)
