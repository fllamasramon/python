#Francisco Llamas
#Práctica 5 ejercicio 7
altura=int(input("introduzca la altura del triángulo"))
for i in range(altura):
    for j in range(altura, i, -1):
        print("* ",end="")
    print()
